![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

# Learning Pydantic: Day 1

This repository tracks my progress in learning and implementing **Pydantic** for data validation. It serves as a personal reference for revisiting core concepts and code snippets.

## Why to use Pydantic?

Pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. Key benefits include:

*   **Data Validation:** Guarantees that data structures match the defined schema and fails loudly when they do not.
*   **Automatic Type Coercion:** Intelligently converts input types (e.g., parsing the string `"123"` into the integer `123`) when safe to do so.
*   **IDE Integration:** Built on standard Python type hints (`typing`), providing excellent autocompletion in editors.
*   **Less Boilerplate:** Eliminates the need for custom `__init__` methods and manual type-checking `if/else` statements.

## Code Example: Student Data Validation

```python
from pydantic import BaseModel
from typing import List, Dict

class Students(BaseModel):
    name: str
    roll_no: int
    total_marks: int
    passed: bool
    subjects: List[str]
    sub_marks: Dict[str, int] # Dict[key, value]
    contact_details: dict[str, str]

def update_details(student: Students):
    print(student.name)
    print(student.roll_no)
    print(student.contact_details)
    print(student.subjects)
    print(student.sub_marks)
    print(student.total_marks)
    print(student.passed)

student_info = {
    "name": "Vivek",
    "roll_no": 123456,
    "subjects": ["English", "Physics", "Chemistry"],
    "sub_marks": {"English": 75, "Physics": 80, "Chemistry": 70},
    "total_marks": 225,
    "passed": True,
    "contact_details": {"mobile": "1234567890", "email": "abc@gmail.com"}
}

student1 = Students(**student_info)
update_details(student1)

```

## How This Code Works (Step-by-Step Explanation)

1. **`BaseModel` is the Engine:** By making the `Students` class inherit from `BaseModel` (`class Students(BaseModel):`), we give standard Python class superpowers. Pydantic takes over the class creation process to validate data automatically.
2. **Strict Type Hinting:** We define exact data types for every variable.
* `name: str` ensures the name is a string.
* `sub_marks: Dict[str, int]` is specifically powerful: it ensures that inside the dictionary, every key (subject) is a string and every value (marks) is an integer.


3. **Dictionary Unpacking (`**`):** When we call `Students(**student_info)`, the `**` operator unpacks the dictionary. It translates the dictionary into keyword arguments, passing it to the class like this: `Students(name="Vivek", roll_no=123456, ...)`.
4. **The Validation Phase:** Before the `student1` object is actually created, Pydantic intercepts the data and checks it against our type hints.
* If we accidentally passed `"Vivek"` as the `roll_no`, Pydantic would instantly crash the script with a `ValidationError` instead of letting the bug pass through silently.


5. **Dot Notation Access:** Because Pydantic creates a true Python object (not just a dictionary), the `update_details` function can access the data cleanly using dot notation (e.g., `student.name` instead of `student["name"]`), which enables IDE autocompletion.

## Tech Stack & Running the Code

* **Language:** Python 3.11
* **Package Manager:** uv
* **Core Library:** Pydantic

## Running the Code Locally

You can set up the environment and run the code locally using `uv`:

```bash
# 1. Create a virtual environment using Python 3.11
uv venv --python 3.11

# 2. Activate the virtual environment
# On Windows:
# .venv\Scripts\activate

# 3. Install Pydantic into the virtual environment
uv pip install pydantic

# 4. Run the script (assuming the file is named main.py)
python main.py

```