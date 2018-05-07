from urlparse import urlparse
import operator
i = 0
freq = {}
for line in open('final'):
    if i % 1000 == 0:
        pass#print i
    url, links, ref_hd, meta_hd = eval(line)
    if links is None:
       continue
    try:
        clean_links = repr(sorted(list(set([link.replace('http://','//').replace('https://','//') for link in links if (link[:2] == '//' or link[:7] == 'http://' or link[:8] == 'https://') and url.strip() not in urlparse(link.strip()).netloc]))))
    except:
        continue
    #print url.strip(), clean_links
    i += 1

    freq[clean_links] = 1 if clean_links not in freq else freq[clean_links] + 1
    #freq[meta_hd] = 1 if meta_hd not in freq else freq[meta_hd] + 1

i = 0
sumf = 0
for ref, freq in sorted(freq.items(), reverse=True, key=operator.itemgetter(1)):
    if freq == 1:
        break
    print "%s & %s \\\\" % (ref, freq)
    i+=1
    sumf += freq
print sumf
