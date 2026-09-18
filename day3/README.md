```markdown
![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

# Learning Pydantic: Day 3

This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 3 focuses on using the `@field_validator` decorator to implement custom business logic, enforce strict rules, and apply automatic data transformations.

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic
* **Extensions:** `pydantic[email]`

## Custom Field Validation Overview

While Pydantic's built-in types and `Field` parameters handle standard constraints, real-world applications often require custom logic. Key features explored include:

*   **`@field_validator`:** A decorator that allows you to attach custom Python functions to specific fields.
*   **Domain-Specific Logic:** Enforcing specific patterns (like allowing only educational email domains) that built-in types cannot handle alone.
*   **Data Transformation:** Automatically mutating incoming data (e.g., converting strings to uppercase) before the object is created.
*   **Validation Modes (`mode="before"`):** Intercepting and validating data *before* Pydantic attempts its standard type parsing and coercion.

## Code Example: Custom Field Validators

```python
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    passed: bool

    @field_validator("email")
    @classmethod
    def email_validation(cls, value):
        valid_domains = ["edu.in", "ac.in"]
        # e.g., abcd@edu.in -> splits at @ and takes the last part
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid educational email")
        return value

    @field_validator("name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    @field_validator("age", mode="before")
    @classmethod
    def valid_age(cls, value):
        if 6 < int(value) < 26: # Added int() cast for safety in 'before' mode
            return value
        else:
            raise ValueError("Age should be in between 6 to 26")

def update_student(student: Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.passed)

student_info = {"name": "Vivek", "age": 24, "email": "abcd@edu.in", "passed": True}
student1 = Student(**student_info)
update_student(student1)

```

## How This Code Works (Step-by-Step Explanation)

1. **The `@field_validator` Decorator:** This tells Pydantic to run a specific function whenever a specific field (like `"email"`, `"name"`, or `"age"`) is being assigned a value.
2. **The `@classmethod` Requirement:** Validators in Pydantic V2 must be class methods. They receive `cls` (the model class itself) and the `value` being validated.
3. **Custom Business Logic (`email_validation`):**
* Even though `EmailStr` ensures the input looks like an email, we need to enforce that it belongs to a school (`edu.in` or `ac.in`).
* The function splits the email string at the `@` symbol, isolates the domain, and checks it against a list.
* If it fails, we `raise ValueError(...)`. Pydantic automatically catches this standard Python error and converts it into a neat `ValidationError`.


4. **Data Transformation (`name_transform`):** Validators aren't just for rejecting data; they can change it. By returning `value.upper()`, any name passed to the model will be automatically capitalized (e.g., `"Vivek"` becomes `"VIVEK"`) when the object is instantiated.
5. **Execution Order & `mode="before"` (`valid_age`):**
* By default, Pydantic parses the data *first* (e.g., turning the string `"24"` into the integer `24`) and *then* runs your custom validator (`mode="after"`).
* By setting `mode="before"`, the `valid_age` function receives the raw, unparsed input exactly as it came in. This is highly useful if you need to inspect or clean messy raw data before Pydantic's strict type engine attempts to evaluate it.