import json
from itertools import combinations, product

cross = {}
analysis = ['cname','hostname','rev']
for a in analysis:
    print a
    i = 0
    for line in open(a + '2cdn'):
        if i % 100000 == 0:
            print i
        i += 1
        hostname, cdn = line.split(',')
        cdn = cdn.strip()
        if hostname not in cross:
            cross[hostname] = {}
            for b in analysis:
                cross[hostname][b] = set()
        cross[hostname][a].add(cdn)

outputfile = open('cross2.csv', 'w')
combs = []
for comblen in range(1, len(analysis)+1):
    comb = list(combinations(analysis, comblen))
    combs += comb

combnames = ['+'.join(comb) for comb in combs]
outputfile.write(','.join(combnames)+'\n')

outputs = []
for hostname, data in cross.iteritems():
    output = []
    for comb in combs:
        output.append(str(len(set.intersection(*[data[a] for a in comb]))))
    outputfile.write(','.join(output)+'\n')

outputfile.close()
