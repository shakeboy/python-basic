import re

qq = '1234,88888888,2346901246,10000,666666,3,24682468'
res = re.findall('[1-9][0-9]{4,}',qq)
print("合法的qq号:",res)
