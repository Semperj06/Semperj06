#1
def peculiarity(n):
    index = 0
    multiplier = 2
    while index < n:
        user_multiplier = (yield index ** multiplier)
        index += 1
        if not user_multiplier is None:
            multiplier = user_multiplier


#2
def user_range(start, stop, step):
    while start < stop+1:
        yield start
        start += step


#3
def prime_numbers(stop):
    for a in range(2, stop):
        k = 0
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                k = k + 1
        if k <= 0:
            yield a


#4
user_list = [x ** 3 for x in range(2, 20)]


#5

def sequence(n):

    def logic(s):
        x = s
        while n * s > x:
            yield x
            x += s
    return logic

f = sequence(15)
logic = f(6)

#6

def fibonacci():
    mem = {}

    def mem_fun(n):
        nonlocal mem
        i = 0
        fib1 = 1
        fib2 = 1
        if n in mem:
            return mem[n]
        else:
            while i < n - 2:
                fib_sum = fib1 + fib2
                mem[i+1] = fib2
                i += 1
                fib1 = fib2
                fib2 = fib_sum
        return fib2
    return mem_fun



#7
def sum(list, user_function):
    result = 0
    for elem in list:
        result += user_function(elem)
    return result

def squared(a):
    b = a * 2
    return b


list = [x for x in range(2, 5)]

a = sum(list, squared)
b = sum(list, lambda x: x**2)

