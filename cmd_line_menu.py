"""
 * Francis Bui
 * SDEV 300
 * Professor Chris Howard
 * Lab 2 - Python Command-Line Menu with Math and Security Related Functions
 * August 27, 2020
 * The purpose of this program is to design a menu system using the command-line interface
 * The application will have various sets of menu option application that will perform a
 * variety of mathematics and security related functions. The menu will loop back after each
 * operation until the user exits. At that point, a function will execute that will thank
 * the user for participating and the application will exit.
"""

import secrets
import string
import decimal
import datetime
import math
import sys


def main_menu():
    """
    Main Menu function
    Executes first and after every function excepts when the user exits
    :return:
    """
    print('\n\ta. Generate Secure Password')
    print('\tb. Calculate and Format a Percentage')
    print('\tc. How many days from today until July 4, 2025?')
    print('\td. Use the Law of Cosines to calculate the leg of a triangle')
    print('\te. Calculate the volume of a Right Circular Cylinder')
    print('\tf. Exit Program\n')

    user_input = input().lower()
    if user_input == 'a':
        gen_pass()
    elif user_input == 'b':
        for_percent()
    elif user_input == 'c':
        july_forth()
    elif user_input == 'd':
        cos_law()
    elif user_input == 'e':
        right_cylinder()
    elif user_input == 'f':
        exit_program()
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        main_menu()


def gen_pass():
    """
    a. Generating a Secure Password
    # incomplete...
    :return:
    """
    pass_choice = string.ascii_lowercase
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    mixed_case = string.ascii_letters
    mixed_numb = string.ascii_letters + string.digits
    mixed_char = string.ascii_letters + string.digits + string.punctuation

    print('\tg. Use Lower Case in password')
    print('\th. Use Upper Case in password')
    print('\ti. Use Mixed Case in password')
    print('\tj. Use Mixed Case and Numbers in password')
    print('\tk. Use Mixed Case, Number and Special Character in password')

    user_input = input().lower()
    if user_input == 'g':
        pass_choice = lower_case
    elif user_input == 'h':
        pass_choice = upper_case
    elif user_input == 'i':
        pass_choice = mixed_case
    elif user_input == 'j':
        pass_choice = mixed_numb
    elif user_input == 'k':
        pass_choice = mixed_char
    else:
        print('Please enter a valid letter that corresponds to the menu item\n')
        gen_pass()

    pass_length = int(input('Length desired for password? Please enter a whole number\n'))

    password = ''.join(secrets.choice(pass_choice) for i in range(pass_length))
    print('Below is your newly generated password')
    print(password)
    main_menu()


def for_percent():
    """
    b. Calculate and Format Percentage
    Uses the decimal library for a precise percentage
    :return:
    """
    numerator = decimal.Decimal(input('Enter the numerator: \n'))
    denominator = decimal.Decimal(input('Enter the denominator: \n'))
    decimal_places = int(input('Enter how many decimal places formatting: \n'))
    percentage = (numerator/denominator)
    print(str((round((decimal.Decimal(100.00) * percentage), decimal_places))) + '%')
    main_menu()


def july_forth():
    """
    c. Calculates number of days until 4th of July 2025
    Uses the datetime library to determine the time from now until July 4th, 2025
    :return:
    """
    today = datetime.datetime.now()
    july_forth_2025 = datetime.datetime(2025, 7, 4, 0, 0, 0)
    days_left = july_forth_2025 - today
    print(days_left.days)
    main_menu()


def cos_law():
    """
    d. Calculates the Law of Cosines given side a, side b, and angle of c
    Uses the math function cosine and radian to calculate side c given side a, side b, and angle c
    :return:
    """
    si_a = float(input('What is the value of side \'a\'?\n'))
    si_b = float(input('What is the value of side \'b\'?\n'))
    deg_c = float(input('What is the degree of angle \'c\'?\n'))
    c_squared = ((si_a**2) + (si_b**2)) - ((2 * si_a) * si_b) * math.cos(math.radians(deg_c))
    print('The value of side \'c\' is:', math.sqrt(c_squared))
    main_menu()


def right_cylinder():
    """
    e. Calculates the volume of a right angle Circular Cylinder
    Uses the math function pi to calculate the volume given the user input for height and radius
    :return:
    """
    height = float(input('What is the height of the right circular cylinder?\n'))
    radius = float(input('What is the radius of the right circular cylinder?\n'))
    print('The volume of the cylinder is: ', ((math.pi * radius**2) * height))
    main_menu()


def exit_program():
    """
    e. Exits the application
    Thank the user and exits the system
    :return:
    """
    print('')
    print('{:*^80}'.format(''))
    print('{:^80}'.format(' Thank you for using the Command Line Menu Math and Secret Generation '))
    print('{:^80}'.format(' We hope you try it again very soon '))
    print('{:*^80}'.format(''))
    print('')
    sys.exit()


# Welcome message and program starts here
print('')
print('{:*^80}'.format(''))
print('{:^80}'.format(' Welcome to the '))
print('{:^80}'.format(' Command Line Menu Math and Secret Generation '))
print('{:*^80}'.format(''))
print('')

main_menu()
