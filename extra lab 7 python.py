# Function with Positional Arguments
def add(a, b):
    return a + b

# Function with Keyword Arguments
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

# Function with Default Arguments
def power(base, exponent=2):
    return base ** exponent

# Function with Variable-Length Arguments (*args)
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Function with Variable-Length Keyword Arguments (**kwargs)
def describe_person(**kwargs):
    description = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    return f"Person details: {description}"

# Calling the functions #
# Positional Arguments
sum_result = add(5, 10)

# Keyword Arguments
greeting = greet(first_name="John", last_name="Doe")

# Default Arguments
square = power(5)
cube = power(5, 3)

# Variable-Length Arguments (*args)
product = multiply(2, 3, 4)

# Variable-Length Keyword Arguments (**kwargs)
person_description = describe_person(name="Alice", age=30, city="New York")

# Output
print("Sum:", sum_result)
print("Greeting:", greeting)
print("Square:", square)
print("Cube:", cube)
print("Product:", product)
print(person_description)