## Practice

# 1. Write a Python program to compute the difference between two lists.

''' Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']

    Expected Output:

    first-second: ['a', 'b']

    second-first: ['e']'''

def compute_difference(first: list, second: list) -> tuple:
    for i in first:
        for j in second:
            if i == j:
                first.remove(i)
                second.remove(j)
                break
        print(i, first, second)
    return first, second

print(compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e']))

assert compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e']) == (['a', 'b', 'c'], ['e'])
assert compute_difference([], ['c', 'd', 'e']) == ([], ['c', 'd', 'e'])
assert compute_difference([1, 2, 3], [4, 5, 6]) == ([1, 2, 3], [4, 5, 6])
assert compute_difference([1, 2, 3], [2, 3, 4]) == ([1], [4])


# 2. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
'''
**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]'''

def sum_of_two(arr: list, target: int) -> list:
    result = []
    for i in range(0, len(arr)-1):
        if result == []: # умова зупинки циклу після знайдення першого рішення
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == target:
                    result.append(i)
                    result.append(j)
                    break
    return result if result != [] else  f'Рішення немає'

assert sum_of_two([1, 2, 3, 6, 5, 7], 4) == [0, 2]
assert sum_of_two([6,5,7], 6) == 'Рішення немає'
assert sum_of_two([], 0) == 'Рішення немає'
assert sum_of_two([0], 0) == 'Рішення немає'
assert sum_of_two([2,-2, 3, -3], 0) == [0, 1]
assert sum_of_two([2, 7, 11, 15], 9) == [0, 1]
assert sum_of_two([3,2,4], 6) == [1, 2]
assert sum_of_two([3,3], 6) == [0, 1]

# 3. Write a program that takes a list of integers as input and returns a new list that contains only the elements that are unique
#  (i.e., that appear only once in the list). For example, if the input list is [1, 2, 3, 2, 4, 5, 5],
#  the output list should be [1, 3, 4]. You can not use set data structure. It`s also forbidden to use the count method.

def unique_elements(arr: list) -> list:
    for i in arr:
        counter = 0
        for j in arr[arr.index(i)+1:len(arr)]:
            if i == j:
                arr.remove(j)
                counter += 1
        if counter > 0:
            arr.remove(i)
    return arr

assert unique_elements([1, 1, 2, 2]) == []
assert unique_elements([1]) == [1]
assert unique_elements([1, 2, 5, 3, 1, 6, 5]) == [2, 3, 6]
assert unique_elements([1, 1, 1]) == []

# 4. Write a program that takes a list of integers as input and returns a new list that contains only the elements that appear an odd number of times in the list.
# For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list should be [1, 3, 4].

def odd_elements(arr: list) -> list:
    for i in arr:
        counter = 0
        for j in arr[arr.index(i)+1:len(arr)]:
            if i == j:
                arr.remove(j)
                counter += 1
        if counter % 2 != 0:
            arr.remove(i)
    return arr

assert odd_elements([1, 1, 2, 2]) == []
assert odd_elements([1, 2, 3, 2, 4, 5, 5]) == [1, 3, 4]
assert odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6]) == [1, 3, 4, 6]

# 5. Write a program that takes a list of integers as input and returns the second-largest element in the list.
#  If the list has fewer than two elements, the program should return None.
#  For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the program should return 5.

def second_largest_element(arr: list) -> int:
    if arr != []:
        arr.remove(max(arr))
    return max(arr) if arr != [] else None

assert second_largest_element([1, 2, 3, 2, 4, 5, 5]) == 5
assert second_largest_element([1, 2, 3, 4, 5]) == 4
assert second_largest_element([1, 1, 1, 1, 1]) == 1
assert second_largest_element([]) == None
assert second_largest_element([0]) == None

# 6. Optional (hard): Longest Increasing Sequence
# Have the function longest_increasing_sequence take the list of positive integers and return the length of the longest increasing subsequence (LIS).
#  A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order.
#  The sequence does not need to be contiguous or unique, and there can be several different subsequences.
#  For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6].
#  For this input, your program should return 3 because that is the length of the longest increasing subsequence.

'''Examples
Input: [9, 9, 4, 2]
Output: 1
Input: [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
Output: 7'''

def longest_increasing_sequence(arr: list) -> int:
    lenght_seq = 1 if arr != [] else 0
    arr_seq = []
    for i in range(0, len(arr)-1):
        counter = 1
        max_value = arr[i]
        for j in range(i+1, len(arr)):
            if max_value < arr[j]:
                counter += 1
            max_value = arr[j]
        arr_seq.append(counter)
    return max(arr_seq) if arr_seq != [] else lenght_seq

assert longest_increasing_sequence([]) == 0
assert longest_increasing_sequence([1]) == 1
assert longest_increasing_sequence([9, 9, 4, 2]) == 1
assert longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]) == 7
assert longest_increasing_sequence([4, 3, 5, 1, 6]) == 3
assert longest_increasing_sequence([4, 3, 4, 5, 1, 6]) == 4

# 7. Sort the following list by population. Calculate average and total population for cities from this list:
'''[
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]
'''

city_population = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]
def sec_element(list_: list) -> int:
    return(list_[1])

city_population.sort(key = sec_element)

number_cities = 0
population_total = 0
for i in city_population:
    population_total += i[1]
    number_cities += 1

print(city_population)
print(f'Average popolation: {population_total/number_cities}\nTotal population: {population_total}')