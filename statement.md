# Campus Lost & Found System

## Problem Statement

In a college campus, students can lose things like ID cards, wallets, mobile phones, books, bags, keys, earphones and water bottles. Most of the time, information about these items is shared through WhatsApp groups, classroom groups, notice boards or by asking other students.

The main problem with this method is that the information is scattered in different places. A message can also be missed or deleted, and it can become difficult to find an old post about a particular item.

To solve this problem, I decided to make a simple Python-based Campus Lost & Found System. The system allows students to enter details about lost and found items and keeps the information in an organized way. Users can also search the records and check for possible matches between lost and found items.

The project is mainly designed to apply the Python concepts learned in the first-year programming course to a practical college-related problem.

## Scope of the Project

The project is designed for use within a college campus.

The system can be used to:

- Report a lost item.
- Report a found item.
- Store item details such as name, category, location, date, description and contact number.
- View lost and found records.
- Search for items by name, category or location.
- Compare lost and found records to find possible matches.
- Update the status of an item.
- Delete a record when it is no longer required.
- Store records in local CSV files so that the data is available after the program is closed.

The current version is a console-based Python program. It does not include an online database, mobile application, login system or graphical interface. These can be considered for future versions.

## Target Users

The main users of the system are:

1. **Students**  
   Students can report items they have lost or found and search the available records.

2. **College Staff**  
   Staff members can use the system to check reported items and help students identify possible matches.

3. **Campus Administration**  
   The administration can use the system as a simple record of lost and found belongings on campus.

The project is mainly focused on students because they are the people who are most likely to lose or find everyday belongings on campus.

## High-Level Features

### 1. Report Lost Item

A student can enter details about an item that they have lost. The information is saved as a lost-item record.

### 2. Report Found Item

A student or staff member can enter details about an item they have found on campus.

### 3. View Records

The system allows users to view the stored lost and found records.

### 4. Search Items

Users can search for records using the item name, category or location.

### 5. Find Possible Matches

The system compares lost and found records using simple rules. It checks information such as the item name, category, location and description. A matching score is calculated and records with a sufficiently high score are shown as possible matches.

### 6. Update Status

The status of an item can be updated, for example when an item has been returned to its owner.

### 7. Delete Records

Records that are no longer needed can be removed from the system.

## Technologies Used

The project is developed using:

- Python 3
- CSV files for storage
- Basic Python modules and functions

The project uses fundamental concepts such as variables, input/output, conditional statements, loops, functions, lists, dictionaries, tuples, sets, string manipulation, file handling and exception handling.

## Expected Outcome

The expected outcome of this project is a simple and organized system that makes it easier for students to report, search and manage lost and found items on campus.

The project also helps demonstrate how basic Python programming concepts can be combined to solve a real-world problem.
