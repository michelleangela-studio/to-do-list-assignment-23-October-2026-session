
"""
Terminal-Based TodoList Program

This program displays a menu that allows users to:
1. View tasks
2. Add tasks
3. Edit tasks
4. Delete tasks
5. Exit the program
"""


def display_menu():
    """
    Display the available TodoList menu options.
    """

    print("\n===== TODO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    """
    Main function that controls the TodoList program.
    It repeatedly displays the menu until the user exits.
    """

    while True:
        """
        Display the menu and ask the user to select an option.
        """

        display_menu()

        choice = input("Enter your choice: ")

        """
        Check the user's choice and perform the
        corresponding operation.
        """

        if choice == "1":
            print("View Tasks selected")

        elif choice == "2":
            print("Add Task selected")

        elif choice == "3":
            print("Edit Task selected")

        elif choice == "4":
            print("Delete Task selected")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


"""
Check whether this file is executed directly.
If it is, start the program by calling main().
"""

if __name__ == "__main__":
    main()
