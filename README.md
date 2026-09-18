# Learning Pydantic: A 7-Day Journey

![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

Welcome to the main repository! This project tracks my step-by-step progress in learning and implementing **Pydantic V2**. Each folder (`day1` through `day7`) contains functional code examples and dedicated READMEs explaining specific core concepts.

## What is Pydantic and Why Use It?

Pydantic is the most widely used data validation library for Python. It uses standard Python type hints to parse, validate, and serialize data. Instead of writing endless `if/else` statements to check if your data is correct, Pydantic handles it automatically.

Key benefits include:
*   **Guaranteed Data Structures:** It ensures your data matches the exact schema you define and fails loudly (with detailed errors) when it doesn't.
*   **Automatic Type Coercion:** It intelligently converts input types when safe (e.g., parsing a string `"123"` into an integer `123`), while allowing strict modes when you need exact matches.
*   **Complex Validation Rules:** Easily enforce granular constraints (like string length or numeric boundaries) and custom business logic across multiple fields.
*   **Painless Serialization:** Effortlessly convert complex, nested Python objects back into clean dictionaries or JSON for APIs.
*   **World-Class Developer Experience:** Because it relies on standard `typing`, it integrates perfectly with IDEs to provide robust autocompletion and linting.

## Repository Structure & Curriculum

This repository is structured as a 7-day curriculum, moving from the absolute basics to advanced data manipulation:

*   **[Day 1: The Basics (`BaseModel`)](./day1)**
    Introduction to core type hinting, creating basic models, and understanding how Pydantic handles dictionary unpacking and validation.
*   **[Day 2: Advanced Data Validation (`Field` & `Annotated`)](./day2)**
    Enforcing strict constraints (max length, numeric boundaries), handling optional data, and using specialized types like `EmailStr`.
*   **[Day 3: Custom Field Validation (`@field_validator`)](./day3)**
    Injecting custom Python logic to validate individual fields (e.g., checking specific email domains) and intercepting raw data before it gets parsed.
*   **[Day 4: Cross-Field Validation (`@model_validator`)](./day4)**
    Validating the entire object as a whole to enforce complex business rules that depend on the relationship between multiple different fields.
*   **[Day 5: Computed Fields (`@computed_field`)](./day5)**
    Dynamically generating read-only fields on the fly based on the values of other inputs, and ensuring they are included in data exports.
*   **[Day 6: Nested Models](./day6)**
    Composing multiple Pydantic models together to handle deeply nested, complex JSON structures efficiently.
*   **[Day 7: Serialization](./day7)**
    Exporting validated objects back to dictionaries or JSON, including targeted filtering (`include`/`exclude`) and managing default states.

## Tech Stack

*   **Language:** Python 3.11
*   **Package Manager:** uv
*   **Core Library:** Pydantic (V2)
*   **Extensions:** `pydantic[email]`