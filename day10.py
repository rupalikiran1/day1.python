info3 = {
    "firstname":"krupali",
    "lastname":"kotkar",
    "rollno":2,
    "age":25

}
print(info3['firstname'])
print(info3.get('firstname'))
y = info3.setdefault('city',"pune")
print(y)
print(info3)


# info4 = dict.fromkeys(["keyone","keytwo","keythree"])
# print(info4)

students = [
    {
        "firstname":"rupali",
        "lastname":"kotkar",
        "age":25,
        "skills":["html","css","js"]
    },
    {
        "firstname":"krupali",
        "lastname":"gund",
        "age":24,
        "skills":["html","css","js","python"]
    },
    {
        "firstname":"parul",
        "lastname":"kotkar",
        "age":22,
        "skills":["html","css","js"]
    }
]
# print(students[2]['firstname'])

# for x in students:
   # print(x['firstname'])


# program 2
# user with python skill
for x in students:
    #print(x['skills'])
  if "python" in x['skills']:
    print(x['firstname'])

# program 3
# user with python skills and age > 30
    
for x in students:
   if x['age'] > 30 and "python" in x['skills']:
      print(x['firstname'],x['age'],x["skills"])

# program 4
# name and number of skills
for x in students:
     print(x['firstname']+":"+ str(len(x['skills'])))

# average age of all students
total = 0
for x in students:
     total = total + x['age']
     print(total/len(students))

# loops,list,dictionary 
           