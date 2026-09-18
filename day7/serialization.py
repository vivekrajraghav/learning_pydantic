from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int

class Student(BaseModel):
    name:str
    age:int
    gender:str = "Male"
    address:Address

student_info={"name":"Vivek","age":24,"address":{"city":"Khurja","state":"Uttar Pradesh","pin":203131}}
student1=Student(**student_info)
temp=student1.model_dump()
print(temp)
print(type(temp))

# To Get JSON of data
temp1=student1.model_dump_json()
print(temp1)
print(type(temp1))

# Getting only selected data in JSON or anywhere
# Only includes asked data
temp3=student1.model_dump(include=["name","age"]) 
print(temp3)

# Only exclude asked data
temp4=student1.model_dump(exclude=["name","age"]) 
print(temp4)

# Excludes those data which have default values and not given by user
temp5=student1.model_dump(exclude_unset=True) 
print(temp5)
