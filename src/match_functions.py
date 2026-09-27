from file_functions import read_items
from display_functions import display_one_item


def calculate_match_score(lost, found):

    score = 0

    if lost["Name"].lower() == found["Name"].lower():
        score += 3

    elif lost["Name"].lower() in found["Name"].lower():
        score += 2

    if lost["Category"].lower() == found["Category"].lower():
        score += 2

    if lost["Location"].lower() == found["Location"].lower():
        score += 2

    lost_words = set(
        lost["Description"].lower().split()
    )

    found_words = set(
        found["Description"].lower().split()
    )

    common_words = lost_words.intersection(
        found_words
    )

    if len(common_words) > 0:
        score += 1

    return score


def find_matches():

    lost_items = read_items("Lost")
    found_items = read_items("Found")

    if len(lost_items) == 0:
        print("There are no lost items.")
        return

    if len(found_items) == 0:
        print("There are no found items.")
        return

    print("\n================================")
    print("POSSIBLE MATCHES")
    print("================================")

    found_match = False

    for lost in lost_items:

        if lost["Status"].lower() == "returned":
            continue

        for found in found_items:

            if found["Status"].lower() == "claimed":
                continue

            score = calculate_match_score(
                lost,
                found
            )

            if score >= 4:

                found_match = True

                print("\nPossible Match")
                print("Match Score:", score)

                print("\nLost Item:")
                display_one_item(lost)

                print("\nFound Item:")
                display_one_item(found)

    if not found_match:
        print("No strong matches found.")