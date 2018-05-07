import operator, sys
freq = {}
print sys.argv
for line in open(sys.argv[1]):
   _, cdn = line.split(',')
   cdn = cdn.strip()
   freq[cdn] = 1 if cdn not in freq else freq[cdn] + 1

for cdn, freq in sorted(freq.items(), reverse=True, key=operator.itemgetter(1)):
   print "%s & %s \\\\" % (cdn, freq)
