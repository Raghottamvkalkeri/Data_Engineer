# Python - Basic Data Structures (DS)

Python provides several built-in data structures to store and manipulate data efficiently. Three fundamental structures are **Lists**, **Tuples**, and **Dictionaries**. Understanding their properties and use cases helps in choosing the right one for specific scenarios.

---

## 📌 Lists in Python
A **list** is an ordered, **mutable** (modifiable) collection of elements that allows for dynamic resizing.

### 🔹 Key Characteristics
- **Mutable** → Lists can be modified after creation (adding, removing, or updating elements).
- **Slightly slower** → Due to dynamic resizing and memory allocation.
- **Syntax:** Defined using **square brackets** `[]`.
  
  ```python
  my_list = [1, 2, 3, 4, 5]
  ```
- **Common Methods:**
  - `append(value)`: Adds an item to the end of the list.
  - `remove(value)`: Removes the first occurrence of a specified item.
  - `sort()`: Sorts the list in ascending order.
  - `pop(index)`: Removes an element by index and returns it.
  - `index(value)`: Returns the first index of a specified value.

### ✅ When to Use Lists?
- You need a **dynamic**, modifiable collection.
- Frequent **additions/removals** of elements are required.
- You need sorting, filtering, or searching functionality.
- Storing **structured data** like objects, dictionaries, or nested lists.

---

## 📌 Tuples in Python
A **tuple** is an ordered, **immutable** (cannot be modified) collection of elements with a fixed size.

### 🔹 Key Characteristics
- **Immutable** → Cannot be changed after creation.
- **Faster** → More efficient in memory and processing since they are static.
- **Syntax:** Defined using **parentheses** `()`.
  
  ```python
  my_tuple = (1, 2, 3, 4, 5)
  ```
- **Common Methods:**
  - `count(value)`: Returns the count of a specific value in the tuple.
  - `index(value)`: Returns the index of the first occurrence of a value.

### ✅ When to Use Tuples?
- You need **immutable** data (ensuring the values never change).
- **Performance** is a concern (tuples are faster than lists).
- You want to use data as a **dictionary key** (only immutable types can be keys).
- Working with **databases**, where fixed records are stored.
- Returning **multiple values** from a function.
- Handling **variable arguments** in function parameters.



---

## 📌 Dictionaries in Python
A **dictionary** is an unordered collection of key-value pairs, optimized for fast lookups.

### 🔹 Key Characteristics
- **Mutable** → Can be modified after creation (adding, updating, and deleting key-value pairs).
- **Fast lookups** → Uses a hash table for efficient retrieval.
- **Syntax:** Defined using **curly braces** `{}`.
  
  ```python
  my_dict = {
      "name": "Alice",
      "age": 25,
      "city": "New York"
  }
  ```
- **Common Methods:**
  - `keys()`: Returns all keys in the dictionary.
  - `values()`: Returns all values in the dictionary.
  - `get(key)`: Retrieves a value for the given key (returns `None` if the key is missing).
  - `update(dict)`: Merges another dictionary into the existing one.
  - `pop(key)`: Removes a key-value pair and returns its value.

### ✅ When to Use Dictionaries?
- When data needs **key-based lookups**.
- To store structured data in a **flexible, labeled format**.
- When handling **JSON-like data**.
- When optimizing performance for **fast retrieval**.

---

## 📌 Example Usage in Python

```python
# Example for Dictionary

# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Get all keys
print(my_dict.keys())

# Get all values
print(my_dict.values())

# Get name from dictionary
print(my_dict["name"])

# Get age from dictionary
print(my_dict.get("age"))

# Get city from dictionary
print(my_dict.get("city"))

# Get Name as name and Age as age
name = my_dict.get("name")
age = my_dict.get("age")
print(name, age)

# Dictionary containing job experience with company names and statuses
job_experience = {
    1: {"company": "Jellycone", "status": "Active"},
    2: {"company": "Coding Spider", "status": "Active"},
    3: {"company": "Capgemini", "status": "Removed"},
    4: {"company": "Aveto Consulting", "status": "Active"}
}

basic_details = {
    "name": "Raghottam",
    "age": 28,
    "city": "Hubli",
    "company": [
        {"name": "Jellycone", "status": "Active", "role": "Platform Developer", "city": "Hubli", "experience": ['Intern', 'Platform Developer']},
        {"name": "Coding Spider", "status": "Active", "role": "Software Developer", "city": "Hubli", "experience": ['Software Engineer']},
        {"name": "Capgemini", "status": "Removed", "role": "Software Developer", "city": "Not Specified", "experience": ['']},
        {"name": "Aveto Consulting", "status": "Active", "role": "Senior Software Developer", "city": "Bangalore - Remote", "experience": ['Associate', 'Software Engineer', 'Senior Software Developer']}
    ]
}

for index, company in enumerate(basic_details["company"], start=1):
    print("-----------------") 
    print("No:", index)
    print("Company Name:", company["name"])
    print("Status:", company["status"])
    print("Role:", company["role"]) 
    print("City:", company['city'])
    counter = 0
    for exp_index, exp in enumerate(company['experience']):
        if len(exp) > 0:
            counter += 1
            if counter > 1:
                print(",", exp , end=" ")
            else:
                print(exp , end=" ")
    print()

    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Job Experience</title>
    <style>
    table { border-collapse: collapse; width: 50%; font-family: Arial, sans-serif; }
    th, td { border: 1px solid black; padding: 8px; text-align: left; }
    ; }
    th { background-color: #f2f2f2; }
    </style>
    </head>
    <h2>My Job Experience</h2>
    <table>
        <tr>
            <th>Company Name</th>
            <th>Status</th>
            <th>Role</th>
            <th>City</th>
            <th>Experience</th>
            </tr>
"""
for index, company in enumerate(basic_details["company"], start=1):
                html += f"""
                <tr>
                <td>{company["name"]}</td>
                <td>{company["status"]}</td>
                <td>{company["role"]}</td>
                <td>{company["city"]}</td>
                <td>
                    <ul>
                        {', '.join(company['experience'])}
                    </ul>
                </td>
            </tr>
            """
html += """
                </table>
                </body>
                </html>
                """
            
with open("dictionary.html", "w") as html_file:
    html_file.write(html)
```

