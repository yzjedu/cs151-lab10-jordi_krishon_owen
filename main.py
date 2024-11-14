
# Import os package into the code
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

def read_file(file_name):
    movie_table = []
    try:
        file = open(file_name, "r")
        for line in file:
            row = line.split()
            row[3] = int(row[3])
            row[4] = int(row[4])
            row[5] = int(row[5])
            for i in range(len(line)):
                if row[i].isdigit():
                    movie_table.append(row)
                return movie_table
    except FileNotFoundError:
        print("File not found.")
        return

def main():
    file_name = read_file_name()
    read_file(file_name)

    return

main()
