import csv, operator, sys
freq = {}
for line in csv.reader(open(sys.argv[1]), delimiter=',', quotechar='"'):
   cdn = line[1].strip()
   freq[cdn] = 1 if cdn not in freq else freq[cdn] + 1

for cdn, freq in sorted(freq.items(), reverse=True, key=operator.itemgetter(1)):
   print "%s & %s \\\\" % (cdn, freq)

