import array as arr
import string
import sys
import time
from random import randint

import psutil as psutil


def twoA():
    input_list = []
    for i in range(10):
        input_number = int(input("Enter A Number: "))
        input_list.append(input_number)
    print([number ** 2 for number in input_list])


# twoA()

def twoB():
    with open("problem_set_5_integers.txt") as file:
        with open("new_problem_set_5_integers.txt", "w+") as new_file:
            for line in file:
                new_file.write(str(int(line) ** 2) + "\n")


# twoB()

def twoC():
    names_list = []
    with open("problem_set_5_names.txt") as file:
        for name in file.readlines():
            names_list.append(name.split("\n")[0])
    for index, name in enumerate(names_list):
        if name.startswith("a"):
            print(f"Index of {name}: {index}")


# twoC()

def twoD():
    t = time.process_time()
    my_list = [i for i in range(1000001)]
    total = 0
    for i in my_list:
        total += i

    print("Using List")
    print(f"Sum: {total}")
    print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024)}MB")
    print(f"Time: {time.process_time() - t}s")


# twoD()

def twoE():
    matrix = []
    for row in range(4):
        row = []
        for column in range(5):
            input_value = int(input("Enter A Number: "))
            row.append(input_value)
        matrix.append(row)

    print(matrix)

    for row in matrix:
        for index, value in enumerate(row):
            if value < 0:
                row[index] = 0

    print(matrix)


# twoE()


def join(list_one, list_two):
    new_list = []
    for index, value in enumerate(list_one):
        list_two_value = list_two[index]
        new_list.append([value, list_two_value])
    return new_list


def twoF():
    print(join([1, 2, 3], ["a", "b", "c"]))


# twoF()

def split(nested_list):
    list_one = []
    list_two = []
    for list in nested_list:
        list_one.append(list[0])
        list_two.append(list[1])
    return list_one, list_two


def twoG():
    print(split([[1, 'a'], [2, 'b'], [3, 'c']]))


# twoG()


def threeA():
    my_array = arr.array('i', range(1000001))
    t = time.process_time()
    total = 0
    for i in my_array:
        total += i

    print("\nUsing Arrays")
    print(f"Sum: {total}")
    print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024)}MB")
    print(f"Time: {time.process_time() - t}s")


def fourA():
    # Using Arrays resulted in less computation time and less usage of memory overall
    twoD()
    threeA()


# fourA()

def fiveA_list():
    # Lists
    t = time.process_time()
    student_list = [i for i in range(1001)]
    student_averages = []

    for student_id in student_list:
        student_grade = round((randint(0, 100) + randint(0, 100) + randint(0, 100)) / 3, 2)
        student_averages.append((student_id, student_grade))

    print(student_averages)
    print("Using List")
    print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024)}MB")
    print(f"Size of List: {sys.getsizeof(student_list)}")
    print(f"Time: {time.process_time() - t}s")


# fiveA_list()


def fiveA_dict():
    # Dictionaries
    t = time.process_time()
    student_list = [i for i in range(1001)]
    student_dict = {}

    for student_id in student_list:
        student_grade = round((randint(0, 100) + randint(0, 100) + randint(0, 100)) / 3, 2)
        student_dict[student_id] = student_grade

    print(student_dict)
    print("Using Dictionaries")
    print(f"Size of Dictionary: {sys.getsizeof(student_dict)} Bytes")
    print(f"Memory: {psutil.Process().memory_info().rss / (1024 * 1024)}MB")
    print(f"Time: {time.process_time() - t}s")


# fiveA_dict()


def word_freq():
    words_dict = {}
    input_words = input("Enter A Sentence: ")
    split_words = input_words.split()

    for word in split_words:
        new_word = []
        for char in word:
            if char in string.ascii_letters:
                new_word.append(char)
        new_word_string = "".join(new_word).lower()

        if new_word_string in words_dict:
            words_dict[new_word_string] = words_dict.get(new_word_string) + 1
        else:
            words_dict[new_word_string] = 1

    return words_dict


def sixA():
    print(word_freq())


# sixA()
