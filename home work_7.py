#1)
"""def mx(*lst):
    #this function defines the maximum integer from the list
    return max(lst)
x = mx(100, 120, 40, 30, 155)
print(x)"""
#2)
"""def sum(a, b, /, c):
    #function adds two numbers (a) and (b) and concatenation them to string (c)
    return str(a + b)+" " + c

z = sum(20, 30, c = "Qwerty")"""
#3)
"""def picture(lenght, width):
   #the function reads two parameters, the height and width of the rectangle, and renders as asterisks
    for i in range(0, width):
        print("* " * lenght)

picture(int(input("lenght == ")), int(input("width == ")))"""
#4)
"""def search(c, list):
    #There are two arguments, a list and an element that we are looking for in the list, if successful, we display the index of the element on the screen, if we did not find it, we output the number -1
    if c in list:
        return list.index(c)
    else:
        return -1

z = search((10),(1,20,30,10))
print(z)"""
#5)
"""def count(line):
    #parameter string reads a string and counts repeated characters
    x = {}
    for elem in line:
        if elem in x:
            x[elem] +=1
        else:
            x[elem] = 1
    return x

z = count("parameter string reads")
print(z)"""