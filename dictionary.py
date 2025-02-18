#Example for Dictionary

# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

#Get all keys
print(my_dict)

#Get all values
print(my_dict.values())

#Get name form dictionary
print(my_dict["name"])

#Get age from dictionary
print(my_dict.get("age"))

#Get city from dictionary
print(my_dict.get("city"))

#get Name as name and age as age
name = my_dict.get("name")
age = my_dict.get("age")
# print(my_dict.get("name", "age"))
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
    "company": [{
        "name": "Jellycone",
        "status": "Active",
        "role": "Platform Developer",
        "city": "Hubli",
        "experience" : ['Intern', 'Platform Developer']
    },
    {
        "name": "Coding Spider",
        "status": "Active",
        "role": "Software Developer",
        "city": "Hubli",
        "experience" : ['Software Engineer']
    },
    {
        "name": "Capgemini",
        "status": "Removed",
        "role": "Software Developer",
        "city": "Not Specified",
        "experience" : ['']
    },
    {
        "name": "Aveto Consulting",
        "status": "Active",
        "role": "Senior Software Developer",
        "city": "Banglore - Remote",
        "experience" : ['Associate', 'Software Engineer', 'Senior Software Developer']
        
    }],
    
}

print("\nBasic Details:")
print("Name:", basic_details["name"])
print("Age:", basic_details["age"])
print("City:", basic_details["city"])
# print("Company Name:", basic_details["company"][0]["name"])

for index, company in enumerate(basic_details["company"], start=1):
     if index > 0:  # Print separator after the first company
        print("-----------------") 
    
        print("No:", index)
        print("Company Name:", company["name"])
        print("Status:", company["status"])
        print("Role:", company["role"]) 
        print("City:", company['city'])
        print('Experience:')
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