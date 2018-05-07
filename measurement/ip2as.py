import pyasn

# Initialize module and load IP to ASN database
# the sample database can be downloaded or built - see below
asndb = pyasn.pyasn('ip2asn')

iprev = {}
for line in open('hostname2ip'):
  spl = line.split()
  for ip in spl[1:]:
    if ip in iprev:
      iprev[ip].append(spl[0])
    else:
      iprev[ip] = [spl[0]]

with open('hostname2as','w') as outfile:
  for ip, hostnames in iprev.items():
    try:
      asn = asndb.lookup(ip)
      for hostname in hostnames:
        outfile.write("%s,%s\n" % (hostname, asn[0]))
    except Exception as e:
      print e
      
