import sys
from ipwhois.net import Net
from ipwhois.asn import IPASN
from pprint import pprint

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line:
            obj = IPASN(Net(line.strip()))
            result = obj.lookup()
            pprint(result)
