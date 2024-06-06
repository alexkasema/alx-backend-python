# Python - Variable Annotations
def moon_weight(earth_weight: float) -> str:
    return f'On the moon, you would weigh {earth_weight * 0.166} kilograms.'```
In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.
## 0-add.py
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
## 1-concat.py
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.
