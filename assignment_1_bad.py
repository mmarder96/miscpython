from random import *
















































l = []
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
l.append(randint(-500,500))
def max1(l):    
    max_val = None
    for value in l:
        if not max_val:
            max_val = value
        elif value > max_val:
            max_val = value
    return max_val
def min1(somelist):
    min_value = None
    for value in somelist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value
max1 = max1(l)
print (max1)
min1 = min1(l)
print (min1)
m1 = min1
m2 = min1
for x in l:
    if x >= m1:
        m1, m2 = x, m1
    elif x > m2:
        m2 = x
print (m2)
m3 = max1
m4 = max1
for x in l:
    if x <= m3:
        m3, m4 = x, m3
    elif x < m4:
        m4 = x
print(m4)
a = sum(l) / len(l)
print (a)
med = None
if len(l) < 1:
    med = None
if len(l) % 2 == 1:
    med = sorted(l)[len(l)//2]
else:
    med = sum(sorted(l)[len(l)//2-1:len(l)//2+1])/2.0
print(med)