#=====importing libraries===========
from datetime import date

#====Login Section====

#Imports and reads the file with user data
users = open('user.txt', 'r+')
open_file = users.read()
#Removes the commas and spaces and sets up a list with all usernames and passwords as individual items
no_spaces = open_file.replace(' ','')
data = no_spaces.replace('\n', ',')
entries = data.split(',')
#Sets the login check to False as default.
login = False

#Gets a username from the user. 
username = input("Enter your username: ")
while True:
    #Returns an error message if the username does not appear in the .txt file.
    #Also requires the username to be at an even index within the list, as otherwise passwords would count as valid usernames for the purpose of this check
    if (username not in entries) or (entries.index(username) % 2 != 0):
        username = input("Plese enter a valid username: ")
        continue

    else:
        #Checks to make sure the password is correct and belongs to that user.
        password = input("Enter your password:")
        for i in range(0, len(entries)):
            if ((i % 2 != 1) and (entries[i] == username)) and (entries[i + 1] == password):
                print("Login successful \n")
                login = True
                break 

            else:
                login = False
                #Loops back to the beginning if the password does not match the username.

    if login == False:
        username = input("Incorrect password. Please enter your username and try again")
        continue

    else:
        users.close()
        break
                
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Register a new user
a - Add a task
va - View all tasks
vm - View my tasks
vs - View task statistics
e - Exit\n
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Register a new user
a - Add a task
va - View all tasks
vm - View my tasks
e - Exit\n
: ''').lower()

#Section to register new users

    if menu == 'r':
        if username != "admin":
            print()
            print("You must be an admin to register new users")
            print()
        else:
            #Reopens the users file for writing to the end of the file
            users = open('user.txt', 'a+')
            #Gets the new username
            new_user = input("Please input the new username: ")
            while True:
                #Gets the user's password. If the two entered passwords do not match, the loop repeats again.
                new_pass = input("Please choose your password: ")
                confirm_pass = input("Please confirm your password: ")
                if new_pass != confirm_pass:
                    print("Error: Passwords do not match")
                    continue

                #If the passwords do match, the data is written to the .txt file and the user is returned to the menu.
                else:
                    users.write('\n' + new_user + ', ' + new_pass)
                    print(f"Thank you. A new user with the username '{new_user}' has been created.\n")
                    #Closes the users file to ensure the new data is written
                    users.close()
                    break

#Section to add new tasks

    elif menu == 'a':
        #Opens the task file in append mode
        tasks = open('tasks.txt', 'a+')

        responsible = input("Enter the person responsible for the new task: ")
        while True:
            #Checks whether the person being assigned the task is a user that currently exists. 
            if (responsible not in entries) or (entries.index(responsible) % 2 != 0):
                responsible = input("That person is not yet registered. Please assign the task to a registered user: ")
                continue
            else:
                break

        #Gets task info from the user
        task_title = input("Enter the title of the new task")
        task_description = input("Enter a description of the task")
        due_date = input("Enter the due date of the task")
        created_date = date.today()
        complete = "No"
        
        #Adds the task to the file on a new line
        tasks.write('\n' + f"{responsible}, {task_title}, {task_description}, {created_date}, {due_date}, {complete}")
        #Closes the file so the task is saved
        tasks.close()
        print("Thank you, your task has been added\n")

#Section to view all tasks

    elif menu == 'va':
        #Opens the tasks document in read only mode
        tasks = open('tasks.txt', 'r')
        for line in tasks:
            #Removes spaces to clean up readability
            line.replace(', ', ',')

            #Splits each line into a list and defines variables for each item based on index position
            task_data = line.split(',')
            responsible = task_data[0]
            task_title = task_data[1]
            task_description = task_data[2]
            created_date = task_data[3]
            due_date = task_data[4]
            #removes the new line character from the end of the completed line
            complete = task_data[5].replace('\n', '')

            #prints all of the variables with tab characters for optimal spacing
            print(f'''
Task:\t\t  {task_title}
Assigned to:\t   {responsible}
Date assigned:\t  {created_date}
Due date:\t  {due_date}
Task completed:\t  {complete}
Task description: {task_description}''')
        tasks.close()
        print()

#Section to view tasks for logged in user only

    elif menu == 'vm':
        tasks = open('tasks.txt', 'r')
        #Sets the outstanding tasks count to 0
        tasks_outstanding = 0
        for line in tasks:
            #Removes spaces to clean up readability
            line.replace(', ', ',')

            #Splits each line into a list and defines variables for each item based on index position
            task_data = line.split(',')
            responsible = task_data[0]
            task_title = task_data[1]
            task_description = task_data[2]
            created_date = task_data[3]
            due_date = task_data[4]
            #removes the new line character from the end of the completed line
            complete = task_data[5].replace('\n', '')
            
            #Checks if the logged in user is responsible and only prints their tasks
            if responsible == username:
            #prints all of the variables with tab characters for optimal spacing
                print(f'''
Task:\t         {task_title}
Assigned to:\t  {responsible}
Date assigned:\t {created_date}
Due date:\t {due_date}
Task completed:\t {complete}
Task description:{task_description}''')
                tasks_outstanding += 1

            #Shows that a user has no tasks assigned to them if they don't    
        if tasks_outstanding == 0:
            print()
            print("You have no tasks currently outstanding")
            print()
                
        else:
            pass
        tasks.close()

#Section for admin to view task statistics 
   
    elif menu == 'vs':
        users = open('user.txt', 'r')
        tasks = open('tasks.txt', 'r')
        user_numbers = 0
        task_numbers = 0

        for line in users:
            user_numbers += 1
        for line in tasks:
            task_numbers += 1
        
        print()
        print(f"There are {user_numbers} registered users and {task_numbers} logged tasks")
        print()
            
#Exit section and error message
  
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again")