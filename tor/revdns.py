import json, os, socket

# Retrieve Tor IP addresses
ips = set([line.strip() for line in open('torlist-2017-12-20.txt')])

# Write resolved addresses out
with open('revdns.txt','w') as outfile:
  i = 0
  for ip in ips:
    try:
      print i
      i += 1
      outfile.write("%s,%s\n" % (ip, socket.gethostbyaddr(ip)[0]))
    except Exception as e:
      print str(e) +  "Failed line for some reason?"
