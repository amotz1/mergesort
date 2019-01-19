from typing import List

x = [3, 5, 8, 7]
a = x[0:int(len(x) / 2)]
b = x[int(len(x) / 2):int(len(x))]
print("a=", a)
print("b=", b)
if a[0] > a[1]:
    a[0], a[1] = a[1], a[0]
if b[0] > b[1]:
    b[0], b[1] = b[1], b[0]
print("a=", a)
print("b=", b)
c = []
if a[0] < b[0]:
    c.append(a[0])
else:
    c.append(b[0])
print(c)
if a[0] > a[1]:
    a[0], a[1] = a[1], a[0]
if b[0] > b[1]:
    b[0], b[1] = b[1], b[0]
if a[1] < b[1]:
    c.append(a[1])
else:
    c.append(b[1])
print(c)
print(a)
print(b)
