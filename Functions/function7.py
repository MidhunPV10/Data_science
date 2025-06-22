# variable-length argument
def employee(name,*skills):
    print("Employee Details....")
    print("Name :",name)
    print("Skills :",skills)
employee("Midhun","Python")
employee("Adarsh","Python","Html","CSS")