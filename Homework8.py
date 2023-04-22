#Practice 1:
# 1. Create emtpy dictionary named en_ua_dictionary.
en_ua_dictionary = dict()

# 2. Add few key-value pairs to the dictionary. Example: 'red': 'червоний'
en_ua_dictionary['red'] = 'червоний'
en_ua_dictionary['green'] = 'зелений'
en_ua_dictionary['yellow'] = 'жовтий'

# 3. Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown.
for i in ('blue', 'purple'):
    if i not in en_ua_dictionary:
        en_ua_dictionary[i] = 'unknown'

# 4. Create a loop over existing values and print them to the console in the following format:
# Red in Ukrainian is червоний
for eng, ukr in en_ua_dictionary.items():
    print(f'{eng} in Ukrainian is {ukr}')

# 5. Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.
en_ua_dictionary['white'] = 'біл'
for i in list(en_ua_dictionary.keys()):
    if len(en_ua_dictionary[i]) < 5:
        en_ua_dictionary.pop(i)

# 6. Write a game where user should guess of a capital of the country that you have in your dictionary.
'''
capitals = { 'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 
'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 
'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen', 
'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens', ... }

You should show user a random country from the list and ask him to guess the capital. 
If user input right capital, print "You are right!", add him a point and ask him to guess another country. 
If not, you should ask again. User should be able to quit the game by typing "exit". 
You should print current score after each round. Also, you should print the final score before user quit the game.

Optional:
A. Give user a hint if he guesses wrong. Hint should looks like first letter of the capital. 
If you user make another mistake, you should print one more letter from the capital.

B. If user make a mistake you should decrement his lives. Initial amount of lives is 3. 
Game will end when user has no lives left. You should print the final score after user has no lives left.
'''
import random as rd
capitals = { 'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 
'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 
'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen', 
'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}
keylist = [i for i in capitals.keys()]
points = 0
lives = 3
while True:
    country = keylist[rd.randint(0,len(keylist)-1)]
    hint = 0
    while True:
        answer = input(f'What is a capital of {country} ').capitalize()
        if answer.lower() == 'exit':
            break
        if answer == capitals[country]:
            print("You are right!")
            points += 1
            break
        else: 
            lives -= 1
            hint += 1
            print(f'You\'ve got {lives} lives left')
            print(f'Small hint: it starts from {capitals[country][0 : hint]}')
            if lives == 0: 
                break
    if answer.lower() == 'exit':
            break
    if lives == 0: 
        print('Game over')       
        break
    else:
        print(f"Your current score is {points} points")
print(f"Your final score is {points} points")

'''
Optional

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
'''
def roman_to_int(s: str) -> int:
    '''
    Converts roman number into arabic number

    Args:
    s(int): roman number to convert into arabic number
    
    Returns:
    int: arabic number, if the input was correct. Otherwise - text message "Wrong roman number"
    '''
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    possible_values = (4, 9, 40, 90, 400, 900)
    impossible_values = (4, 40, 400)
    romnum = s.upper()
    count_I = 0 
    count_V = 0
    count_X = 0 
    count_L = 0 
    count_C = 0
    count_D = 0
    count_else = 0
    for j in romnum:
        match j:
            case 'I': count_I += 1
            case 'V': count_V += 1
            case 'X': count_X += 1
            case 'L': count_L += 1
            case 'C': count_C += 1
            case 'D': count_D += 1
            case 'M': continue
            case _: count_else += 1
    if count_I > 3 or count_V > 1 or count_X > 4 or count_L > 1 or count_C > 4 or count_D > 1 or count_else > 0 \
    or 'XXXX' in romnum or 'CCCC' in romnum:
        print('Wrong roman number')
    else:
        arabnum = 0
        arablist = [roman[i] for i in romnum]
        for i in range(len(romnum)):
            if i == len(romnum) - 1:
                arabnum += arablist[i]
            elif arablist[i] >= arablist[i+1]:
                arabnum += arablist[i]
            elif arablist[i+1] - arablist[i] in possible_values and \
                (i == 0 or arablist[i-1] > arablist[i] and arablist[i-1] - arablist[i] not in impossible_values):
                if i + 1 == len(romnum) - 1 or arablist[i] > arablist[i+2]:
                    arabnum -= arablist[i] 
                else:
                    print('Wrong roman number')
                    break
            else:
                print('Wrong roman number')
                break
        return arabnum if i == len(romnum) - 1 else None
    
assert roman_to_int('IX') == 9
assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994

# Optional
# Try to create a function that will do reverse operation - from integer to roman

def int_to_roman(s: int) -> str:
    '''
    Converts Arabic number into Roman number

    Parameters:
    ----------
        s:  int
            the arabic number to convert into roman number

    Returns:
    -------
    str:    roman number 
    '''
    integers = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    arablist = [i for i in integers.keys()]
    roman = ''
    for i in arablist[::-1]:
        while s >= i:
            roman += integers[i]
            s -= i
    return roman

assert int_to_roman(9) == 'IX'
assert int_to_roman(3) == 'III'
assert int_to_roman(58) == 'LVIII'
assert int_to_roman(1994) == 'MCMXCIV'

# Optional
# Write an algorithm to determine if a number n is happy.
'''
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''

def is_happy(n: int) -> bool:
    '''
    Checks if the number is a happy number

    Parameters:
    ----------
        n:  int
            the number to check if it is happy
    Returns:
    -------
    bool:    "True" if the number is happy. Otherwise "False"
    '''
    numbers_list = []
    str_num = None
    num = n
    result = True
    while 1 not in numbers_list:
        str_num = str(num)
        num = 0
        for i in str_num:
            num += int(i) ** 2
        if num in numbers_list:
            result = False
            break
        else:
            numbers_list.append(num)   
    return result

assert is_happy(19) == True
assert is_happy(2) == False
