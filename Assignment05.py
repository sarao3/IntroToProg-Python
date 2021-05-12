# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# SaraONeal,05.08.2021,Created script file
# SaraONeal,05.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None  # file handle
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

print("Load data from ToDoList text file into python list of dictionary rows: \n")
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # split() returns a list object
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
    print(lstTable)  # List with dictionary objects
objFile.close()

# -- Input/Output -- #
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
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here

        print('Your current data is: ')
        for row in lstTable:
            print('', row["Task"], ',', row["Priority"],sep='')
        ## print(lstTable)  # List with dictionary objects
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here

        while(True):
            strTask = input("Task: ")
            strPriority = input("Priority: ")
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        print(lstTable)  # List with dictionary objects
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here

        while(True):
            strTask = input("Item to Remove: ")
            for row in lstTable:
                if row["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("row removed")
                    print(lstTable)  # List with Dictionary objects
                else:
                    print("row not found")
                    print(lstTable)  # List with Dictionary objects
            strChoice = input("Exit? ('y/n'): ")
            if strChoice.lower() == 'y':
                break
        print(lstTable)  # List with dictionary objects
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        print("Would you like to save your data?")
        strOption = str(input("Enter 'y' or 'n': "))
        if (strOption.lower() == 'y'):
            objFile = open(strFile, "w")
            for row in lstTable:
                objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
            objFile.close()
            print("Now in file!")
        else:
            print("Changes were not saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Would you like to exit the program?")
        strExit = str(input("Enter 'y' or 'n': "))
        if (strExit.lower() == 'y'):
            break  # and Exit the program
        else:
            print('Please choose only 1, 2, 3, 4, or 5!')
    else:
        print('Please choose only 1, 2, 3, 4, or 5!')