![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

# Learning Pydantic (Model Validator): Day 4

This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 4 focuses on using the `@model_validator` decorator to implement cross-field validation, allowing us to validate data based on the relationship between multiple different fields.

## Model Validation Overview

While `@field_validator` (from Day 3) is great for checking a single piece of data independently, real-world data often has complex dependencies. Key features explored include:

*   **Cross-Field Validation (`@model_validator`):** Validating the entire object as a whole. This is essential when the validity of one field depends on the value of another.
*   **Validation Modes (`mode="after"`):** Intercepting the data *after* Pydantic has successfully parsed and constructed the model instance. This allows you to interact with the fully typed object using standard dot notation (e.g., `model.age`).
*   **Complex Business Rules:** Enforcing conditional logic, such as requiring specific dictionary keys based on an integer threshold.

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic
* **Extensions:** `pydantic[email]`
## Code Example: Cross-Field Validation

```python
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
    contact: Dict[str, str]

    @model_validator(mode="after")
    def valid_emergency_contact(cls, model):
        # If the student is a minor, an emergency contact is mandatory
        if model.age < 18 and "emergency" not in model.contact:
            raise ValueError("Minor students must have an emergency contact")
        return model

def update_student_details(student: Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.contact)

student_info = {
    "name": "Dhruv", 
    "age": 15, 
    "email": "abc@gmail.com", 
    "contact": {"mobile": "12356790"}
}

# This will trigger a ValidationError because Dhruv is 15 but lacks an emergency contact.
student1 = Student(**student_info)
update_student_details(student1)

```

## How This Code Works (Step-by-Step Explanation)

1. **The `@model_validator` Decorator:** Unlike the field validator that targets a specific attribute by name, this decorator tells Pydantic to run this function against the *entire* dictionary or object being passed into the `Student` class.
2. **`mode="after"`:** Because we specified `after`, Pydantic first checks that `age` is an integer, `email` is a valid EmailStr, and `contact` is a dictionary. Once it builds the `Student` object, it passes that complete object into our function as the `model` variable.
3. **Cross-Field Logic (`valid_emergency_contact`):**
* The function evaluates the relationship between two entirely separate fields: `model.age` and `model.contact`.
* It checks if `model.age < 18`.
* If true, it then looks inside the `model.contact` dictionary for the key `"emergency"`.
* Since our dictionary only contains `{"mobile": "12356790"}`, the condition fails and a `ValueError` is raised.


4. **Returning the Model:** If the validation passes (for example, if Dhruv's age was 19, or if he had an `"emergency"` key), the function *must* `return model`. If you forget this return statement, Pydantic will wipe out your data and return `None`.
5. **Failing Loudly:** If you run this exact script, it will crash before `update_student_details` is ever called. Pydantic successfully catches that Dhruv is a minor missing his mandatory emergency contact, protecting your downstream functions from bad data.