from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated

class Students(BaseModel):
    name:str
    father:str=Field(max_length=50)
    roll_no:Annotated[int,Field(gt=1000,strict=True)]
    email:Optional[EmailStr]=None
    linkedin:Optional[AnyUrl]=None
    total_marks:int=Field(le=300)
    passed:bool = False
    subjects:Optional[List[str]] = None
    sub_marks:Annotated[Dict[str,int],Field(max_length=3,title="Subject wise marks",description="Please enter subjects followerd by names in key value pairs",examples=[{"Subject1":65}])]
    contact_details:dict[str,str]


def update_details(student:Students):
    print(student.name)
    print(student.roll_no)
    print(student.father)
    print(student.contact_details)
    print(student.subjects)
    print(student.sub_marks)
    print(student.total_marks)
    print(student.passed)
    print(student.linkedin)
    print(student.email)

student_info={"name":"Vivek","roll_no":123456,"father":"Rajkumar","email":"abc@gmail.com","subjects":["English","Physics","Chemistry"],"sub_marks":{"English":75,"Physics":80,"Chemistry":70},"total_marks":225,"passed":True,"contact_details":{"mobile":"1234567890"}}
student1=Students(**student_info)
update_details(student1)
