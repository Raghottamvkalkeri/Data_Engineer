# fruits1 = { "apple","banana","cherry"}
# fruits2 = {"cherry", "mango", "grape"}

# print(fruits1);
# print(fruits2);
# # #Example of Union
# # print(fruits1 | fruits2)
# # #Example of Intersection
# # print("Intersection:", fruits1 & fruits2) 
# # #Example of Difference
# # #It checks the Left Hand side
# # print("Difference:", fruits1 - fruits2)
# # #It checks the Left Hand side
# # print("Difference:", fruits2 - fruits1)
# # #Example of Symmetric
# # print("Symmetric Difference:", fruits1 ^ fruits2)



#Using data as employess 
employees = [
    {
        "name": "Raghottam",
        "skills": ["Python", "Django", "Vue.js", "SQL"]
    },
    {
        "name": "Amit",
        "skills": ["Java", "Spring Boot", "SQL", "Vue.js"]
    },
    {
        "name": "Neha",
        "skills": ["Python", "Flask", "React", "SQL"]
    }
]

#print("Employess \n" ,employees)

#print (employees[0]["name"], employees[0]['skills'])

for getemp in employees:
    # print("Employee Name" ,getemp['name'])
    # print("Skills :")
    allskills = set(skill for allemp in employees if allemp != getemp for skill in allemp['skills'])
    unique_skills = set(getemp['skills']) - allskills 
    print(getemp['name'] , unique_skills)


    # for emp in employees:
    # other_skills = set(skill for other_emp in employees if other_emp != emp for skill in other_emp["skills"])
    # unique_skills = set(emp["skills"]) - other_skills  # Skills not found in others
    # print(f"{emp['name']} → {unique_skills}")


#Still I have some confusion on this not getting how to utilise and what is different in code structure
    
