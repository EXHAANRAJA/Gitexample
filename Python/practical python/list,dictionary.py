# We create dictionary and list combine together and 
# get required information inside the list
contactdetail = {
    "student":4,
    "detail": 
        [
            {"name":"Ahsan Ul HAQ","email":"rajaahsanulhaq3@gmail.com"},
            {"name" :"ABC","email":"example1@gmail.com"},
            {"name":"DEF","email":"example2@gmail.com"},
            {"name":"GHI","email":"example3@gmail.com"}
        ]
}

print("Contact detail given below:")
for student in contactdetail["detail"]:
    print(student['name'] + " : " + student['email'])
