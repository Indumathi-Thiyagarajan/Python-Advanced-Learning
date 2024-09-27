### Expand the README file to explain the code and how to run it. Here is an example of what is expected:
import text_toolkit as tt

### Example usage:
freq = tt.word_frequency('example.txt')
print(freq)

unique = tt.unique_words('example.txt')
print(unique)

cooccurrence_matrix = tt.word_cooccurrence_matrix('example.txt')
print(cooccurrence_matrix)

### Example of using the text generator
for line in tt.text_generator('example.txt'):
    print(line)

# UNDERSTANDING OF MODULE AND PACKAGES
In Python, a module is essentially a file containing Python code. Modules can define functions, classes, and variables, and can also include runnable code. They help in organizing code logically and can be reused across different programs.

### first lets create a module named math_operations.py

    #math_operations.py

    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    pi = 3.14

### using module in other scripts

    import math_operations
    print(math_operations.add(5,3))
    print(math_operations.subtracts(5,3))
    print(math_operations.pi)

Package is a collection of modules organized in directories that provide a hierarchial structure. It contains an __init__.py file to indiciate that the directory is a package, along with multiple modules files. 

    geometry/
    __init__.py
    circle.py
    rectangle.py

### lets create a init module gemotery/__init__.py

    from .circle import area_of_circle
    from .rectangle import area_of_rectangle 


### module geometry/circle.py
    def area_of_circle(radius):
        pi = 3.14
        return pi*(radius**2)


### lets create rectangle.py
def area_of_rectangle(length, width):
    return length * width


### using package in other script 

    import geometry
    print(geometry.area_of_circle(5))
    print(gemoetry.area_of_rectangle(4,6))
