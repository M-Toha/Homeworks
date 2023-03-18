'''
1. Print('Hello world') - синтаксична помилка
   a,b = 1,2 
   print('a= ',b) - логічна помилка

2. 1/0 видасть помилку, тому що значення виходить за область допустимих значень 
   0/1 дорівнюватиме нулю - ця операція дозволена і не виходить за область допустимих значень

3. Коментарі потрібні для того, щоб добре орієнтуватись у власному коді, а також щоб можна було зрозуміти код, написаний іншою людиною

4. Змінна - це проіменована частинка пам'яті, що містить в собі певне значення
'''
#Практична частина 

# 1. Написати програму яка отримує від користувача два числа. Вивести ці два числа в консоль
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(a,b)

# 2. Провести та вивезти над ними всі базові арифметичні операції в print
print('Сума a+b: ',a+b)
print('Різниця a-b: ',a-b)
print('Добуток a*b: ',a*b)
print('Частка a/b: ',a/b)

# 3. Додати функціонал по знаходженню степені числа. Перше число є базою, друге - ступенем. 
#    Вивести результат в консоль у форматі "а в b степені це c»
print('а в b степені це ',a**b)

# 4. Додати можливість працювати зі float
a = float(a)
print(a)

# 5. Прийняти від користувача ім'я, призвіще, вік, вивезти одним print:
name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('How old are you: '))
print(name, surname, 'You are', age, 'years old')

#Practice

# 1. Write a program that get two int variables and swap their values. Do it in 3 different ways.
a=3
b=5

#First way - with 3-rd variable
c=a 
a=b 
b=c
print(a,b)

#Second way - without 3-rd variable
a=a+b
b=a-b
a=a-b
print(a,b)

#Third way
a, b = b, a
print(a,b)

# 2.Write a program that get 2 numbers from the user. 
#   Print to the console maximum of this two variable.
c = int(input('Enter first number: '))
d = int(input('Enter second number: '))
print('Maximum is: ',max(c,d))

# 3.Optional: Write a program that get 3 digit number from the user and reverse it.
e = int(input('Enter a number: '))
e1 = e//100                         # Get 3-rd digit
e2 = (e-e1*100)//10                 # Get 2-nd digit
e3 = e-e1*100-e2*10                 # Get 1-st digit
e_reversed = e3*100+e2*10+e1        # making reversed value
print('Reversed number is ', e_reversed)
