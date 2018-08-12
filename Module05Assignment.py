# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRGraybeal
# Date:  August 11, 2018
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   RRGraybeal, August 11,2018, Added code to complete assignment 5
# https://www.tutorialspoint.com/python/python_dictionary.htm


# 1.	Create a text file called Todo.txt using the following data:
# Clean House,low
# Pay Bills,high
# 2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary.
# (The data will be stored like a row in a table.)
# Tip: You can use a for loop to read a single line of text from the file and then place the data
# into a new dictionary object.
# 3.	After you get the data in a Python dictionary, Add the new dictionary “row” into a Python
# list object (now the data will be managed as a table).
# 4.	Display the contents of the List to the user.
# 5.	Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
#     Menu of Options
#     1) Show current data
#     2) Add a new item.
#     3) Remove an existing item.
#     4) Save Data to File
#     5) Exit Program
# 6.	Save the data from the table into the Todo.txt file when the program exits.
# -------------------------------------------------#

# -- Data --#
# declare variables and constants

objFile = () #used to read and write to file
strNewTask = () #user input and key in dictionary
strPriority = () #user input and value in dictionary
strChoice = () #menu choice from user
dicToDo = {} #dictionary for Todo list
lstTable = [] # a list to hold the dictionary items


# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)


# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

with open("./ToDo.txt", "r") as objFile:
    for row in objFile:
        splitRow = row.strip().split(",")
        dicToDo[splitRow[0]] = ",".join(splitRow[1:])

# # 3.	After you get the data in a Python dictionary, Add the new dictionary “row”
# into a Python list object (now the data will be managed as a table).
for task, priority in dicToDo.items():
    row = (task, priority)
    lstTable.append(row)

# Step 2 - Display a menu of choices to the user
while (True):

    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

# Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):  # show current data
        print("Your ToDo List:\n")
        for task, priority in dicToDo.items(): #shows contents of dictionary
            print(task, ":", priority)
        continue

# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strNewTask = input("What task do you want me to add?:")
        strNewTask = strNewTask.lower()
        if strNewTask not in dicToDo:
            strPriority = input("What is the priority?:")
            dicToDo[strNewTask] = strPriority # add new task and priority to dictionary
            row = (strNewTask, strPriority)#add new task and priority to list
            lstTable.append(row) #append the new items to the Table
        else:
            print(strNewTask, "already exists. Try another")

# Step 5 - Remove a new item to the list/Table from book pg 145
    elif (strChoice == '3'):
        # try:
        strRemoveTask = input("What would you like to remove? ")
        strRemoveTask = strRemoveTask.lower()
        if strRemoveTask in dicToDo:
            del dicToDo[strRemoveTask]
            print("\n", strRemoveTask, "has been deleted.")
        else:
            print("\nSorry, I was unable to remove", strRemoveTask, "as it isn't yet on the list.")
        continue

# Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        with open("./ToDo.txt", "w") as objFile:
            for task, priority in dicToDo.items():
                objFile.write("%s:%s\n" % (task, priority))
        print("Your data has been saved. ")
        continue

# Step 7
# Exit program
    elif (strChoice == '5'):
        objFile.close()
        break  # and Exit the program

# -------------------------------

