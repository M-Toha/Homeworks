# Practice section 1:

# 1. Write a program that caluculate Fibonacci series. 
'''The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. 
Number of iterations should be taken from user input.'''

iteration = int(input('Enter number of iterations: '))
def fibonacci(iter) -> int:
    a = 0
    b = 1
    for i in range(1, iter + 1):
        print(b)
        a,b = b, a+b              
fibonacci(iteration)

# Practice section 2

# 1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.

def div_three(num):
    for i in range(0,num + 1):
        if i % 3 != 0:
            continue
        print(i)
print(div_three(100))

# 2. Get a number from user input and iterate from 0 to that number.
'''Print 'foo' if the number is divisible by 3.
Print 'bar' if the number is divisible by 5.
Print 'foobar' if the number is divisible by both 3 and 5.'''

def foobar(number):
    for i in range(0, number + 1):
        if i % 15 == 0: print('foobar', i)
        elif i % 3 == 0: print('foo', i)
        elif i % 5 == 0: print('bar', i)
        else: continue
    return 'The end'
number = int(input('Enter your number: '))
print(foobar(number))

# Practice block 3:

# 1. Write a function called square() with one argument of int type
#  and returns the value of that number raised to the second power.

def square(a:int)->int:
    a **= 2
    return a
print(square(4))

# 2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit.
# It should take a number as an argument from user input and return a number to the console.

def convert_cel_to_fahr() -> float:
    temp_cels = float(input('Enter the Celsius temperature: '))
    temp_fahr = temp_cels * 1.8 + 32
    print(f'The Fahrenheit temperature is {temp_fahr}')
convert_cel_to_fahr()

# 3. Write a function that implement case swapping. It should return the same result as swapcase() method. 
# Your function should accept one str argument and convert all lower case values to upper case and vice versa.

string = input('Enter your text: ')
def swapcase(string: str) -> str:
    swap_string = ''
    for i in range(0, len(string)):
        swap_string += string[i].upper() if string[i].islower() else \
              string[i].lower() if string[i].isupper() else string[i]
    return swap_string
        
print(swapcase(string))
print(string.swapcase())
print(swapcase(string) == string.swapcase())

# Task 1.Опціонально. Дискримінант. Створіть функцію з іменем discriminant.
# Функція повинна приймати на вхід a, b, c, choose. Де a, b, c - це аргументи функції, 
# choose - опціональний параметр, вибору способу рішення(дискримінант або Вієта, 1 - disc, 2 - Вієта)
# Функція повинна повертати в залежності від параметрів один/два кореня або їх відсутність.
'''
Example:
Input: a = 5, b = -8, c = 3
Output: x = 1, x = 0.6 Результати округлювати до 2 знаку. 
Функція повинна перевіряти тип аргументів(int повинен бути).'''

def discriminant(a: int, b: int, c: int, choose = 1) -> float:
    if isinstance(a, int) == False or isinstance(b, int) == False or isinstance(c, int) == False or choose not in (1,2):
        return 'Некоректні аргументи функції'
    else:
        if a == 0:
            if b == 0: 
                if c == 0: return 'Коренів нескінченно багато' 
                else: return 'Коренів немає'
            else: x1 = -c/b
            return f'x = {round(x1,2)}'
        else:
            disc = b**2 - 4*a*c
            if disc < 0: 
                return 'Дійсних коренів немає'
            elif disc == 0:
                x1 = -b/(2*a)
                return f'x = {round(x1,2)}'
            else:
                x1 = (-b + disc**(1/2))/(2*a)
                x2 = (-b - disc**(1/2))/(2*a) if choose == 1 else -b/a - x1
                return f'x = {round(x1,2)}, x = {round(x2,2)}'

print(discriminant(1,5,-6))      



    