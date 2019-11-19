# Sean Smith
# CSCI 102 - Section B
# Week 12 Part A

def PrintOutput (string):
    print("OUTPUT", string)

def LoadFile (file_name):
    file = open(file_name, 'r').read()
    line_list = file.splitlines()
    return line_list
