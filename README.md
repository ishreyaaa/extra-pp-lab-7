# Practical 7: Python Function Arguments

# Aim & Objective

* Aim:To write a Python program that demonstrates the use of different types of function arguments, including positional, keyword, default, and variable-length arguments, and to understand their usage through examples[span_0](start_span)[span_0](end_span).
* **Objective:** To create user-defined functions in Python with different types of function arguments to build flexible and reusable components[span_1](start_span)[span_1](end_span).


# Theory & Concepts Covered

Python functions can accept various types of arguments to allow for flexible and dynamic definitions[span_2](start_span)[span_2](end_span). This project covers the following four main types:

1. *Positional Arguments:** The most common type where values are passed to the function in the exact order they are defined[span_3](start_span)[span_3](end_span).
2. *Keyword Arguments:** Arguments passed by explicitly naming each parameter, allowing you to bypass strict ordering[span_4](start_span)[span_4](end_span).
3. *Default Arguments:** Arguments that have a predefined default value in the function definition. If the function is called without this argument, the default value is used[span_5](start_span)[span_5](end_span).
4. *Variable-Length Arguments:** Allows functions to handle a variable number of arguments using `*args` (non-keyword arguments) and `**kwargs` (keyword arguments)[span_6](start_span)[span_6](end_span).

#Source Code Overview

The repository includes implementations of the following functions[span_7](start_span)[span_7](end_span):
* `add(a, b)`: Demonstrates positional arguments.
* `greet(first_name, last_name)`: Demonstrates keyword argument usage.
* `power(base, exponent=2)`: Demonstrates default arguments.
* `multiply(*args)`: Demonstrates variable-length non-keyword arguments.
* `describe_person(**kwargs)`: Demonstrates variable-length keyword arguments.

# Conclusion
This program demonstrates the use of different function types in Python, allowing for more flexible and adaptable code. Positional arguments are straightforward and rely on order, while keyword arguments improve readability[span_8](start_span)[span_8](end_span). Default arguments add versatility, and variable-length arguments (`*args` and `**kwargs`) enable functions to accept an arbitrary number of inputs, enhancing code scalability and reusability[span_9](start_span)[span_9](end_span).
