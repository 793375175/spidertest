str = '你好'
print(type(str))

print(str.encode())
print(type(str.encode()))

byte = str.encode('GBK')

print(byte)
print(type(byte))
print(byte.decode('GBK'))
print(type(byte.decode('gbk')))
