import pyasn

# Initialize module and load IP to ASN database
# the sample database can be downloaded or built - see below
asndb = pyasn.pyasn('ip2asn')

ips = set([line.strip() for line in open('torlist-2017-12-20.txt')])

with open('ip2as.txt','w') as outfile:
  for ip in ips:
    try:
      asn = asndb.lookup(ip)
      outfile.write("%s,%s\n" % (ip, asn[0]))
    except Exception as e:
      print e
      
