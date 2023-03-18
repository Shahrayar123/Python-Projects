""" The sys module helps us to exit the program. """
import sys


def main():
    """ This functin lets the user to create or delete a todo. """
    user_choice = input("Type 'C' to create a todo, 'D' to delete: ").upper()
    if user_choice == 'C':
        create_todo()
    elif user_choice == 'D':
        delete_todo()
    else:
        print("Invalid Input")


def create_todo():
    """ This function creates a todo for the user """
    user_input = input("Write your Todo here: ").title()
    with open('todolist.txt', 'a') as file: # pylint: disable= unspecified-encoding
        file.write(user_input)
        print("Creation Successful")


def delete_todo():
    """ This function deletes the todo of the user """
    user_input = input("Are you sure you want to delete your todo\
Type 'yes' or 'no' : ").lower()
    if user_input == 'yes':
        with open('todolist.txt') as file: # pylint: disable= unspecified-encoding
            file_list = file.readlines()
            user_index = int(input("Which one you want to delete enter a number: "))
            del file_list[user_index - 1]
            new_file_list = ''.join(file_list)
            with open('todolist.txt', 'w') as new_file: # pylint: disable= unspecified-encoding
                new_file.write(new_file_list)
                print("Deletion Successful")
    elif user_input == 'no':
        sys.exit(1)


if __name__ == '__main__':
    main()
