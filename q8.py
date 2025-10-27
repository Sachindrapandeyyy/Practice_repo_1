student = {
    "name": "rahul",
    "age":21,
    "dob": "01-01-2002"
    
}
print(student["name"])
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())

'''
rahul
rahul
dict_keys(['name', 'age', 'dob'])
dict_values(['rahul', 21, '01-01-2002'])
dict_items([('name', 'rahul'), ('age', 21), ('dob', '01-01-2002')])
'''