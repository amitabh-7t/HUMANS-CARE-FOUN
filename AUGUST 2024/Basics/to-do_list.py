"""
problem statement:- Write a Python program to create a simple To Do List Manager. 
The program should have the following features:
1. Add an item to the To Do List
2. Delete an item from the To Do List
3. Print the To Do List
4. Exit
The program should display a menu with options to the user. 
The program should keep running until the user selects the Exit option.

"""

print("To Do List Manager")
to_do_list = [] # list to store the items
flag = True # flag to keep the program running
while flag:
    print("1. Add an item to the To Do List")
    print("2. Delete an item from the To Do List")
    print("3. Print the To Do List")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to add: ")
        to_do_list.append(item)# adding the item to the list
    elif choice == 2:
        item = input("Enter the item to delete: ")
        if item in to_do_list:
            to_do_list.remove(item)# removing the item from the list
        else:
            print("Item not found")
    elif choice == 3:
        print("To Do List:")
        for i in range(len(to_do_list)):
            print(f"{i + 1}. {to_do_list[i]}")
    elif choice == 4:
        flag = False # exiting the program
    else:
        print("Invalid choice")