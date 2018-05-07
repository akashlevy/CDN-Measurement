from ipwhois import IPWhois, IPDefinedError

ips = set([line.strip() for line in open('torlist-2017-12-20.txt')])

outfile = open('ip2whois.txt', 'w')

for ip in ips:
  try:
    who = IPWhois(ip)
    try:
      name = who.lookup_whois(get_referral=True)
      print '%s,%s\n' % (ip,name)
      outfile.write('%s,%s\n' % (ip,name.encode('ascii', 'ignore').decode('ascii')))
    except (TypeError, KeyError):
      pass
  except: #(UnboundLocalError, IPDefinedError):
    pass

outfile.close()
