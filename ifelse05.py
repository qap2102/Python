from math import *
x1, y1, x2, y2 = map(int, input().split())
k = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
can = float(sqrt(k))
print("%.2f" %can)
