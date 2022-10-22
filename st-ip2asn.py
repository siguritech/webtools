import sys
from ipwhois.net import Net
from ipwhois.asn import IPASN

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line:
            obj = IPASN(Net(line.strip()))
            result = obj.lookup()
            txt = "#ASN-{asn} \n\n {result}".format(asn=result['asn'], result=result)
            fname = line.strip() + ".md"
            f = open(fname, "w")
            f.write(txt)
            f.close()
            
