# Learning Pydantic (Nested Models): Day 6
![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

This repository tracks my progress in learning and implementing **Pydantic** for data validation. Day 6 focuses on **Nested Models**, which allow you to build complex, deeply nested JSON structures by composing multiple Pydantic models together.

## Nested Models Overview

Real-world data is rarely flat. APIs usually return objects inside other objects (e.g., a user profile containing a nested address object). Key features explored include:

* **Model Composition:** Using one Pydantic model as a type hint inside another Pydantic model.
* **Modularity & Reusability:** Grouping related fields (like city, state, pin) into their own model so they can be reused across different parts of an application (e.g., using the same `Address` model for a `Student`, a `Teacher`, or a `School`).
* **Deep Dot Notation:** Accessing deeply nested data cleanly without chaining cumbersome dictionary keys (e.g., bypassing `dict["address"]["pin"]`).

## Tech Stack

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic

## Code Example: Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int

class Student(BaseModel):
    name: str
    age: int
    gender: str
    address: Address  # <--- Using the Address model as a type hint

address_dict = {"city": "Khurja", "state": "Uttar Pradesh", "pin": 203131}
address1 = Address(**address_dict)

student_dict = {"name": "Vivek", "age": 24, "gender": "Male", "address": address1}
student1 = Student(**student_dict)

print(student1)

# Getting address info 
print(student1.address.pin) # we can use dot . instead of [] 
print(student1.address.state)
print(student1.address.city)

```

## How This Code Works (Step-by-Step Explanation)

1. **Defining the Sub-Model (`Address`):** Before building the main student profile, we define a smaller, standalone `BaseModel` to handle physical locations. This ensures any location data strictly contains a city, state, and pin code.
2. **Model Composition (`address: Address`):** Inside the `Student` model, the `address` field is heavily restricted. By setting its type hint to the `Address` class, Pydantic guarantees that the student's address will perfectly match the structure we defined in step 1.
3. **Staged Instantiation:**
* First, the code unpacks the `address_dict` to create an isolated `address1` object.
* Then, that fully validated `address1` object is injected into the `student_dict` to build the complete `student1` record.
* *(Note: Pydantic is smart enough that you could also just pass the raw nested dictionary directly, like `"address": {"city": "Khurja", ...}`, and it would automatically build the `Address` object for you!)*


4. **Dot Notation Navigation:** Because Pydantic converts these dictionaries into rich Python objects, you can chain dot notation to navigate the nested data. Writing `student1.address.pin` is significantly cleaner, safer, and more IDE-friendly (providing autocomplete) than navigating raw Python dictionaries using bracket notation like `student1["address"]["pin"]`.