# Learning Pydantic (Serialization): Day 7

![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 7 focuses on **Serialization**, which is the process of converting your validated Pydantic objects back into standard Python dictionaries or JSON strings so they can be sent to APIs, databases, or front-end applications.

## Serialization Overview

Once your data is safely inside a Pydantic model, you eventually need to get it out. Pydantic provides highly flexible built-in methods for exporting data. Key features explored include:

* **Dictionary Export (`model_dump`):** Converts the nested model object back into a standard Python dictionary.
* **JSON Export (`model_dump_json`):** Converts the model directly into a valid JSON string, ready for HTTP responses.
* **Targeted Filtering (`include` / `exclude`):** Allows you to selectively export only the exact fields you need, protecting sensitive data (like passwords) from being serialized.
* **Default State Management (`exclude_unset`):** A powerful flag that exports only the data explicitly provided by the user, ignoring any fields populated by fallback default values.

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic

## Code Example: Serialization and Filtering

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int

class Student(BaseModel):
    name: str
    age: int
    gender: str = "Male"
    address: Address

# Notice we pass a raw nested dictionary for the address instead of an Address object
student_info = {"name": "Vivek", "age": 24, "address": {"city": "Khurja", "state": "Uttar Pradesh", "pin": 203131}}
student1 = Student(**student_info)

temp = student1.model_dump()
print(temp)
print(type(temp))

# To Get JSON of data
temp1 = student1.model_dump_json()
print(temp1)
print(type(temp1))

# Getting only selected data in JSON or anywhere
# Only includes asked data
temp3 = student1.model_dump(include=["name", "age"]) 
print(temp3)

# Only exclude asked data
temp4 = student1.model_dump(exclude=["name", "age"]) 
print(temp4)

# Excludes those data which have default values and not given by user
temp5 = student1.model_dump(exclude_unset=True) 
print(temp5)

```

## How This Code Works (Step-by-Step Explanation)

1. **Automatic Nested Parsing:** Building on Day 6, notice that we pass a raw dictionary `{"city": "Khurja", ...}` directly into the `address` field of `student_info`. Pydantic automatically detects this and instantiates the nested `Address` model for us.
2. **`model_dump()` (To Dictionary):** This method takes the validated `student1` object and converts it—and all its nested models—back into a standard Python `<class 'dict'>`.
3. **`model_dump_json()` (To JSON):** This converts the model into a standard JSON `<class 'str'>`. This is incredibly useful in frameworks like FastAPI when you need to return a text-based JSON response over the internet.
4. **Targeted Export (`include` & `exclude`):**
* Passing `include=["name", "age"]` forces Pydantic to ignore everything else and export *only* those two fields.
* Passing `exclude=["name", "age"]` does the exact opposite, exporting the `address` and `gender` but stripping out the name and age.


5. **Smart Defaults (`exclude_unset=True`):** In the model definition, `gender` is given a default value of `"Male"`. Because the `student_info` dictionary did not explicitly contain a `"gender"` key, Pydantic populated it automatically. By passing `exclude_unset=True`, Pydantic will strip `"gender"` from the export, returning only the raw data that was intentionally set by the user upon creation.