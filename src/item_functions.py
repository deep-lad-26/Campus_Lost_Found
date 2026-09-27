from file_functions import (
    read_items,
    save_items,
    generate_id
)

from validation import (
    get_non_empty,
    get_phone_number,
    get_category
)


def add_item(item_type):

    print("\n------------------------------")
    print("Report", item_type, "Item")
    print("------------------------------")

    item_id = generate_id(item_type)

    name = get_non_empty("Enter item name: ")

    category = get_category()

    location = get_non_empty(
        "Enter location where item was lost/found: "
    )

    date = get_non_empty(
        "Enter date (DD-MM-YYYY): "
    )

    description = get_non_empty(
        "Enter item description: "
    )

    contact = get_phone_number()

    item = {
        "ID": item_id,
        "Name": name,
        "Category": category,
        "Location": location,
        "Date": date,
        "Description": description,
        "Contact": contact,
        "Status": item_type
    }

    items = read_items(item_type)

    items.append(item)

    save_items(item_type, items)

    print("\nItem successfully added.")
    print("Your Item ID is:", item_id)


def update_status():
    print("\n1. Update Lost Item")
    print("2. Update Found Item")

    choice = input("Enter choice: ")

    if choice == "1":
        item_type = "Lost"

    elif choice == "2":
        item_type = "Found"

    else:
        print("Invalid choice.")
        return

    items = read_items(item_type)

    if len(items) == 0:
        print("No records available.")
        return

    try:
        item_id = int(
            input("Enter item ID: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    found = False

    for item in items:

        if int(item["ID"]) == item_id:

            print("\nCurrent status:", item["Status"])

            new_status = get_non_empty(
                "Enter new status: "
            )

            item["Status"] = new_status

            found = True
            break

    if found:
        save_items(item_type, items)
        print("Status updated successfully.")

    else:
        print("Item ID not found.")


def delete_item():

    print("\n1. Delete Lost Item")
    print("2. Delete Found Item")

    choice = input("Enter choice: ")

    if choice == "1":
        item_type = "Lost"

    elif choice == "2":
        item_type = "Found"

    else:
        print("Invalid choice.")
        return

    items = read_items(item_type)

    try:
        item_id = int(
            input("Enter item ID to delete: ")
        )
    except ValueError:
        print("Invalid ID.")
        return

    new_items = []
    found = False

    for item in items:

        if int(item["ID"]) == item_id:
            found = True
        else:
            new_items.append(item)

    if found:
        save_items(item_type, new_items)
        print("Item deleted successfully.")

    else:
        print("Item ID not found.")