from pydantic import BaseModel, EmailStr, Field,EmailStr
from dotenv import load_dotenv
from typing import List, Optional, Literal


# load environment variables
load_dotenv()


class Student(BaseModel):
    name : str = "Rahul"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(ge=0.0, le=10.0,default=8.5)


new_student = {"age":21,"name":"piyush","email":"piyush@example.com"}

student = Student(**new_student)

print(student)