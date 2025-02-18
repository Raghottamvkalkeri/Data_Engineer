# Python - Basic Data Structures (DS)

Python provides several built-in data structures to store and manipulate data efficiently. Two fundamental structures are **Lists** and **Tuples**. Understanding their properties and use cases helps in choosing the right one for specific scenarios.

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

## 🔍 Comparison Summary

| Feature       | List (`[]`) | Tuple (`()`) |
|--------------|------------|--------------|
| **Mutability** | Mutable (modifiable) | Immutable (fixed) |
| **Performance** | Slower (dynamic resizing) | Faster (fixed size) |
| **Memory Usage** | Uses more memory | Uses less memory |
| **Methods** | Many built-in methods | Limited methods |
| **Use Case** | When modifications are needed | When data should not change |

---

## 📌 Example Usage in Python

```python
# List Example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an element
fruits.remove("banana")  # Removing an element
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Tuple Example
coordinates = (10.5, 20.7)
# coordinates[0] = 15  # ❌ Error: Tuples are immutable
print(coordinates[0])  # Output: 10.5
```

📌 **Tip:** Use **lists** when frequent modifications are needed, and **tuples** when immutability and performance are priorities.

---

### 📖 Learn More
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

🚀 **Happy Coding!** 🎯
