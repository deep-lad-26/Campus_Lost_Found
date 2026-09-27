import csv
import os


LOST_FILE = "lost_items.csv"
FOUND_FILE = "found_items.csv"


def get_file_name(item_type):
    if item_type == "Lost":
        return LOST_FILE
    else:
        return FOUND_FILE


def create_file_if_needed(item_type):
    file_name = get_file_name(item_type)

    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Name",
                "Category",
                "Location",
                "Date",
                "Description",
                "Contact",
                "Status"
            ])


def read_items(item_type):
    create_file_if_needed(item_type)

    file_name = get_file_name(item_type)

    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)

            items = []

            for row in reader:
                items.append(row)

            return items

    except FileNotFoundError:
        return []


def save_items(item_type, items):
    file_name = get_file_name(item_type)

    with open(file_name, "w", newline="") as file:
        fieldnames = [
            "ID",
            "Name",
            "Category",
            "Location",
            "Date",
            "Description",
            "Contact",
            "Status"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for item in items:
            writer.writerow(item)


def generate_id(item_type):
    items = read_items(item_type)

    if len(items) == 0:
        return 1

    largest_id = 0

    for item in items:
        try:
            current_id = int(item["ID"])

            if current_id > largest_id:
                largest_id = current_id

        except ValueError:
            continue

    return largest_id + 1