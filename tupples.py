
#My Job Experience Using Lists
mydata = ["Jellycone", "Coding Spider (merged with Jellycone)" , "Capgemini" , "Aveto Consulting"]
print("Expernince of work:" , mydata)
#Removed Capgemini as I got confirmation from Aveto Consulting
# if "Capgemini" in mydata:
#     mydata.remove("Capgemini")
print("Remove Capgemini as I got confirmation from ", mydata[-1])
#Printing Job Experience 
print("Expernince of work:" , mydata)
additional_data = ""
codeexplation = ""
html_contents = """
<!DOCTYPE html>
<html>
<head>
    <title>Job Experience</title>
    <style>
        table { border-collapse: collapse; width: 50%%; font-family: 
Arial, sans-serif; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; 
}
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>My Job Experience Lists</h2>
    <table>
        <tr><th>Company Name</th></tr>
"""


for companys in mydata:
    
    if "Capgemini" in companys:
    #mydata.remove("Capgemini")
        html_contents += "<tr><td><em>Capgemini was removed from the list</em></td></tr>\n"
    else:
        if "Jellycone" in companys:
            additional_data += f" <strong> as startup </strong>\n"
        else:
            additional_data = " <strong>as startup</strong>" if companys == "Jellycone" else ""
        html_contents += f"<tr><td>{companys}{additional_data}</td></tr>\n"
html_contents += """
    </table>
    </body>
    </html>
    """
    
    






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


html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Job Experience</title>
<style>
    table { border-collapse: collapse; width: 50%; font-family: Arial, sans-serif; }
    th, td { border: 1px solid black; padding: 8px; text-align: left; }
    </style>
</head>
<body>
<h2>My Job Experience Tupples</h2>
<table>
    <tr>
    <th>No.</th>
    <th>Company Name</th>
    </tr>
"""
for company in job_experience:
        if "Capgemini" in company:
            html_content += f"<tr><td>{job_experience.index(company) + 1}</td><td colspan='2'><em>{company} was removed from the list</em></td></tr>\n"
        else:
            html_content += f"<tr><td>{job_experience.index(company) + 1}</td> \n <td>{company}</td></tr>\n"
html_content += """
</table>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_contents + html_content)