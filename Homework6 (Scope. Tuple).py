# Practice block 1:

# 1. Create an outer function that will accept two parameters, a and b
# 2. Create an inner function inside an outer function that will calculate the addition of a and b
# 3. At last, an outer function will add 5 into addition and return it

def outer(a: int, b: int) -> int:
    def inner() -> int:
        return a + b
    return inner() + 5

outer(2,4)

# Practice block 2
# 1. Write a program that asks user to enter an integer and convert it to int. 
# If the user enters something that is not an integer, program should catch an error and ask the user to enter an integer again. 
# if user inputs an integer, program should print this number and quit w/o any error.

def int_number() -> int:
    not_int = True
    while not_int == True:
        _value = input('Enter your integer number: ')
        try:
            int_value = int(_value)
        except ValueError: 
            print('This is not an integer. Please try again: ')
        not_int = not (_value.isdigit() or _value[0] == '-' and _value[1::].isdigit())
    return int_value
print(int_number())
# 2. Write a program that asks the user to input a string and an integer n.
#  Then display the character at index n in the string. 
# You should handle an error properly and display proper error message.

string = input('Enter your integer string: ')
n = int_number()
if n >= len(string) or n < -len(string):
    raise ValueError(f"There's no {n}-th position in the string")
Else: print(f'The character at index "{n}" in the string "{string}" is "{string[n]}"')

# Practice block 3:

# 1. Write a function that simulate a dice roll and returns the result from 1 to 6.
import random

def diceroll() -> int:
    return random.randint(1,6)
diceroll()

# 2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
def ten_thous_rolls(n:int) -> int:
    a1, a2, a3, a4, a5, a6 = 0, 0, 0, 0, 0, 0
    for i in range(1, n + 1):
        match random.randint(1,6):
            case 1: a1 += 1
            case 2: a2 += 1
            case 3: a3 += 1
            case 4: a4 += 1
            case 5: a5 += 1
            case 6: a6 += 1
    return(f'Number of 1s: {a1}\nNumber of 2s: {a2}\nNumber of 3s: {a3}\n\
Number of 4s: {a4}\nNumber of 5s: {a5}\nNumber of 6s: {a6}')
print(ten_thous_rolls(10000))

# 3. Simulate an election for two candidates. 
# Program should take amount of regions and rating for 1st candidate in each region (in percentage). 
# Program should run election in every region. In every region, program should ask 10 000 voters. 
# Candidate count as a winner if he gains more than 50% of all votes. 
# Program should print the result of the election for each region and the winner

'''Example:

Enter number of regions: 2

Enter rating for 1st candidate in each region: 34, 56

Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate

Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate

Result: 2nd candidate won with 10900 votes and 54.5% of all votes'''

print('Enter number of regions: ')
number_regions = int_number()  # використано ф-ію з завдання 2.1
rating_candidate1 = input('Enter rating for 1st candidate in each region: ').strip().split(',')

#перевірка відповідності к-сті регіонів і к-сті рейтингів
if len(rating_candidate1) < number_regions:         
    print('You have not listed all the ratings')
elif len(rating_candidate1) > number_regions:
    print('You have listed too many ratings')
else:
    # перевірка коректності рейтингів
    number_errors = 0
    for i in range(1, number_regions + 1):
        if int(rating_candidate1[i-1]) > 100 or int(rating_candidate1[i-1]) < 0:
            print(f'The rating in region {i} is incorrect')
            number_errors += 1
            break                            
    if number_errors == 0:
        votes_total1 = 0
        for i in range(1, number_regions + 1):
            votes1 = 0
            for j in range(1, 10001):
                if random.randint(1, 100) <= int(rating_candidate1[i-1]):
                    votes1 += 1
            print(f'Region {i}: {votes1} votes for 1st candidate, {10000 - votes1} votes for 2nd candidate')
            votes_total1 += votes1
        if votes_total1 > number_regions*10000 - votes_total1:
            print(f'Result: 1st candidate won with {votes_total1} votes and {round(votes_total1/(number_regions*100), 1)}% of all votes')
        elif votes_total1 < number_regions*10000 - votes_total1:
            print(f'Result: 2nd candidate won with {number_regions*10000 - votes_total1} votes and {round(100 - votes_total1/(number_regions*100), 1)}% of all votes')
        else:
            print(f'Result: There\'s a draw, both candidates has the same result of {votes_total1} votes and 50% of all votes')
    
# Practice block 4

# 1. Create a tuple with your first name, last name, and age.
tuple_nameage = ('Anton', 'Morderer', 34)

# 2. Print your last name using indexing.
print(tuple_nameage[1])

# 3. Create three variables in one line that extracted from tuple that you created in step 1.
name, surname, age = tuple_nameage[0], tuple_nameage[1], tuple_nameage[2]

# 4. Print your name letter by letter from this tuple
for i in range(0,len(tuple_nameage[0])):
    print(tuple_nameage[0][i])

# 5. Create a new tuple that contains all info from the first tuple but remove first letter from all strings

tuple_wo_first = (tuple_nameage[0][1::], tuple_nameage[1][1::], tuple_nameage[2])
print(tuple_wo_first)

# 6. Create a tuple with two values. First one is (1, 2), second one is (3, 4).
tuple_two_values = (1,2), (3,4)

# 7. Create a program that calculates the sum of all values in the tuple and print it to the console.
def tuple_sum_values(*args) -> int:
    tuple_ = args
    sum_values = 0
    count_values = 0
    for i in range(0,len(tuple_)):
        if isinstance(tuple_[i], int) == True:
            sum_values += tuple_[i]
            count_values += 1
    return f'Sum of all integer values of the tuple is {sum_values}' if count_values > 0 else\
    f'There are no integer values in the tuple'

tuple_sum_values(1,-2,'adf',4)



