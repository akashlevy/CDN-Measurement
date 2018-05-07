import json

with open('hostname2ip_clean', 'w') as clean_out, open('ipaddrs', 'w') as ip_out:
  for line in open('hostname2ip'):
    spl = line.split()
    for ip in spl[1:]:
      clean_out.write('%s,%s\n' % (spl[0], ip))
      ip_out.write('%s\n' % ip)
