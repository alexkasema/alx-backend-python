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
## 2-floor.py
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
## 3-to_str.py
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
## 4-define_variables.py
Define and annotate the following variables with the specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”
## 5-sum_list.py
A type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
## 6-sum_mixed_list.py
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
## 7-to_kv.py
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
## 8-make_multiplier.py
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
## 9-element_length.py
Annotate the below function’s parameters and return values with the appropriate types
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
def element_length(lst):
    return [(i, len(i)) for i in lst]
## 100-safe_first_element.py
Augment the following code with the correct duck-typed annotations:
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
### The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None	
## 101-safely_get_value.py
Given the parameters and the return values, add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
### Here's what the mappings should look like
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
## 102-type_checking.py
Use mypy to validate the following piece of code and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
