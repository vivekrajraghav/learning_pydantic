from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict

class Student(BaseModel):
    name:str
    age:int
    email:EmailStr
    contact:Dict[str,str]

    @model_validator(mode="after")
    def valid_emergency_contact(cls,model):
        if model.age<18 and "emergency" not in model.contact:
            raise ValueError("Minor students must have an emergency contact")
        return model

def update_student_details(student:Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.contact)

student_info={"name":"Dhruv","age":15,"email":"abc@gmail.com","contact":{"mobile":"123"
"56790"}}

student1=Student(**student_info)

update_student_details(student1)