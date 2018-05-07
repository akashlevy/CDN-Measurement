from ipwhois import IPWhois, IPDefinedError

ips = set([line.strip() for line in open('torlist-2017-12-20.txt')])

outfile = open('ip2rdap.txt', 'w')

for ip in ips:
  try:
    who = IPWhois(ip)
    for obj in who.lookup_rdap(depth=1)['objects'].values():
      try:
        print obj
        contactname = obj['contact']['name']
        print '%s,%s\n' % (ip,contactname)
        outfile.write('%s,%s\n' % (ip,contactname.encode('ascii', 'ignore').decode('ascii')))
      except (TypeError, KeyError):
        pass
  except: #(UnboundLocalError, IPDefinedError):
    pass

outfile.close()
