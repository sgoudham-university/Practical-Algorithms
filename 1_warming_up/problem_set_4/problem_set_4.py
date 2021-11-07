import random as rand

import time


# Sequential Operations
def oneA():
    before_tax_price = float(input("Before Tax Price: "))
    discount_offered = float(input("Discount Offered: "))

    discount_price = before_tax_price * ((100 - discount_offered) / 100)
    final_price = discount_price * 1.175

    print(f"Final Price: £{final_price:.2f}")


# oneA()


def oneB():
    last_name = input("Enter Your Last Name: ").lower()
    last_name_sliced = last_name[0:3]
    three_digit_num = rand.randint(100, 999)

    print(f"Character ID: {last_name_sliced}{three_digit_num}")


# oneB()

# Conditional Operations
def twoA():
    number_one = int(input("Enter First Number: "))
    number_two = int(input("Enter Second Number: "))

    if number_one % number_two == 0 or number_two % number_one == 0:
        print(True)
    else:
        print(False)


# twoA()

def twoB():
    hours = float(input("Enter Hours: "))
    hourly_rate = float(input("Enter Hourly Rate: "))

    gross_pay = 0
    if 0 < hours <= 40:
        gross_pay = hours * hourly_rate
    elif hours > 40:
        gross_pay = 40 * hourly_rate + ((hours - 40) * hourly_rate * 1.5)

    print(f"Gross Pay: £{gross_pay:.2f}")


# twoB()

def twoC():
    month_number = int(input("Enter A Number: "))

    if month_number == 3 or month_number == 4:
        return "Spring"
    elif month_number == 5 or month_number == 6 or month_number == 7 or month_number == 8:
        return "Summer"
    elif month_number == 9 or month_number == 10:
        return "Autumn"
    elif month_number == 11 or month_number == 12 or month_number == 1 or month_number == 2:
        return "Winter"


# print(twoC())

def three():
    number = input("Enter A 5 Digit Number: ")
    if not number.isdigit() or len(number) != 5:
        print("Not Suitable Number")
        return

    return number == number[::-1]


# print(three())

# Iterative Operations
def fourA():
    n = int(input("Enter The Number of Iterations: "))
    sum = 0
    i = 0

    while i < n:
        number = int(input("Enter A Number: "))
        sum += number
        i = i + 1

    print(f"Total Sum: {sum}")


# fourA()

def fourB():
    n = int(input("Enter The Number of Iterations: "))
    sum = 0

    for i in range(n):
        number = int(input("Enter A Number: "))
        sum += number

    print(f"Total Sum: {sum}")


# fourB()

def fourC():
    first_input = int(input("Enter Number: "))
    all_numbers = []

    while first_input != 0:
        new_input = int(input("Enter Number: "))
        if new_input == 0:
            break
        all_numbers.append(new_input)
        first_input = new_input

    print(f"Mean: {sum(all_numbers) / len(all_numbers)}")


# fourC()

def fourE():
    sum = 0
    while True:
        user_input = int(input("Enter A Number NOW: "))
        if sum + user_input >= 1000:
            print("Sum Exceeded 1000!")
            break
        print(f"Current Sum: {sum}")
        sum += user_input
        print(f"New Sum: {sum}")


# fourE()

def fiveA():
    t = time.process_time()
    sum = 0
    for number in range(10000001):
        sum += number
    print(sum)
    print(time.process_time() - t)


# fiveA()

def fiveB():
    t = time.process_time()
    sum = 0
    i = 0
    while i <= 10000000:
        sum += i
        i += 1
    print(sum)
    print(time.process_time() - t)


# fiveB()

def fiveC():
    t = time.process_time()
    # sum = n(n + 1) / 2
    sum = (10000000 * (10000000 + 1)) / 2
    print(sum)
    print(time.process_time() - t)


def fiveD():
    t = time.process_time()
    sum = 0
    for number in range(20000001):
        sum += number
    print(sum)
    print(time.process_time() - t)

    t = time.process_time()
    sum = 0
    i = 0
    while i <= 20000000:
        sum += i
        i += 1
    print(sum)
    print(time.process_time() - t)

    t = time.process_time()
    # sum = n(n + 1) / 2
    sum = (20000000 * (20000000 + 1)) / 2
    print(sum)
    print(time.process_time() - t)


fiveD()
