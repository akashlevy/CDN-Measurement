import csv, json
data = json.load(open('../cdn.json'))
refcdns = set(data['vendors'].values()).union(set([entry[2] for entry in data['headers']]))
i=0
with open('as2cdn', 'w') as outfile:
    for line in csv.reader(open('as2cdn_pre'), delimiter=',', quotechar='"'):
        if i % 10000 == 0:
            print i
        i += 1
        hostname, cdn = line
        cdn = cdn.strip()
        found = False
        for refcdn in refcdns:
            try:
                if refcdn.lower().replace(" cdn", "").replace("amazon cloudfront", "amazon").strip() in cdn.lower():
                    outfile.write('%s,%s\n' % (hostname, refcdn))
                    found = True
                    break
            except UnicodeDecodeError:
                pass
        if not found:
            outfile.write('%s,Other\n' % hostname)
