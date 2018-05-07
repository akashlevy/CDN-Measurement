import dns.resolver

with open('hostnames') as infile, open('cnames', 'w') as outfile:
    for i, line in enumerate(infile):
        if i < 2884:
            continue
	try:
            print i
            print line.strip()
            cname = str(dns.resolver.query(line.strip(), 'CNAME')[0])
            print cname
            outfile.write(line.strip() + ',')
            outfile.write(cname + '\n')
        except Exception as e:
            print line.strip() + ' failed with ' + str(e)
