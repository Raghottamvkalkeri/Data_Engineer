#My Job Experience Using Lists
mydata = ["Jellycone", "Coding Spider" , "Capgemini" , "Aveto Consulting"]
print("Expernince of work:" , mydata)
#Removed Capgemini as I got confirmation from Aveto Consulting
# if "Capgemini" in mydata:
#     mydata.remove("Capgemini")
print("Remove Capgemini as I got confirmation from ", mydata[-1])
#Printing Job Experience 
print("Expernince of work:" , mydata)
additional_data = ""
codeexplation = ""
html_content = """
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
    <h2>My Job Experience</h2>
    <table>
        <tr><th>Company Name</th></tr>
"""


for companys in mydata:
    
    if "Capgemini" in companys:
    #mydata.remove("Capgemini")
        html_content += "<tr><td><em>Capgemini was removed from the list</em></td></tr>\n"
    else:
        if "Jellycone" in companys:
            additional_data += f" <strong> as startup </strong>\n"
        else:
            additional_data = " <strong>as startup</strong>" if companys == "Jellycone" else ""
        html_content += f"<tr><td>{companys}{additional_data}</td></tr>\n"
html_content += """
    </table>
    </body>
    </html>
    """
    
    
codeexplation = """
<!-- Explanation of the code -->
<h1>Explanation of the code:</h1>
<div style="
    border: dotted;
    padding: 20px;
    background: #000;
    color: #fff;
    width: 80%;
">#My Job Experience Using Lists
<p>mydata = ["Jellycone", "Coding Spider" , "Capgemini" , "Aveto Consulting"]</p>
<p>print("Expernince of work:" , mydata)</p>
<p>Commented Code</p>
<p>#Removed Capgemini as I got confirmation from Aveto Consulting
# if "Capgemini" in mydata:
#     mydata.remove("Capgemini")
</p>
<p>print("Remove Capgemini as I got confirmation from ", mydata[-1])</p>
#Printing Job Experience 
print("Expernince of work:" , mydata)
additional_data = ""


html_content = '''
 &lt;!DOCTYPE html&gt;
 &lt;html&gt;
 &lt;head&gt;
   <p>  &lt;title&gt;Job Experience &lt;/title&gt;
     &lt;style&gt;
        table { border-collapse: collapse; width: 50%%; font-family: 
Arial, sans-serif; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; 
}
        th { background-color: #f2f2f2; }
     &lt;/style&gt;</p>
 &lt;/head&gt;
<body>
   <p> &lt;h2&gt;My Job Experience&lt;/h2&gt;</p>
    &lt;table&gt;

        &lt;tr&gt;
        &lt;th&gt;

Company Name&lt;/th&lt;th&gt;&lt;/tr&lt;th&gt;
'''

for companys in mydata:
    
    if "Capgemini" in companys:
    #mydata.remove("Capgemini")
        html_content += "<tr><td><em>Capgemini was removed from the list</em></td></tr>\n"
    else:
        if "Jellycone" in companys:
            additional_data += f" <strong> as startup </strong>\n"
        else:
            additional_data = ""
    html_content += f"<tr><td>{companys + additional_data}</td></tr>\n"
html_content += '''
    &lt;/table&gt;
    </body>
    </html>
    </div>
    """

''

with open("job_experience.html", "w") as file:
    file.write(html_content + codeexplation)

print("HTML file 'job_experience.html' created successfully!")
