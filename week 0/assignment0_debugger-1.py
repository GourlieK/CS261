# Name: Kyle Gourlie
# OSU Email: GourlieK@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 0: debugger
# Due Date: 10/07/2003
# Description: This script contains a function that takes a list as an input and returns the length of the list

# Please enter your name, favorite color, favorite hobby, and hometown in the list
my_list = ['Kyle Gourlie', 'Blue', 'Hiking', 'Scio']

def my_info(my_list):
    """ A function that passes a list of my information """
    count = 0
    for value in my_list:
        count += 1
    return count


if __name__ == '__main__':
    print(my_info(my_list))

