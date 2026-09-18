from pydantic import BaseModel,computed_field

class Student(BaseModel):
    name:str
    age:int
    subject1_marks:int
    subject2_marks:int

    @computed_field
    @property
    def percentage(self) -> float:
        percent=round((self.subject1_marks+self.subject2_marks)/2,2)
        return percent

def update_student(student:Student):
    print(student.name)
    print(student.age)
    print(student.subject1_marks)
    print(student.subject2_marks)
    print("Percentage",student.percentage)
    print("Updated")

student_info={"name":"Vivek","age":24,"subject1_marks":75,"subject2_marks":80}
student1=Student(**student_info)

update_student(student1)