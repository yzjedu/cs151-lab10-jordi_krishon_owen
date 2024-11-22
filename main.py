# Programmers:  [Krishon, Jordi, Owen]
# Course:  CS151, [Professor Zee]
# Due Date: [11/21/2024]
# Lab Assignment:  [LAB 10]
# Problem Statement:  [Our program analyze data on movies, their budgets, and their profits]
# Data In: [name of a file of this format and the name of an output file]
# Data Out:  [movie information]
# Credits: [class notes and class program]
# Input Files: [the input file 'read_file_name' asks user to input the file name and checks to see it is exists before proceeding]

# Import os module
import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

# Name: read_file
# Parameters: file_name
# Return: headline_list
# Stores data from user-inputted file name into list
def read_file(file_name):
    movie_table = []
    try:
        # Open file name with read permissions
        file = open(file_name, "r")
        # For each line in file, split line by commas and store split line in list
        for line in file:
            row = line.split(',')
            movie_table.append(row)
        print(movie_table)
        return movie_table
    except FileNotFoundError:
        print("File not found.")
        return

# Name: main
# Parameters: [NONE]
# Return: [NONE]
# Runs main function
def main():
    file_name = read_file_name()
    read_file(file_name)

    return

main()
