## Practice section

# 1. Figure out the result of the following expressions:
''' a) False
    b) False
    c) True
    d) False
'''
# 2. Make all of them True by adding parentheses:
'''    a) False == (not True)
    b) (True and False) == (True and False)
    c) not (True and "A"=="B")
'''

# Practice section 2
# 1. Write a Python program that reads two integers representing a month and prints the season for that month.
#  Get month from the user input.
'''
Expected Output:
Input the month: october
Season is autumn'''

month_season = input('Input the month: ')
print('Season is',end=' ')
match month_season.lower():
    case 'december': print('winter')
    case 'january': print('winter')
    case 'february': print('winter')
    case 'april': print('spring')
    case 'april': print('spring')
    case 'may': print('spring')
    case 'june': print('summer')
    case 'july': print('summer')
    case 'august': print('summer')
    case 'september': print('autumn')
    case 'october': print('autumn')
    case 'november': print('autumn')
    case _: print('unknown')

# 2. Write a Python program to get next day of a given date. 
# Get day, month and year from the user input.
'''Expected Output:
**Input a year:** 2022                                                     
**Input a month [1-12]:** 8                                               
**Input a day [1-31]:** 23                                           
The next date is [yyyy-mm-dd] 2022-8-24'''

year = int(input('Input a year: '))
if year == 0:
    print('Incorrect year')
else:
    month = int(input('Input a month [1-12]: '))
    if month > 12 or month < 1: 
        print('Incorrect month')
    else:
        day = int(input('Input a day [1-31]: '))
        if day < 1 or day > 31 or (day > 30 and month in (2,4,6,9,11))\
        or (day > 29 and month == 2) or (day == 29 and month == 2\
        and not(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
            print('Incorrect day')
        else:
            if day == 31 and month == 12:
                if year+1 < 0: print(f'{-(year+1)}-1-1 BC')
                if year+1 == 0: print(f'1-1-1')
                else: print(f'{year+1}-1-1')
            elif day == 31 or (day == 30 and month in (4,6,9,11))\
            or (day == 29 and month == 2)\
            or (day == 28 and month == 2 and not (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
                if year < 0: print(f'{-year}-{month+1}-1 BC')
                else: print(f'{year}-{month+1}-1')
            else: 
                if year < 0: print(f'{-year}-{month}-{day+1} BC')
                else: print(f'{year}-{month}-{day+1}')

# 3. Get a phrase from user input. Display whether the lenght of the string if longer than 5 characters, 
# equal to 5 characters or shorter than 5 characters. Use if, elif, else for this.

string = input('Enter your phrase: ')
print('Your phrase is',end=" ")
if len(string) > 5: print('longer then five characters')
elif len(string) == 5: print('five characters long')
else: print('shorter then five characters')

# 4. Get a positive number from user input. Find all factors of this number.
'''Example:
If the number is 6, the factors are: 1, 2, 3, 6
If the number is 10, the factors are: 1, 2, 5, 10'''

number = int(input('Enter a positive integer: '))
while number <= 0:
        print('This number in not a positive integer')
        number = int(input('Enter a positive integer: '))
for i in range(1, number + 1):
    if number % i == 0: print(i, end='' if i == number else ', ')       

# 5. Write a Python program to check a triangle is equilateral, isosceles or scalene. 
# Get all three sides from user input.

a = float(input('Enter the first side of a triangle: '))
b = float(input('Enter the second side of a triangle: '))
c = float(input('Enter the third side of a triangle: '))
if a + b <= c or a + c <= b or c + b <= a:
    print('These sides do not form a triangle')
else:
    print("The triangle is ",end='')
    if a == b and a == c: print('equilateral')
    elif a == b or a == c or b == c: print('isosceles')
    else: print('scalene')

# Practice section 3:
# 1. Write a for loop that prints out the integers from 2 to 10, each on a new line, by using the range() function.

for i in range(2,11):
    print(i)

# 2. Use a while loop that prints out the integers from 2 to 10

i = 1
while i < 10:
    i += 1
    print(i)

# 3. Write a program that takes number as its input and doubles that number few times in a loop. 
# Number of iterations and initial number should be taken from user input. 
# You should display each result on a separate line. Here is some sample output:
'''Input:
initial number: 2
number of iterations: 5

Output:
4
8
16
32
64'''

initial = int(input('Enter initial number: '))
iteration = int(input('Enter number of iterations: '))
for i in range(1, iteration + 1):
    initial *= 2
    print(initial)

# 4. Write a program that caluculate Fibonacci series. 
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. 
# Number of iterations should be taken from user input.

iteration = int(input('Enter number of iterations: '))
a = 0
b = 1
for i in range(1, iteration + 1):
    print(b)
    a,b = b, a+b

# 5. Write a program that takes a number as input and revert it using math operators. 
# You might use result of the exercise from the first lesson. 
# Here you should be able to do it not only for three-digit numbers, but for any numbers.

number = int(input('Enter your number: '))
number1 = number if number >=0 else -number
reverse = 0
while number1 > 0:
    reverse = reverse*10 + number1 % 10
    number1 //= 10
print(number, reverse if number >= 0 else -reverse)

# Practice section 4
# 1. Write a program that always asks user to input somethings. Quit only if user inputs 'q' or 'Q'.

while True:
    a = input('Enter something (\'q\' or \'Q\' to quit): ')
    if a in ('q','Q'):
        break

# 2. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.

for i in range(0,101):
    if i % 3 != 0:
        continue
    print(i)

# 3. Get a number from user input and iterate from 0 to that number.
'''
A. Print 'foo' if the number is divisible by 3.
B. Print 'bar' if the number is divisible by 5.
C. Print 'foobar' if the number is divisible by both 3 and 5.'''

number = int(input('Enter your number: '))
for i in range(0,number+1):
    if i % 15 == 0: print('foobar', i)
    elif i % 3 == 0: print('foo', i)
    elif i % 5 == 0: print('bar', i)
    else: continue

