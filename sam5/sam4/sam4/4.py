nub = int(input())
if nub<0:
    nub = nub*(-1)
z = nub//100
x = nub % 100 // 10
c = nub % 10
# 1000-7?
print (nub)
print(z*100+c*10+x)
print (x*100+z*10+c)
print (x*100+c*10+z)
print (c*100+z*10+x)
print (c*100+x*10+z)