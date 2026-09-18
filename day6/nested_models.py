from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int

class Student(BaseModel):
    name:str
    age:int
    gender:str
    address:Address

address_dict={"city":"Khurja","state":"Uttar Pradesh","pin":203131}
address1=Address(**address_dict)

student_dict={"name":"Vivek","age":24,"gender":"Male","address":address1}
student1=Student(**student_dict)

print(student1)

# Getting adress info 
print(student1.address.pin) #we can use dot . instead of [] 
print(student1.address.state)
print(student1.address.city)