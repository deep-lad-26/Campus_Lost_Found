from item_functions import add_item
from display_functions import view_items
from search_functions import search_items
from match_functions import find_matches
from item_functions import update_status, delete_item


def main_menu():
    while True:
        print("\n======================================")
        print("       CAMPUS LOST & FOUND SYSTEM")
        print("======================================")
        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search Items")
        print("6. Find Possible Matches")
        print("7. Update Item Status")
        print("8. Delete Item")
        print("9. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item("Lost")

        elif choice == "2":
            add_item("Found")

        elif choice == "3":
            view_items("Lost")

        elif choice == "4":
            view_items("Found")

        elif choice == "5":
            search_items()

        elif choice == "6":
            find_matches()

        elif choice == "7":
            update_status()

        elif choice == "8":
            delete_item()

        elif choice == "9":
            print("\nThank you for using Campus Lost & Found.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


main_menu()