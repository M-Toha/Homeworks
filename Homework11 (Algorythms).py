'''
### Practice

**You have 100 cats.**

One day you decide to arrange all your cats in a giant circle. 
Initially, none of your cats have any hats on. 
You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, 
or you take its hat off if it has one on.

1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. 
Code is simple here, but you might struggle with algorithm. 
Therefore don`t try to write a code from the first attempt. '''

'''Ідея:
Для довільного кола з номером 'n', ми відвідуємо котів, номери яких діляться без остачі на число n. 
Тож, якщо к-сть кіл дорівнює к-ті котів, нам фактично потрібно порахувати, скільки дільників має кожне число від 1 до 100 (враховуючи 1), 
при чому нас цікавить лише парність цієї кількості. Якщо число дільників для числа 'm' парне - на коті не буде капелюха, 
якщо непарне - буде. Буд-яке число k, що не є повним квадратом, має парну к-ть дільників (бо для кожного дільника p є дільник q = k/p).
Тож, нам фактично потрібно вивести список чисел, що є повними квадратами.
'''
def hats_on_cats(nr_rounds_and_cats: int) -> list:
    '''
    Calculates which cats from a circle of n cats are wearing hats 
    after walking n times around the circle following the rules:
        1. Initially, none of your cats have any hats on. You always start with the first cat
        2. The first round, you stop at every cat, placing a hat on each one.
        3. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
        4. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
        5. You continue this process until you’ve made n rounds around the cats (e.g., you only visit the nth cat).

    Parameters:
    ----------
        n:  int
            the  number of cats in a circle and number of circles to walk

    Returns:
    -------
    list:    a list of cat's numbers, who are wearing hats after n rounds
    '''
    i = 1
    list_of_numbers = list()
    while i ** 2 <= nr_rounds_and_cats:
        list_of_numbers.append(i ** 2)
        i += 1
    return list_of_numbers

assert hats_on_cats(100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