## 📌 Sets in Python
A **set** is an unordered collection of **unique** elements. Unlike lists or tuples, sets do not allow duplicates and provide fast lookups.

### 👉 Key Characteristics
- **Unordered** → The elements have no defined order.
- **Unique Elements** → Duplicates are automatically removed.
- **Fast Operations** → Ideal for membership tests and set operations.
- **Syntax:** Defined using **curly braces** `{}`.


## When to Use Sets?

✅ **When you need to store unique values only** (no duplicates).

✅ **For fast membership testing** (`value in set`).

✅ **When performing mathematical set operations** (union, intersection, difference).

✅ **When order doesn't matter** (sets are unordered).

✅ **To remove duplicates from a list quickly.**

✅ **When you need an efficient way to compare groups of items.**

✅ **For optimizing performance** in cases where frequent lookups and uniqueness checks are needed.


### 📌 Creating a Set
```python
my_set = {1, 2, 3, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}  # Duplicates removed
```

### 📌 Adding Elements
```python
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
```

### 📌 Removing Elements
```python
my_set.remove(3)  # Removes 3, raises error if not found
my_set.discard(10)  # Does nothing if 10 is not in the set
```

### 📌 Set Operations
#### **Union (All Unique Elements from Both Sets)**
```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
```

#### **Intersection (Common Elements)**
```python
print(A & B)  # Output: {3}
```

#### **Difference (Elements in A but not in B)**
```python
print(A - B)  # Output: {1, 2}
```

#### **Symmetric Difference (Elements in A or B, but not both)**
```python
print(A ^ B)  # Output: {1, 2, 4, 5}
```

---

## 📌 Real-World Example: Finding Unique Skills for Each Employee

```python
employees = [
    {"name": "Raghottam", "skills": ["Python", "Django", "Vue.js", "SQL"]},
    {"name": "Amit", "skills": ["Java", "Spring Boot", "SQL", "Vue.js"]},
    {"name": "Neha", "skills": ["Python", "Flask", "React", "SQL"]}
]

for emp in employees:
    other_skills = set(skill for other_emp in employees if other_emp != emp for skill in other_emp["skills"])
    unique_skills = set(emp["skills"]) - other_skills
    print(f"{emp['name']} → {unique_skills}")
```

---


# How to Get Data from CSV File and Create Another CSV

This project reads a CSV file (`zomato.csv`), extracts the `name` and `online_order` columns, and converts the data into both JSON and CSV formats.

## Files

- `zomato.csv` - Input data file containing restaurant details.
- `zomatodata.csv` - Processed CSV file with selected columns and added serial numbers.
- `zomato.json` - JSON file containing the extracted data.
- `zomato.py` - Python script for processing the data.

## Requirements

Ensure you have Python installed along with the required library:

```sh
pip install pandas
```

## Usage

Run the script to process the data:

```sh
python zomato.py
```

## Code Overview

The script performs the following steps:

1. Reads `zomato.csv` using Pandas.
2. Selects only `name` and `online_order` columns.
3. Converts the selected data into JSON format and saves it as `zomato.json`.
4. Saves the processed data into `zomatodata.csv` with an index column (`SL No`).

## Python Script

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('zomato.csv')

# Select only the name and online_order columns
selected_columns = df[['name', 'online_order']]

# Convert to JSON
json_data = selected_columns.to_json(orient='records')
csv_data = selected_columns.to_csv('zomatodata.csv', index=True , index_label="SL No")

# Write the JSON data to a file
with open('zomato.json', 'w') as f:
    f.write(json_data)
```

## Why Use Pandas Instead of the Default CSV Module?

1. **Ease of Use**: Pandas provides a simple interface for reading, writing, and manipulating data.
2. **Built-in Functions**: It has built-in functions for handling missing values, filtering, and transformation.
3. **Efficient Data Handling**: Pandas is optimized for working with large datasets, unlike the built-in `csv` module, which is more suited for basic file operations.
4. **Automatic Data Type Inference**: Pandas intelligently detects and assigns data types, reducing the need for manual type conversion.
5. **Multiple Export Formats**: It allows seamless conversion to CSV, JSON, Excel, and other formats with minimal effort.

## Example Output

### JSON Output (`zomato.json`):
```json
[
  {"name": "Restaurant A", "online_order": "Yes"},
  {"name": "Restaurant B", "online_order": "No"},
  {"name": "Restaurant C", "online_order": "Yes"}
]
```

### CSV Output (`zomatodata.csv`):
```
SL No,name,online_order
1,Restaurant A,Yes
2,Restaurant B,No
3,Restaurant C,Yes
```



### 📖 Learn More
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
---

🚀 **Happy Coding!** 🎯
