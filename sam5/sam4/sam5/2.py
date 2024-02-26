z = int(input())
x = int(input())
c = int(input())
if x > z:
z, x = x, z
if c > x:
x, c = c, x
if x > z:
z, x = x, z
print(z, x, c)