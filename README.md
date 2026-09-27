# Campus Lost & Found System

## About the Project

The Campus Lost & Found System is a simple Python project made to help students keep track of things they lose or find on campus.

In a college, students may lose items such as ID cards, wallets, mobile phones, books, bags, keys, earphones or water bottles. Usually, people post about these items in WhatsApp groups or tell their classmates. The problem is that these messages can get mixed up or missed.

This project keeps the information in one place. A user can report a lost or found item, search the records and check whether a lost item has a possible match with a found item.

The project is developed as part of the **CSE1021 - Introduction to Problem Solving and Programming** course.

---

## Main Features

- Report a lost item
- Report a found item
- View all lost items
- View all found items
- Search items by:
  - Name
  - Category
  - Location
- Find possible matches between lost and found items
- Update the status of an item
- Delete an item record
- Save records in CSV files
- Basic input validation and error handling

---

## Technologies Used

- **Python 3**
- **CSV files** for storing data
- Python functions and modules
- Basic file handling

The project uses concepts learned in the course, such as:

- Variables
- Input and output
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- Sets
- String manipulation
- File handling
- Exception handling

---

## Project Structure

```text
Campus_Lost_Found/
│
├── main.py
├── item_functions.py
├── search_functions.py
├── match_functions.py
├── file_functions.py
├── validation.py
├── display_functions.py
│
├── lost_items.csv
└── found_items.csv
```

### What each file does

**main.py**  
Contains the main menu and connects the different parts of the program.

**item_functions.py**  
Used for adding items, updating item status and deleting records.

**search_functions.py**  
Contains the functions used to search for lost and found items.

**match_functions.py**  
Compares lost and found records and calculates a simple matching score.

**file_functions.py**  
Handles reading and writing data to CSV files.

**validation.py**  
Checks user input, such as empty fields, phone numbers and item categories.

**display_functions.py**  
Displays item records in a readable format.

---

## How the Matching Works

The matching part is a simple rule-based system.

When a lost item is compared with a found item, the program checks different details:

- Same item name = **3 points**
- Similar item name = **2 points**
- Same category = **2 points**
- Same location = **2 points**
- Common word in the description = **1 point**

If the total score is **4 or more**, the program displays the two records as a possible match.

This is only a basic matching method. It does not use machine learning or artificial intelligence.

---

## How to Run the Project

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check it by opening Command Prompt and typing:

```text
python --version
```

### 2. Open the Project Folder

Open the `Campus_Lost_Found` folder.

Make sure all the Python files are inside the same folder.

### 3. Open Command Prompt

Click the address bar in File Explorer, type:

```text
cmd
```

and press Enter.

### 4. Run the Program

Type:

```text
python main.py
```

The main menu should appear.

---

## Example Menu

```text
======================================
       CAMPUS LOST & FOUND SYSTEM
======================================
1. Report Lost Item
2. Report Found Item
3. View Lost Items
4. View Found Items
5. Search Items
6. Find Possible Matches
7. Update Item Status
8. Delete Item
9. Exit
======================================
```

The user can enter the number of the option they want to use.

---

## Data Storage

The project uses two CSV files:

```text
lost_items.csv
found_items.csv
```

The records contain information such as:

- ID
- Item name
- Category
- Location
- Date
- Description
- Contact number
- Status

CSV files were used because they are simple to understand and suitable for this beginner-level project.

---

## Input Validation

The program performs some basic checks before saving information.

For example:

- Empty fields are not accepted.
- The contact number should contain 10 digits.
- The category should be selected from the available categories.
- Invalid menu choices are handled.
- Invalid item IDs are handled.

These checks help prevent incorrect data from being entered.

---

## Testing

The following parts of the program can be tested:

| Feature | Test |
|---|---|
| Report Lost Item | Add a new lost item |
| Report Found Item | Add a new found item |
| View Items | Check saved records |
| Search | Search using name, category or location |
| Matching | Add similar lost and found records |
| Update | Change an item's status |
| Delete | Remove an existing record |
| Validation | Enter invalid or empty input |

The program was tested using different inputs to check whether the main functions work correctly.

---

## Limitations

The current version is a console-based application, so it has some limitations.

- There is no graphical user interface.
- There is no online database.
- There is no login system.
- It is mainly designed for use on one computer.
- Matching is based on simple rules rather than advanced algorithms.
- Contact information is stored directly in the CSV file.

These limitations can be addressed in future versions.

---

## Future Improvements

Some features that could be added later are:

- Graphical user interface
- Login and user accounts
- Online database
- Admin panel
- Better item matching
- Email or notification system
- Image upload for items
- Web or mobile version
- Better privacy and security for contact information

---

## What I Learned

While making this project, I got practice with different Python concepts and learned how they can be used together to solve a practical problem.

The main things I worked with were functions, loops, conditions, lists, dictionaries, sets, file handling and exception handling.

I also learned that dividing a program into different files and functions makes the code easier to understand and manage.

---

## Conclusion

The Campus Lost & Found System is a simple project that tries to solve a common problem in college campuses.

Instead of keeping lost and found information scattered across different messages and groups, the program keeps the records in an organized form. It also provides basic searching and matching features.

The project is intentionally kept simple so that the Python concepts learned in the course can be clearly understood and demonstrated.

---

## Author

**Name:** __________________________

**Registration Number:** __________________________

**Course:** CSE1021 - Introduction to Problem Solving and Programming

**Department/School:** __________________________
