"""
https://app.codingrooms.com/management/assignments/365244/overview
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

"""
filtering even numbers
"""
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.
"""

with open("./files/file1.txt") as f1:
    f1_numbers = [int(n) for n in f1.readlines()]

with open("./files/file2.txt") as f2:
    f2_numbers = [int(n) for n in f2.readlines()]

slice_list = [n for n in f1_numbers if n in f2_numbers]
print(slice_list)