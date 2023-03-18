# Practice chapter 1
"""Guess result of expression without executing it:

a) 1 <= 1   True

b) 1 != 1   False

c) 1 != 2   True

Make all of them true.

a) 3 __ 4   !=

b) 10 __ 5  !=

c) 42 __ "42"   != """

# Practise chapter 2
# 1. Print the text in which there will be a quote with double quotes.
print('"Hello world"')
# 2. Print the text in which there will be an apostrophe.
print("Hello World I'm Anton")
# 3. Print a line that will be displayed on several lines
print("Hello\nworld")
# 4. Print text that doesn`t fit in one line but will be displayed in one line
print(
    "This text doesn't feet \
in one line"
)

# Practise chapter 3
# 1. Create a variable with data type string. Count the length of this line.
string = "Line"
print(len(string))
# 2. Create another variable with string data type.
#    Output the result of concatenation of these two variables.
string1 = "age"
print(string + string1)
# 3. Print the two previous variables, but with a space between them.
print(string + " " + string1)
# 4. Get a string from user input. Check if the string is a palindrome.
polindrom = input("Введіть текст: ")
print(polindrom, polindrom[len(polindrom) :: -1])
print(polindrom == polindrom[len(polindrom) :: -1])
# 5. Replace age in the following string with your age.
# "I'm 10 years old" -> "I'm 30 years old". Do it with a) indexing and b) replace function.
age = int(input(print("Enter your age: ")))
string2 = "I'm 10 years old"
# a) indexing
print(string2[:4] + str(age) + string2[6:])
# b) replace
print(string2.replace("10", str(age)))

# Practice chapter 4
# 1. The program receive user's name and age from input.
Username = input("Enter your name: ")
Userage = int(input("Enter your age: "))
#    Then you need to display the name and age in one line in several ways:
#       a) by listing all the parameters in the print function
print("Your name is " + Username + " and you're " + str(Userage) + " years old")
#       b) by formatting a string using the format function
print("Your name is {0} and you're {1} years old".format(Username, Userage))
print(
    "Your name is {Username} and you're {Userage} years old".format(
        Username=Username, Userage=Userage
    )
)
#       c) by formatting a string with f-string
print(f"Your name is {Username} and you're {Userage} years old")

# Practice chapter 5
string_1 = "Animals  "
string_2 = "  Badger"
string_3 = "honey bee"
string_4 = "   HoneyPot   "
# 1. All letters must be written in lowercase.
print(string_1.lower(), string_2.lower(), string_3.lower(), string_4.lower(), sep="\n")
# 2. All letters must be capitalized.
print(string_1.upper(), string_2.upper(), string_3.upper(), string_4.upper(), sep="\n")
# 3. Remove all spaces:
#   a) from the beginning of the line
print(
    string_1.lstrip(), string_2.lstrip(), string_3.lstrip(), string_4.lstrip(), sep="\n"
)
#   b) from the end of the line
print(
    string_1.rstrip(), string_2.rstrip(), string_3.rstrip(), string_4.rstrip(), sep="\n"
)
#   c) on both sides of the line
print(string_1.strip(), string_2.strip(), string_3.strip(), string_4.strip(), sep="\n")
# 4. Check the value of the startwith ('be') function for each line:
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
print(
    string_1.startswith("be"),
    string_2.startswith("be"),
    string_3.startswith("be"),
    string_4.startswith("be"),
)
# Convert all rows with methods so that when using startwith ('be') it returns True.
print(
    string_1.lower().startswith("be"),
    string_2.lower().startswith("be"),
    string_3.lower().startswith("be"),
    string_4.lower().startswith("be"),
)
# 5. Find and replace all letters 's' with the letter 'x' in the following line:
# Somebody said something to Samantha.
string_5 = "Somebody said something to Samantha."
print(string_5.replace("s", "x"))
# у разі, якщо хочемо також змінити великі літери
print(string_5.replace("s", "x").replace("S", "X"))
# 6. Write a program that receives a phrase and letter from the user
# and returns "Yes!" if you find this letter in a line.
phrase = input(print("Enter your phrase: "))
letter = input(print("Enter your letter: "))
inline = letter in phrase
print(str(inline).replace("True", "Yes!").replace("False", ""))
# 7. Clean the following line with string methods:: '12345!,_6--'
line = "12345!,_6--"
print(line.rstrip("-").replace("!,_", ""))
# 8. At the input we get two numbers - the numerator and denominator of the fraction.
# Display the number as a percentage in the console.
# If the user entered 5 and 10, then you need to display: '50% '.
numerator = int(input(print("Введіть перше число: ")))
denominator = int(input(print("Введіть друге число: ")))
print("{:.0%}".format(numerator / denominator))
# 9. Find a secret message in the following text: 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'`
message = "X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX"
print(message.replace("X", "").replace("x", "")[::-1])
