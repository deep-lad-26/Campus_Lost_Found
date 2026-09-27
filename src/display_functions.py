from file_functions import read_items


def display_one_item(item):

    print("\n------------------------------")
    print("ID          :", item["ID"])
    print("Name        :", item["Name"])
    print("Category    :", item["Category"])
    print("Location    :", item["Location"])
    print("Date        :", item["Date"])
    print("Description :", item["Description"])
    print("Contact     :", item["Contact"])
    print("Status      :", item["Status"])
    print("------------------------------")


def view_items(item_type):

    items = read_items(item_type)

    print("\n================================")
    print(item_type.upper(), "ITEMS")
    print("================================")

    if len(items) == 0:
        print("No items found.")
        return

    for item in items:
        display_one_item(item)

    print("Total records:", len(items))