cat hostnames | awk '!/([^a-zA-Z0-9._-])|(^[.])|([.][.])|(.{63,})/' | ./go-bulk-dns-resolver/bulkdns > results2.txt