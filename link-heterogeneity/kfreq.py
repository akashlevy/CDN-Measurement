import operator

freq = {}
for line in open('outputfinal'):
    freq[int(line.split(',')[-1])] = 1 if int(line.split(',')[-1]) not in freq else freq[int(line.split(',')[-1])] + 1
for item in sorted(freq.items(), reverse=False):
    print str(item[0]) + ',', item[1]