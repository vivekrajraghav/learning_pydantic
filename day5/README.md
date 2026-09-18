# Learning Pydantic (Computed Field): Day 5
![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 5 focuses on using the `@computed_field` decorator to automatically generate read-only data fields based on the values of other fields in the model.

## Computed Field Overview

While standard fields hold data provided by the user or an API, you often need fields derived from that incoming data. Key features explored include:

* **Dynamic Calculation (`@computed_field`):** Allows you to create a field that calculates its value on the fly rather than requiring it to be provided in the initial input data.
* **Serialization Inclusion:** A standard Python `@property` is ignored when Pydantic exports data. Adding `@computed_field` ensures this derived value is included when converting the model back to a dictionary or JSON (e.g., when calling `.model_dump()`).
* **Read-Only Nature:** Computed fields act as read-only attributes. They cannot be set or modified directly by the user after the object is instantiated.

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic

## Code Example: Computed Field

```python
from pydantic import BaseModel, computed_field

class Student(BaseModel):
    name: str
    age: int
    subject1_marks: int
    subject2_marks: int

    @computed_field
    @property
    def percentage(self) -> float:
        percent = round((self.subject1_marks + self.subject2_marks) / 2, 2)
        return percent

def update_student(student: Student):
    print(student.name)
    print(student.age)
    print(student.subject1_marks)
    print(student.subject2_marks)
    print("Percentage:", student.percentage)
    print("Updated")

student_info = {"name": "Vivek", "age": 24, "subject1_marks": 75, "subject2_marks": 80}
student1 = Student(**student_info)

update_student(student1)

```

## How This Code Works (Step-by-Step Explanation)

1. **The `@computed_field` Decorator:** This tells Pydantic to treat the method as an official field of the model. If you were to call `student1.model_dump()`, `"percentage": 77.5` would automatically be included in the resulting dictionary.
2. **The `@property` Decorator:** This is a standard Python tool that turns the `percentage()` method into a readable attribute. Because of this, we can access it cleanly via `student.percentage` instead of calling it like a function (`student.percentage()`).
3. **Dynamic Calculation:** When the `percentage` attribute is accessed, it automatically pulls `self.subject1_marks` and `self.subject2_marks`, adds them together, divides by 2, and rounds the result to 2 decimal places.
4. **Type Hinting (`-> float`):** It is mandatory to provide a return type hint on computed field functions. Pydantic relies on `-> float` to know exactly what type of data the field will output so it can accurately generate the model's schema.
5. **Seamless Access:** When `update_student` is called, `student.percentage` is accessed effortlessly alongside explicitly provided fields (`name`, `age`, etc.), despite never being passed in the original `student_info` dictionary.