import json

iprev = {}
for line in open('hostname2ip'):
  spl = line.split()
  for ip in spl[1:]:
    if ip in iprev:
      iprev[ip].append(spl[0])
    else:
      iprev[ip] = [spl[0]]

with open('hostname2rev','w') as outfile:
  i = 0
  for line in open('20171108-rdns.json'):
    if i % 1000000 == 0:
      print i
    try:
      ipdata = json.loads(line)
      for name in iprev[ipdata['name']]:
        outfile.write("%s,%s\n" % (name, ipdata['value']))
        outfile.flush()
    except KeyError:
      pass
    i += 1
