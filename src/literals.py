a = 1e9

print(a)
print(int(a))

b = 0o123 # octal number

print(b)

c = 0x123 # hexadecimal number

print(c)

d = 10.51

print(type(d))


e = 1_000_000 # more readable

print(e)

f = 'A'

print(ord(f))
print(type(f))

g = True

print(g)
print(type(g))

''' Output: 
1000000000.0
1000000000
83
291
<class 'float'>
1000000
65
<class 'str'>
True
<class 'bool'>
'''