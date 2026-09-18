from pydantic import BaseModel
from typing import List,Dict

class Students(BaseModel):
    name:str
    roll_no:int
    total_marks:int
    passed:bool
    subjects:List[str]
    sub_marks:Dict[str,int] #Dict[key,value]
    contact_details:dict[str,str]

def update_details(student:Students):
    print(student.name)
    print(student.roll_no)
    print(student.contact_details)
    print(student.subjects)
    print(student.sub_marks)
    print(student.total_marks)
    print(student.passed)
student_info={"name":"Vivek","roll_no":123456,"subjects":["English","Physics","Chemistry"],"sub_marks":{"English":75,"Physics":80,"Chemistry":70},"total_marks":225,"passed":True,"contact_details":{"mobile":"1234567890","email":"abc@gmail.com"}}
student1=Students(**student_info)
update_details(student1)
