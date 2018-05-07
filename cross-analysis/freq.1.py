import csv, operator, sys
freq = {}
refcdns = [u'Limelight', u'Yunjiasu', u'CDNvideo', u'OnApp', u'Internap', u'Cloudflare', u'Medianova', u'Cotendo', u'PageRain', u'Rackspace', u'StackPath', u'LeaseWeb', u'NetDNA', u'OVH', u'ReSRC', u'Yahoo', u'KINX', u'Aryaka', u'Instart Logic', u'HiberniaCDN', u'Cedexis', u'Yottaa', u'Caspowa', u'Hosting4CDN', u'Edgecast', u'Mirror Image', u'BO.LT', u'Cachefly', u'Twitter', u'SFR', u'UnicornCDN', u'Airee', u'Blue Hat Network', u'KeyCDN', u'Rev Software', u'Sucuri Firewall', u'Level 3', u'Highwinds', u'Optimal', u'Amazon', u'Akamai', u'Reflected Networks', u'afxcdn.net', u'cubeCDN', u'MediaCloud', u'ChinaCache', u'Fastly', u'BitGravity', u'NGENIX', u'NYI FTW', u'GoCache', u'Facebook', u'CDNetworks', u'AT&T', u'Bison Grid', u'Microsoft Azure', u'Alimama', u'Advanced Hosters', u'Incapsula', u'Surge', u'Azion', u'Roast.io', u'Taobao', u'jsDelivr', u'CDN77', u'Naver', u'Simple', u'Reapleaf', u'SwiftCDN', u'Google', u'ChinaNetCenter', u'Netlify', u'BunnyCDN', u'Telenor', u'CDNsun', u'VoxCDN', u'section.io', u'WordPress', u'Zenedge', u'TRBCDN']
for line in csv.reader(open(sys.argv[1]), delimiter=',', quotechar='"'):
    cdn = line[1].strip()
    for refcdn in refcdns:
        try:
            if refcdn.lower() in cdn.lower():
                cdn = refcdn
        except UnicodeDecodeError:
            pass
    
    freq[cdn] = 1 if cdn not in freq else freq[cdn] + 1

for cdn, freq in sorted(freq.items(), reverse=True, key=operator.itemgetter(1)):
    print "%s & %s \\\\" % (cdn, freq)

