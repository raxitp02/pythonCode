#hashGen.py

#imported hashlib that contains algos for

#perfect hash value genetration

import hashlib

#list that conating names

list = [ "Raxit","Acdemy:CSIS","Ricky","Jay","ID#209838" ]

#printing hash value of each name in list

for name in list:

print(name+" : ",hashlib.md5(name.encode('utf-8')).hexdigest())