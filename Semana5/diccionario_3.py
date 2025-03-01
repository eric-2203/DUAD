list_of_keys = ["access_level" , "age"]
employee = {
    "name" : "Eric",
    "email" : "eric2203@outlook.es",
    "address": "Guapiles",
    "access_level" : 6,
    "age" : 30,
}
for keys in list_of_keys:
    employee.pop(keys)
print(employee)