# Exercise 1.
'''text = input("Enter")
sum_b = 0
for elem in text:
    if "b" == elem:
        sum_b = 1 + sum_b
        continue
print(sum_b)'''
# Exercise 2.
'''while True:
    name = input("write your name -")
    name = name.lower()
    name = name.title()
    if name.isalpha():
        print("Your name is", name)
        break
    else:
        print(name, "is incorrect name")'''
# Exercise 3.
'''text = input("Print text \n")
sum = 0
for ltr in text:
    sum += ord(ltr)
print("summa =", sum)'''
# Exercise 4.
'''import math
h = 2
while h < 16:
    print("Pi = {:.{num}f}".format(math.pi, num=h))
    h +=1'''
# Exercise 5.
'''text = input("Enter").split(" ")
length_ltr = text[0]
for ltr in text:
    if len(ltr) >= len(length_ltr):
        length_ltr = ltr
print("The string has the most characters =", length_ltr)'''
# Exercise 6.
'''text = "catcatcatcat ".lower()
word = ""
for letter in text:
    if not letter in word:
        word += letter
print(word)'''

