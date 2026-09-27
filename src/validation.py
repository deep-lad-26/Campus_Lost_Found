def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("This field cannot be empty.")


def get_phone_number():
    while True:
        phone = input("Enter contact number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Please enter a valid 10-digit number.")


def get_category():
    categories = [
        "ID Card",
        "Wallet",
        "Mobile Phone",
        "Earphones",
        "Book",
        "Water Bottle",
        "Bag",
        "Keys",
        "Other"
    ]

    print("\nCategories:")

    for i in range(len(categories)):
        print(i + 1, ".", categories[i])

    while True:
        choice = input("Choose category number: ")

        if choice.isdigit():
            number = int(choice)

            if number >= 1 and number <= len(categories):
                return categories[number - 1]

        print("Invalid category.")