import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import codecs

from bs4 import BeautifulSoup
from multiprocessing import Pool, Lock

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Index for crawl from the third month of 2018
index = "2018-13"

#
# Searches the Common Crawl Index for a domain.
#
def search_domain(domain):
    print "[*] Trying target domain: %s" % domain
    
    cc_url  = "http://localhost:8080/CC-MAIN-%s-index?" % index
    cc_url += "matchType=domain&url=%s&fl=filename,offset,length&limit=1&output=json" % domain
    response = requests.get(cc_url)
    return json.loads(response.content)

#
# Downloads a page from Common Crawl - adapted graciously from @Smerity - thanks man!
# https://gist.github.com/Smerity/56bc6f21a8adec920ebf
#
def download_page(record):
    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1

    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    # Getting the file on S3 is equivalent however - you can request a Range
    prefix = 'https://commoncrawl.s3.amazonaws.com/'
    
    # We can then use the Range header to ask for just this set of bytes
    resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    
    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = StringIO.StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)
    
    # What we have now is just the WARC response, formatted:
    data = f.read()
    
    response = ""
    header = ""
    
    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass

    referrer_header = None
    for h in header.split('\n'):
        if h[:16] == 'Referrer-Policy:':
            referrer_header = h[17:].strip()

    return response, referrer_header

#
# Extract links from the HTML  
#
def extract_external_links(html_content):
    parser = BeautifulSoup(html_content, "lxml")
    meta_ref = None
    try:
        meta_ref = parser.find('meta', {'name': 'referrer'})['content']
    except:
        pass
    return [src['src'] for src in parser.find_all(src=True)], meta_ref

outfile = open('results', 'w')
final = open('final', 'w')
lock = Lock()

def process_search_domain(line):
    _, site = line.split(',')
    search = search_domain(site)
    lock.acquire()
    outfile.write(repr((site, search)))
    outfile.write('\n')
    outfile.flush()
    lock.release()

def process_download_extract(result):
    site, search = eval(result)
    print site
    if 'error' in search:
        lock.acquire()
        final.write(repr((site, None, None, None)))
        final.write('\n')
        final.flush()
        lock.release()
    else:
        resp, ref_hd = download_page(search)
        links, meta_hd = extract_external_links(resp)
        lock.acquire()
        final.write(repr((site, links, ref_hd, meta_hd)))
        final.write('\n')
        final.flush()
        lock.release()

#Pool(128).map(process_search_domain, open('top-1m.csv'))
Pool(128).map(process_download_extract, open('index_results'))

outfile.close()
final.close()

