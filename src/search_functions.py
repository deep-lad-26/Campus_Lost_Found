from file_functions import read_items
from display_functions import display_one_item


def search_by_name(items, keyword):

    results = []

    for item in items:

        if keyword.lower() in item["Name"].lower():
            results.append(item)

    return results


def search_by_category(items, keyword):

    results = []

    for item in items:

        if keyword.lower() == item["Category"].lower():
            results.append(item)

    return results


def search_by_location(items, keyword):

    results = []

    for item in items:

        if keyword.lower() in item["Location"].lower():
            results.append(item)

    return results


def search_items():

    print("\n==============================")
    print("SEARCH ITEMS")
    print("==============================")

    print("1. Search by Name")
    print("2. Search by Category")
    print("3. Search by Location")

    choice = input("Enter choice: ")

    keyword = input("Enter search value: ").strip()

    lost_items = read_items("Lost")
    found_items = read_items("Found")

    all_items = lost_items + found_items

    if choice == "1":

        results = search_by_name(
            all_items,
            keyword
        )

    elif choice == "2":

        results = search_by_category(
            all_items,
            keyword
        )

    elif choice == "3":

        results = search_by_location(
            all_items,
            keyword
        )

    else:
        print("Invalid choice.")
        return

    if len(results) == 0:
        print("\nNo matching records found.")

    else:

        print("\nMatching records:")

        for item in results:
            display_one_item(item)

        print("Number of matches:", len(results))