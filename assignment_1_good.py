from random import *
from statistics import mean, median

# initialize list my_randoms
my_randoms = []

# fill list with 100 random integers between -500 and 500
for i in range(100):
    my_randoms.append(randint(-500,500))

# find max/min values in the list
max_value = max(my_randoms)
min_value = min(my_randoms)

# calculate and store second max value
second_max_value = second_max(my_randoms)

# calculate and store second min value
second_min_value = second_min(my_randoms)

# find mean value in the list
mean_value = mean(my_randoms)

# find median value in the list
median_value = median(my_randoms)

# function for find the second max in the list
def second_max(list):
    m1, m2 = min(list), min(list)
    for x in list:
        if x >= m1:
            m1, m2 = x, m1
        elif x > m2:
            m2 = x
    return m2

# function for find the second min in the list
def second_min(list):
    m1, m2 = max(list), max(list)
    for x in list:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

# print friendly output to console
print('The maximum value of the list is:', max_value)
print('The minimum value of the list is:', min_value)
print('The next maximum value of the list is:', second_max_value)
print('The next minimum value of the list is:', second_min_value)
print('The mean value of the list is:', mean_value)
print('The median value of the list is:', median_value)
