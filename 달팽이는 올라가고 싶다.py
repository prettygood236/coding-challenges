import math

A,B,V = map(int,input().split())


d = (V-A)/(A-B)

print(math.ceil(d)+1)