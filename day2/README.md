# Learning Pydantic (Data Validation): Day 2

![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)


This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 2 focuses on moving beyond basic type hints to enforce advanced validation rules, specialized network types, and strict constraints.

## Advanced Validation Features

Instead of just checking if a variable is a basic string or integer, Pydantic allows you to enforce strict business rules on your data. Key features explored include:

*   **Granular Constraints (`Field`):** Restrict string lengths (e.g., `max_length`), set numeric thresholds (`gt` for greater than, `le` for less than or equal to), and manage metadata.
*   **Specialized Types:** Validate complex structures like Emails (`EmailStr`) and URLs (`AnyUrl`) out of the box without writing custom regular expressions.
*   **Strict Typing:** Prevent Pydantic from automatically coercing types (e.g., stopping the string `"1234"` from silently becoming the integer `1234`).
*   **Optionality:** Elegantly handle missing or null data using `Optional` and default values.

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic
* **Extensions:** `pydantic[email]` (required for `EmailStr`)

## Code Example: Advanced Student Validation

```python
from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Students(BaseModel):
    name: str
    father: str = Field(max_length=50)
    roll_no: Annotated[int, Field(gt=1000, strict=True)]
    email: Optional[EmailStr] = None
    linkedin: Optional[AnyUrl] = None
    total_marks: int = Field(le=300)
    passed: bool = False
    subjects: Optional[List[str]] = None
    sub_marks: Annotated[Dict[str, int], Field(max_length=3, title="Subject wise marks", description="Please enter subjects followerd by names in key value pairs", examples=[{"Subject1": 65}])]
    contact_details: dict[str, str]

def update_details(student: Students):
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

student_info = {
    "name": "Vivek",
    "roll_no": 123456,
    "father": "Rajkumar",
    "email": "abc@gmail.com",
    "subjects": ["English", "Physics", "Chemistry"],
    "sub_marks": {"English": 75, "Physics": 80, "Chemistry": 70},
    "total_marks": 225,
    "passed": True,
    "contact_details": {"mobile": "1234567890"}
}

student1 = Students(**student_info)
update_details(student1)

```

## How This Code Works (Step-by-Step Explanation)

1. **`Field` Function for Granular Control:** We use `Field()` to assign specific limits to our variables.
* `father: str = Field(max_length=50)` ensures the father's name string cannot exceed 50 characters.
* `total_marks: int = Field(le=300)` ensures the total marks are **L**ess than or **E**qual to 300.


2. **Combining Types with `Annotated`:** Pydantic V2 highly recommends using `Annotated` to attach `Field` constraints to types.
* `roll_no: Annotated[int, Field(gt=1000, strict=True)]` means the roll number must be an integer **G**reater **T**han 1000.
* By setting `strict=True`, we tell Pydantic *not* to try and fix bad data. If a user passes `"123456"` as a string instead of an integer, validation will fail immediately.


3. **Specialized Types (`EmailStr`, `AnyUrl`):** Instead of standard strings, `email` and `linkedin` use built-in Pydantic network types. The `EmailStr` type requires the `email-validator` library (installed via `pydantic[email]`) and automatically ensures the provided string is a valid, properly formatted email address.
4. **Handling Missing Data (`Optional` and Defaults):**
* `Optional[...]` signals that a field is allowed to be `None` (empty).
* By assigning a default value like `= None` (or `= False` for the `passed` boolean), Pydantic will auto-populate these variables if they are missing from the `student_info` input dictionary, preventing `KeyError` crashes.


5. **Advanced Dictionary Constraints:** The `sub_marks` field combines `Annotated`, `Dict`, and `Field`. It demands a dictionary mapping strings to integers, restricts it to a maximum of 3 key-value pairs (`max_length=3`), and attaches documentation metadata (`title`, `description`, `examples`) which is highly useful when generating automated APIs with FastAPI.

