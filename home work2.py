# Exercise 1.
#for i in range(7, 100, 7):
#      print(i)
# Exercise 2.
'''n = int(input("enter"))
sum = 1
x = n
while 4 < n < 16:
    if x == 1:
        break
    while x > 1:
         sum = x * sum
         x = x-1
print(sum)'''
# Exercise 3.
'''FIRST = 5
for i in range (11):
    print(i, "x", FIRST, "=", i * FIRST, end='  ')'''
# Exercise 4.
'''ONE = int(input("enter"))
TWO = int(input("enter"))
while ONE > 0 :
    print("*"*TWO)
    ONE -=1'''
# Exercise 4.
'''ONE = int(input("enter"))
TWO = int(input("enter"))
while ONE > 0 :
    print("*"*TWO)
    ONE -=1'''
# Exercise 5.
'''my_list = [0, 5, 2, 4, 7, 1, 3, 19]
even = []
not_even = []
for x in my_list:
    if x % 2 == 0 and x !=0:
       even.append(x)
    elif x != 0:
       not_even.append(x)
print("even = ", len(even))
print("not_even = ", len(not_even))'''
# Exercise 6.
'''my_list = [0, 5, 2, 4, 7, 1, 3, 19]
new_list = my_list
for x in new_list[0:4]:
    i = x * 2
    new_list.append(i)
print(new_list)'''
# Exercise 7.
'''import random
x = 0
salary = []
for i in range (12):
    salary.append(random.randrange(7500, 15000))
print(salary)
avg = sum(salary) // len(salary)
print("average monthly salary =", avg, "grn")'''
# Exercise 8.
'''matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
sum = 0
for i in matrix:
     for j in i:
        sum = j + sum
     print(i)
print("sum = ", sum)'''
#1)
k = 0
for i in range(2, 101):
    for z in range (2, i):
        if i % z == 0:
            k += 1
        if k == 0:
           print(i)
