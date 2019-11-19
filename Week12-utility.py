# https://github.com/Me7is/Week12-utility
# Sean Smith
# CSCI 102 - Section B
# Week 12 Part A

def PrintOutput (string):
    print("OUTPUT", string)

def LoadFile (file_name):
    file = open(file_name, 'r').read()
    line_list = file.splitlines()
    return line_list

def UpdateString (string_1, string_2, index):
    string_1_list = list(string_1)
    string_1_list[index] = string_2
    PrintOutput("".join(string_1_list))

def FindWordCount (list, string):
    count = 0
    for i in range(len(list)):
        if string == list[i]:
            count += 1
    return count

def ScoreFinder (list_1, list_2, string):
    exist = False
    for i in range(len(list_1)):
        if list_1[i].lower() == string.lower():
            print("OUTPUT", list_1[i], "got a score of", list_2[i])
            exist = True
            break
    if not exist:
        print("OUTPUT player not found")

def Union (list_1, list_2):
    exist = False
    for i in range(len(list_1)):
        for x in range(len(list_2)):
            if list_1[i] == list_2[x]:
                exist = True
        if not exist:
            list_2.append(list_1[i])
        exist = False
    return list_2

def Intersection (list_1, list_2):
    list_3 = []
    for i in range(len(list_1)):
        for x in range(len(list_2)):
            if list_1[i] == list_2[x]:
                list_3.append(list_1[i])
                break
    return list_3

def NotIn (list_1, list_2):
    exist = False
    list_3 = []
    for i in range(len(list_1)):
        for x in range(len(list_2)):
            if list_1[i] == list_2[x]:
                exist = True
        if exist == False:
            list_3.append(list_1[i])
        exist = False
    return list_3
