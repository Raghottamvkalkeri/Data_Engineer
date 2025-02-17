# Creating a tuple
job_experience = ("Jellycone", "Coding Spider", "Capgemini", "Aveto Consulting")

# Accessing elements
print("First company:", job_experience[0])  # Output: Jellycone
print("Last company:", job_experience[-1])  # Output: Aveto Consulting

# Iterating through a tuple
print("\nJob Experience List:")
for company in job_experience:
    print(company)

# Finding the index of an item
index = job_experience.index("Capgemini")
print("\nCapgemini is at index:", index)

# Tuple length
print("Total companies:", len(job_experience))

# Attempting to modify a tuple (will raise an error)
# job_experience[1] = "New Company"  # ❌ TypeError: 'tuple' object does not support item assignment

