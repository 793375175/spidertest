import re

str = 'abc123cd'
rs = re.findall('\d', str)
rs = re.findall('\d*', str)
rs = re.findall('\d+', str)
rs = re.findall('\d?',str)
print(rs)

print('ab\nc'=='ab\nc')  #True
print(r'ab\nc'=='ab\nc')  #False