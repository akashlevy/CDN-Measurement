# CCS'16 Key Sharing Datasets
# ASN to Organization Mapping
# Frank Cangialosi
# November 2016

The raw data from CAIDA is included in the data/ folder.

saveDB() in as2ISP.py can parse this data, however we've included the data
structure as a result of running this function in as2isp.pkl, which can be used
as follows:

1. Import as2ISP functions (may need sys.path.insert(...) if not in current dir)

  from as2ISP import *

2. Create an instance:
  
  as2isp = AS2ISP()

3. Get the organization name for ASN X on date YYYYmmdd:

  as2isp.getISP("YYYYmmdd", "X")
