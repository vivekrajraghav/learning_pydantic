from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):
    name:str
    email:EmailStr
    age:int
    passed:bool

    @field_validator("email")
    @classmethod
    def email_validation(cls,value):
        valid_domains=["edu.in","ac.in"]
        #abc@.edu.in
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid educational email")
        return value

    @field_validator("name")
    @classmethod
    def name_transform(cls,value):
        return value.upper()

    @field_validator("age",mode="before")
    @classmethod
    def valid_age(cls,value):
        if 6<value<26:
            return value
        else:
            raise ValueError("Age should be in between 6 to 26")

def update_student(student:Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.passed)

student_info={"name":"Vivek","age":24,"email":"abcd@edu.in","passed":True}
student1=Student(**student_info)
update_student(student1)