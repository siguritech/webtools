import sys
from ipwhois.net import Net
from ipwhois.asn import IPASN

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line:
            obj = IPASN(Net(line.strip()))
            result = obj.lookup()
            txt = "[[{line}]] [[{asn}]] {result}".format(line=line.strip(), asn=result['asn'], result=result)
            print(txt)
            
