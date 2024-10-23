
### Sequence:
A sequence is a general term for an ordered collection of items. Python sequences include lists, tuples, strings, ranges, and more. A list is a specific type of sequence that is mutable, meaning its contents can be changed after creation."""

### Hashing:
Hashing makes search faster. hashing makes the operation doesnt go sequentially instead it goes directly to the element. example when u are looking for 4 in a tuple (1,2,3,4,5), goes directly to elememt 4. all google indexes are hashed making the search faster. 
hashing works on immutable data type [ works on tupple and doesnt work on list].

*** for loop in general looks for iter and next. for loop stops when stop iteration is called *** 

### clear()

    l = [1, 2, 3, 4, 5]
    m = l
    l.clear()
    print(m)  # Output: []

    l = [1, 2, 3, 4, 5]
    m = l
    l = []
    print(m)  # Output: [1, 2, 3, 4, 5]

### Appending vs extending:

appending used for adding one element, extends add multiple element. 

    l = [1, 2, 3]
    l.append([4, 5])
    print(l)  # Output: [1, 2, 3, [4, 5]]

    l = [1, 2, 3]
    l.extend([4, 5])
    print(l)  # Output: [1, 2, 3, 4, 5]

    l = [1, 2, 3]
    l.extend((4, 5))
    print(l)  # Output: [1, 2, 3, 5, 4] #since it is set, the ordre is not guaranteed 


### pop 
Removes and returns an element from the list.
Default Behavior: If no index is specified, it removes and returns the last element.
Usage: list.pop([index])

    l = [1, 2, 3, 4, 5]
    last_element = l.pop()
    print(last_element)  # Output: 5
    print(l)  # Output: [1, 2, 3, 4]

    second_element = l.pop(1)
    print(second_element)  # Output: 2
    print(l)  # Output: [1, 3, 4]

### insert()
Function: Inserts an element at a specified position in the list.
Usage: list.insert(index, element)

    l = [1, 2, 3, 4, 5]
    l.insert(2, 'a')
    print(l)  # Output: [1, 2, 'a', 3, 4, 5]

### reverse()

This method modifies the list directly and does not return a new list.

    l = [1, 2, 3, 4, 5]
    l.reverse()
    print(l)  # Output: [5, 4, 3, 2, 1]

### Shallow Copy (copy)

 A shallow copy shares references to the same objects, while a deep copy creates entirely new objects.

 For non-nested objects like a simple list of integers, both copy() and deepcopy() will produce the same result because there are no nested objects to consider.

Usage: copy.copy(obj)
Behavior: Only the top-level structure of the object is copied. Nested objects are not copied; instead, references to the original nested objects are used.

    import copy

    original = [[1, 2, 3], [4, 5, 6]]
    shallow_copied = copy.copy(original)

    shallow_copied[0][0] = 99
    print("Original:", original)  # Output: [[99, 2, 3], [4, 5, 6]]
    print("Shallow Copied:", shallow_copied)  # Output: [[99, 2, 3], [4, 5, 6]]

### Deep Copy
 Creates a new object and recursively copies all objects found in the original.
 Usage: copy.deepcopy(obj)

    import copy

    original = [[1, 2, 3], [4, 5, 6]]
    deep_copied = copy.deepcopy(original)

    deep_copied[0][0] = 99
    print("Original:", original)  # Output: [[1, 2, 3], [4, 5, 6]]
    print("Deep Copied:", deep_copied)  # Output: [[99, 2, 3], [4, 5, 6]]


### List comprehension

    s = "hello"
    char_list = [char for char in s]
    print(char_list)
    
    #without list comprehension
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i*j)
        table.append(row)

    #with list comprehension
    table2 = [[i*j for j in range(1, 11)] for i in range(1, 11)]

    flattened_grades = [grade for sublist in grades for grade in sublist if grade >= 75]
    print(flattened_grades)


### range

range() generates numbers on the fly and doesn’t store them in memory, making it very memory efficient1. This is particularly useful when dealing with large sequences.


    for i in range(5):
        print(i) #Output: 0 1 2 3 4

    for i in range(1, 10, 2): #start, stop, step
        print(i) # Output: 1 3 5 7 9


The range() function in Python cannot be directly used with strings because it only works with integers.  you can use range() in conjunction with a loop to iterate over the indices of a string

    s = "hello"
    for i in range(len(s)):
        print(s[i])

### zip

The zip() function takes multiple iterables (like lists, tuples, etc.) and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.

        # Two lists
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    # Using zip()
    zipped = zip(list1, list2)

    # Converting to a list to see the result
    print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

### map()

The map() function applies a given function to all items in an input iterable (like a list) and returns an iterator of the results.

    # Function to square a number
    def square(x):
        return x * x

    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # Using map()
    squared_numbers = map(square, numbers)

    # Converting to a list to see the result
    print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

    ____________________________________

    # Traditional function
    def add(x, y):
        return x + y

    # Lambda function
    add = lambda x, y: x + y

    __________________________________


    numbers = [1, 2, 3, 4, 5]

    added = list(map(lambda x: x + 10, numbers))
    print(added)

### reduce():

is a **cummulative** function that Aggregates all elements in an iterable into a single value by applying a function cumulatively. Outputs single value and not list or sequence

    from functools import reduce

    # List of numbers
    numbers = [1, 3, 5, 2, 4, 6]

    # Using reduce() with a lambda function
    max_value = reduce(lambda x, y: x if x > y else y, numbers)

    print(max_value)  # Output: 6


    #for string

    from functools import reduce

    # Function to concatenate two strings
    def concat(x, y):
        return x + y

    # List of strings
    strings = ["Hello", " ", "World", "!"]

    # Using reduce() with the concat function
    concatenated_string = reduce(concat, strings)

    print(concatenated_string)  # Output: Hello World!

### lambda ():

**lambda arguments: expression**. 

    # Traditional function
    def add(x, y):
        return x + y

    # Lambda function
    add = lambda x, y: x + y

    __________________________________


    numbers = [1, 2, 3, 4, 5]

    added = list(map(lambda x: x + 10, numbers))
    print(added)

### repr():

Should return a string that ideally looks like a valid Python expression to recreate the object.

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age})"
    
    # Creating an instance of the Person class
    person = Person("Alice", 30)
    
    # Using repr() to get the string representation
    print(repr(person))  # Output: Person(name='Alice', age=30)

### named tuple:

A named tuple in Python is a subclass of tuples that allows you to access its elements using named fields instead of just index positions.



# 🌞🌞🌞 ALL ABOUT ITER AND NEXT 🌞🌞🌞: 

Python’s built-in iterators for lists, tuples, strings, etc., already have the __iter__() and __next__() methods implemented. 


### non custom class usage :
    The iter() function can be used outside of classes to create an iterator from any iterable object, such as lists, tuples, strings, and more. These iterators have the __iter__() and __next__() methods built-in.

    #example 1:
    my_list = [1, 2, 3]
    iterator = iter(my_list)

    print(next(iterator))  # Output: 1
    print(next(iterator))  # Output: 2
    print(next(iterator))  # Output: 3
    # If you call next(iterator) again, it will raise StopIteration

    #example 2:
    from collections import namedtuple

    def cast(data_type, value):
        if data_type == 'DOUBLE':
            return float(value)
        elif data_type == 'INT':
            return int(value)
        else:
            return str(value)
        
    def cast_row(data_types, data_row):
        return [cast(data_type, value) 
                for data_type, value in zip(data_types, data_row)]
        
    cars = []
    with open('cars.csv') as file:
        file_iter = iter(file)
        headers = next(file_iter).strip('\n').split(';')
        Car = namedtuple('Car', headers)
        data_types = next(file_iter).strip('\n').split(';')
        for line in file_iter:
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
            cars.append(car)
    cars[0]

### iterator and iterable:
*** An iterable is an object that return iterator ***. All the materials in the iterables should be predefined. 
An iterator must implement both __iter__() and __next__().
An iterable must implement __iter__(), which returns an iterator. you can iterate over iterable as many times , but iterator only once. 

    _SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    _RANKS = tuple(range(2, 11) ) + tuple('JQKA')
    from collections import namedtuple
    
    Card = namedtuple('Card', 'rank suit')
    
    class CardDeck:
        def __init__(self):
            self.length = len(_SUITS) * len(_RANKS)
    
        def __len__(self):
            return self.length
        
        def __iter__(self):
            return self.CardDeckIterator(self.length)
            
        class CardDeckIterator:
            def __init__(self, length):
                self.length = length
                self.i = 0
                
            def __iter__(self):
                return self
            
            def __next__(self):
                if self.i >= self.length:
                    raise StopIteration
                else:
                    suit = _SUITS[self.i // len(_RANKS)]
                    rank = _RANKS[self.i % len(_RANKS)]
                    self.i += 1
                    return Card(rank, suit)

    deck = CardDeck()
    for card in deck:  
    print(card)

### custom class usage:

When you create your own classes and want them to be iterable, you need to implement these methods yourself using __next__() and __iter__() inside your class. 


### __iter__():

usually __iter__() returns self making the entire instance of class iterable. The __iter__ method itself does not perform iteration; it simply returns an iterator. For the iteration to work, the returned iterator must implement the __next__ method. So __iter__() cannot work independentaly. When you create a custom class that represents a collection of items, implementing __iter__ allows you to use it in a for loop or any other context that expects an iterable.

### __next__():

The __next__ method is responsible for returning the next item in the sequence and raising a StopIteration exception when there are no more items. next can work independently. 

    if i need to iterate over instance of class using for loop then. i need iter.. but if i am calling instance of the class without using for loop using 
    
    # direct calls like below.

    class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result   
    
    def __len__(self):
        return self.length

    squares = Squares(5)

    # Using next() directly
    print(next(squares))  # Output: 0
    print(next(squares))  # Output: 1
    print(next(squares))  # Output: 4
    print(next(squares))  # Output: 9
    print(next(squares))  # Output: 16
    # The next call will raise StopIteration

    # iterating over instance of a class

    class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __iter__(self):
        self.i = 0  # Reset the counter
        return self
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result   
    
    def __len__(self):
        return self.length

    squares = Squares(5)
    for square in squares:
        print(square)


### ARGUMENTS OF A FUNCTION:

**positional_argument**: These parameters must be provided in the exact order they are defined in the function.  Use when the function has a small number of parameters and the order is intuitive.

    def add(a, b):
    return a + b
    # Calling the function with positional arguments
    result = add(2, 3)
    print(result)  # Output: 5


**named_argument**: Calling the function with keyword arguments. Use when the function has many parameters, or when the parameters are not immediately obvious in their order or purpose

    def add(a, b):
        return a + b

    result = add(a=2, b=3)
    print(result)  # Output: 5

# 🌞🌞🌞 GENERATORS 🌞🌞🌞🌞:

A generator object in Python is a special type of iterator that allows you to iterate over a sequence of values lazily, meaning it generates values on the fly and only when needed. This can be very memory efficient, especially when dealing with large datasets.A generator function is defined like a normal function but uses the **yield** statement to return values one at a time.

    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1

    # Create a generator object
    counter = count_up_to(5)

    # Iterate over the generator
    for num in counter:
        print(num)

### list comprehension vs generator

If you only need to iterate over the sequence once and want to save memory, use a generator expression. If you need to access the elements multiple times or perform operations that require the entire sequence, use a list comprehension.

    squares_gen = (x**2 for x in range(10))
    for square in squares_gen:
        print(square)
    # Trying to iterate again will yield no results
    for square in squares_gen:
        print(square)  # No output

    
    squares = [x**2 for x in range(10)]
    for square in squares:
        print(square)
    # You can iterate again
    for square in squares:
        print(square)  # Output: 0 1 4 9 16 25 36 49 64 81


Using a generator simplifies the implementation of the Deck class by eliminating the need to manually manage the __iter__ and __next__ methods.

    type: 1
        class Squaresss:
        def __init__(self, length):
            self.length = length
            # self.i = 0
        
        def __iter__(self):
            # self.i = 0  # Reset the counter
            for i in range(self.length):
                yield i ** 2

        squares = Squaresss(5)
        for square in squares:
            print(square)

    type 2:
        class Squares_sides:
        def __init__(self):
            self.sides = [2,4,5,7,8,9]
            # self.i = 0
        
        def __iter__(self):
            # self.i = 0  # Reset the counter
            for i in self.sides:
                yield i ** 2

        sq = Squares_sides()
        for square in sq:
            print(square)

# 🌞🌞🌞 LAZY ITERATOR 🌞🌞🌞:

* Using yield: Instead of returning a list, you use the yield keyword to return values one at a time. This makes the function a generator.
* No List Storage: Since values are generated on-the-fly, there’s no need to store them in a list, which saves memory.

* List Comprehension (Without Lazy Iterator)
    Memory Usage: The entire list is generated and stored in memory at once.
    Immediate Computation: All values are computed immediately when the list is created.
    Data Structure: The result is a list, which is a concrete data structure.

        squares = [x**2 for x in range(5)]

* Generator Expression (Using Lazy Iterator)
    Memory Efficiency: Values are generated one at a time and not stored in memory all at once. This is more memory-efficient, especially for large datasets.
    Lazy Evaluation: Values are computed on-the-fly as you iterate over them, rather than all at once.
    Data Structure: The result is a generator, which is an iterator that yields items one at a time.

        lazy_squares = (x**2 for x in range(5))
### Reading a file 
    # Without lazy iterator
    with open('large_file.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    # Using lazy iterator
    def read_file(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    
    for line in read_file('large_file.txt'):
        print(line)

### filtering even number

        # Without lazy iterator
    numbers = [x for x in range(10) if x % 2 == 0]
    print(numbers)

    # Using lazy iterator
    def even_numbers(n):
        for x in range(n):
            if x % 2 == 0:
                yield x
    
    for number in even_numbers(10):
        print(number)





    


# 🌞🌞🌞 UNDERSTANDING CLASS CALLING 🌞🌞🌞:

**attributes** : Attributes are variables that belong to an object or class. They are used to store data that is associated with an instance of a class.
**parameters** : Parameters are variables that are used in function or method definitions to accept input values. They are placeholders for the arguments that will be passed to the function or method.

Absolutely, I’d be happy to explain this concept in detail! When you call a class (let’s call it Class1) within another class (let’s call it Class2), you typically create an instance of Class1 inside Class2. This is a common practice in object-oriented programming and is known as composition. Here’s a step-by-step explanation:

    class Class1:
        def __init__(self, attribute1, attribute2):
            self.attribute1 = attribute1
            self.attribute2 = attribute2

    class Class2:
        def __init__(self, attribute3, attribute1, attribute2):
            self.attribute3 = attribute3
            self.class1_instance = Class1(attribute1, attribute2)

    instance_of_class2 = Class2(attribute3_value, attribute1_value, attribute2_value)

-------------------------------------------------------------------------------
    class Engine:
        def __init__(self, horsepower, type):
            self.horsepower = horsepower
            self.type = type
    
        def start(self):
            return "Engine started"
    
    class Car:
        def __init__(self, make, model, horsepower, engine_type):
            self.make = make
            self.model = model
            self.engine = Engine(horsepower, engine_type)
    
        def start_car(self):
            return f"{self.make} {self.model} with {self.engine.horsepower} HP {self.engine.type} engine: {self.engine.start()}"
    
        # Create an instance of Car
        my_car = Car("Toyota", "Camry", 301, "V6")
    
        # Access attributes and methods
        print(my_car.start_car())

### use of isinstance() inside class:

when u are unaware of what data comes inside the class and when u have any conditional range, where only if the data comes within particular range the class will function we check using isinstance... in other case , when u have control of what data comes inside u can directly initialize without checking

class MyClass:
    def __init__(self, data, threshold=10):
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if not isinstance(threshold, int) or threshold <= 0:
            raise ValueError("threshold must be a positive integer")
        
        self.data = data
        self.threshold = threshold

# 🌞🌞🌞 DECORATOR UNDERSTANDING 🌞🌞🌞:
### using get and setter method inside class also help of property decorator:

In the below class, we can see that width is initialized inside the init and also inside the setter method. this is because, initialization within the setter method helps to update the area automatically once the width is changed when isntance of class is called. 

Also one more advantages of get setter is, the validation happens properly... if u assign value that is non negative then it will throw error. while i tested if u do it using isinstance method like this 

    def __init__(self, r):
        if isinstance (r, int) and r > 0:
            self.radius = r
        else:
            raise ValueError('Radius must be positive')
    
    def area(self):
        return math.pi * self.radius ** 2   " it isnt working. 

    _______________________________________________________________________________________________________________________________________________________

    import math

    class Circle:
        def __init__(self, r):
            self.radius = r  # Calls the setter

        @property
        def radius(self):
            return self._radius

        @radius.setter
        def radius(self, r):
            if r <= 0:
                raise ValueError("Radius must be positive")
            self._radius = r
            self._area = math.pi * self._radius ** 2  # Automatically update area

        def area(self):
            return self._area

    # Usage
    c = Circle(1)
    print("radius", c.radius)  # Output: 1
    print(c.area())              # Output: 3.141592653589793

    c.radius = 10              # Automatically updates area
    print(c.radius)            # Output: 10
    print(c.area())              # Output: 314.1592653589793

### @property:

using @ property, u can simply call c.area in above code instead of c.area().

    @property
    def area(self):
        return self._area

    # Usage
    c = Circle(1)
    print("radius", c.radius)  # Output: 1
    print(c.area)              # Output: 3.141592653589793


    
### @static method : 
to call a method like area without creating an instance of the class, you would typically use a @staticmethod or @classmethod

    import math

    class Circlec:
        def __init__(self, r):
            self.radius = r

        @property
        def radius(self):
            return self._radius

        @radius.setter
        def radius(self, r):
            if r <= 0:
                raise ValueError("Radius must be positive")
            self._radius = r
            
        def area(self):
            return math.pi * self.radius ** 2

        @staticmethod
        def calculate_area(radius):
            if radius <= 0:
                raise ValueError("Radius must be positive")
            return math.pi * radius ** 2

    # Usage
    c = Circlec(5)
    print(c.radius)  # Output: 5
    print(c.area())  # Output: 78.53981633974483

    # Calling the static method without creating an instance
    print(Circlec.calculate_area(5))  # Output: 78.53981633974483


# 🌞🌞🌞 MAGIC METHODS INSIDE CLASSES 🌞🌞🌞:

### Usage of __eq__() and __gt__():

The other parameter represents the instance you are comparing your current instance (self) to

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return (self._n == other._n and self._R == other._R)
        else:
            return NotImplemented
    def __gt__(self,other):
        if isinstance(other, Polygon):
            return (self._n > other._n)
        else:
            return NotImplemented

    poly1 = Polygon(3, 10)
    poly2 = Polygon(4, 5)
    poly3 = Polygon(3, 10)
    print(poly1 == poly2)
    print(poly1 == poly3)
    print(poly1 > poly2)

### __len__():

This method returns the number of polygons in the Polygon_sequence instance. since __len__(), __next__() are all inbuilt methods of a class when calling it we dont have to call it as class.len instead we can directly call the len. 

    polygon_seq = Polygon_sequence(5)
    print(len(polygon_seq))  # Output: 3

### __getitem__():

The __getitem__ method allows an instance of your class to support indexing, like a list or tuple. This method should return the item at the specified index.
The __getitem__ method allows an object to use the indexing syntax (obj[key]) to retrieve items. __getitem__ and __len__ together is an alternative of __iter__ and __next__


    def __getitem__(self, index):
    return self.polygons[index]

    polygon_seq = Polygon_sequence(5)
    print(polygon_seq[0])  # Output: Polygon with 3 vertices and circumradius 10

    polygon_seq[0] returns the first polygon in the sequence.

### __init__(): 

1. **Attributes Used Across Methods:**
        Initialize: If an attribute is used in multiple methods, it should be initialized in the __init__ method. This ensures that the attribute is available and has a defined state whenever it is accessed.
2. **Attributes Representing State:**
        Initialize: Attributes that represent the state of an object should be initialized. This includes attributes that track the status, configuration, or any other state-related information.
        Example: self.file represents the state of the file being open or closed.
3. **Attributes with Default Values:**
        Initialize: If an attribute has a default value or needs to be set to a specific initial state, it should be initialized in the __init__ method.
        Example: self.file = None ensures that the file attribute starts in a known state.
4. **Configuration Attributes:**
        Settings: Configuration options that affect the object’s behavior (e.g., timeout, max_retries).
        Parameters: Values that customize the object’s functionality (e.g., threshold, mode).
5. **Attributes That Are Optional:**
        Initialize: If an attribute is optional and may not always be set, it should still be initialized to a default value (e.g., None) to avoid AttributeError.
        Example: self.reader and self.Row are initialized to None because they are set up later in the __enter__ method.
6. **References to Other Objects:**
        Dependencies: Other objects that this object interacts with (e.g., a database connection, a logger).


### ALL ABOUT ITER AND NEXT: 

Python’s built-in iterators for lists, tuples, strings, etc., already have the __iter__() and __next__() methods implemented. 

##### non custom class usage :
    The iter() function can be used outside of classes to create an iterator from any iterable object, such as lists, tuples, strings, and more. These iterators have the __iter__() and __next__() methods built-in.

    #example 1:
    my_list = [1, 2, 3]
    iterator = iter(my_list)

    print(next(iterator))  # Output: 1
    print(next(iterator))  # Output: 2
    print(next(iterator))  # Output: 3
    # If you call next(iterator) again, it will raise StopIteration

    #example 2:
    from collections import namedtuple

    def cast(data_type, value):
        if data_type == 'DOUBLE':
            return float(value)
        elif data_type == 'INT':
            return int(value)
        else:
            return str(value)
        
    def cast_row(data_types, data_row):
        return [cast(data_type, value) 
                for data_type, value in zip(data_types, data_row)]
        
    cars = []
    with open('cars.csv') as file:
        file_iter = iter(file)
        headers = next(file_iter).strip('\n').split(';')
        Car = namedtuple('Car', headers)
        data_types = next(file_iter).strip('\n').split(';')
        for line in file_iter:
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
            cars.append(car)
    cars[0]

##### custom class usage:

When you create your own classes and want them to be iterable, you need to implement these methods yourself using __next__() and __iter__() inside your class. 


# __iter__():

usually __iter__() returns self making the entire instance of class iterable. The __iter__ method itself does not perform iteration; it simply returns an iterator. For the iteration to work, the returned iterator must implement the __next__ method. So __iter__() cannot work independentaly. When you create a custom class that represents a collection of items, implementing __iter__ allows you to use it in a for loop or any other context that expects an iterable.

# __next__():

The __next__ method is responsible for returning the next item in the sequence and raising a StopIteration exception when there are no more items. next can work independently. 

    if i need to iterate over instance of class using for loop then. i need iter.. but if i am calling instance of the class without using for loop using 
    
    # direct calls like below.

    class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result   
    
    def __len__(self):
        return self.length

    squares = Squares(5)

    # Using next() directly
    print(next(squares))  # Output: 0
    print(next(squares))  # Output: 1
    print(next(squares))  # Output: 4
    print(next(squares))  # Output: 9
    print(next(squares))  # Output: 16
    # The next call will raise StopIteration

    # iterating over instance of a class

    class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __iter__(self):
        self.i = 0  # Reset the counter
        return self
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result   
    
    def __len__(self):
        return self.length

    squares = Squares(5)
    for square in squares:
        print(square)

    
# 🌞🌞🌞 ITERATING CLASS INSIDE A CLASS 🌞🌞🌞:

Steps:
**Define the Iterable Class:**
    1. This class should contain the data you want to iterate over. [stores the list of cities]
    2. Implement the __iter__ method to return instance of the iterator object. []
    3.  can optionaly have __len__
**Define the Iterator Class:**
    1. stores reference to iterable object and initialized index
    2. The __iter__ method should return self.
    3. The __next__ method should define how to retrieve the next item and raise StopIteration when there are no more items.

 *** An iterable is an object that returns an iterator ***



# 🌞🌞🌞 CONTEXT MANAGER 🌞🌞🌞:
###### Contextmanager module from contextlib
The @contextmanager decorator from the contextlib module allows you to convert a regular function into a context manager. This can be very convenient because it simplifies the creation of context managers, making your code more readable and maintainable.  Apply the @contextmanager decorator to the function to convert it into a context manager.

How It Works
    Define a Generator Function:
    The function should use the yield statement to separate the setup and teardown code.
    The code before yield is executed when entering the context.
    The code after yield (typically in a finally block) is executed when exiting the context.
    Use the @contextmanager Decorator:
  
Here’s a simple example to illustrate:

Regular Function
Let’s say you have a regular function to open and close a file:

    def open_file(fname):
        file = open(fname, 'r')
        try:
            # Perform file operations
            pass
        finally:
            file.close()

Converted to Context Manager
Using the @contextmanager decorator, you can convert this function into a context manager:

    from contextlib import contextmanager
    @contextmanager
    def open_file(fname):
        file = open(fname, 'r')
        try:
            yield file
        finally:
            file.close()

    with open_file('example.txt') as f:
        for line in f:
            print(line)

###### Use of YIELD:

In the context of @contextmanager, yield is used to provide a value (or values) to the with block.
The code before yield is executed when entering the context, and the code after yield (typically in a finally block) is executed when exiting the context.This allows the code inside the with block to access both the reader for iterating over the rows and the named tuple class for converting rows into named tuples.

### Context Managers in Python

> context manager create module or area where we do our stuffs and get rid of it. 
> whatevre is done inside context manager , will be there as long as context is there and the moment we are out of context all the new objects created inside context manager will be gone and will be back to default
> Context manager can be used alternatively for try except and finally. 

contxt manager used for below cases by default:

  > 1. open and close conenction 
  > 2. Lock and release (Blocking a memory and then release it)
  > 3. change and reset (flags used, counters, float16 used within bloack and go back to float32 which is default)
  > 4. enter and exits (entering a particular logging, flag and then reset)
  > 5. start and stop (timer)


### _enter_ _exit_:


### Practical example of why context manager is essential: we need to run ML model in cloud AWS. AWS charges as long as GPU is live. If we push file to AWS , and if  say the file crashes and if we do not close the connection and then AWS charges


🌞🌞🌞 HASHING and DICTIONARY🌞🌞🌞 :

1) anything that is immutable is hashed and anything that can be hashed  can become key of dictionary. It can be tuple, string or a function or anything that is immutable 
        example : a = {('a',100):['a','b','c'], 'key2': ('a',100):[1,2,3]}

        def fn_add (a,b):
            return a+b
        funcs_dic = {fn_add:(10,20) , fn_inv(2,)}

        for f in funcs:
        print

# creating dictionary:
    ### method 1:
        key = ['fn_add', 'fn_inv', 'fn_mult']
        values = ((10,20), (2,), (2,8))
        funcs = dict(zip(key, values))

        d ={}
        for key , values in zip(key, values):
            d[key] = values
    
    ### method 2:

        counters = dict.fromkeys(['a', 'b', 'c'], 0)
        
        
    ### method 3:

        d = dict(zip('abc', range(1,4)))
        

    """ Note: if you are accessing a key of the dictionary and if the key is not present in the dictionary, it will throw an error. To avoid this, 
    try d = d.pop('a', 0) which will return 0 if the key is not present in the dictionary. If the key is present, it will return the value of the key.
    d = d.get('a', 0) will also return 0 if the key is not present in the dictionary. If the key is present, it will return the value of the key."""
    
    """
        d = {'a': 1, 'b': 2, 'c': 3}
        d.pop('a', 0) # 1 #returns the value of the key and deletes the key
        del d['a'] # doesnt return value just deletes
        d.popitem() # removes the last item from the dictionary. It returns the key and value of the last item including key and value
        d.clear() # clears the dictionary
        
    """

# accessing dictionary:
        def fn_add(a, b):
            return a + b

        def fn_inv(a):
            return 1/a

        def fn_mult(a, b):
            return a * b
        funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
        for f in funcs:
            print("f",f) #function fn_add, fn_inv, fn_mult
            print("funcs[f]",funcs[f]) #values of the key of the function fn_add, fn_inv, fn_mult
            print("f(*funcs[f])",f(*funcs[f])) #calling the function with the values of the key , * is used to unpack the tuple
            result = f(*funcs[f])
            print(result)
    
        ### method 2:

        for key, values in funcs.items():
            result = key(*values)
            print(result)
            
        ### method 3:
        d = {'a': 1, 'b': 2, 'c': 3}
        d.get('a') # 1
                    
        
   
# similar to list comprehension, we can also make dictionary comprehension

list_comp = [i**2 for i in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

dict_comp = {i: i**2 for i in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

dict_comp = {k:v for k,v in zip(key, values) if v %2 == 0}


# nested list comprehension

x_i = (1,2,3,4)
y_i = (5,6,7,8)

result = [(x,y) 
          for x in x_i
          for y in y_i]
print(result)


# iterating over and creating dictionary:
    ### method 1:
        text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'
        counts = dict()
        for c in text:
            c = c.lower().strip()
            if c:
                counts[c] = counts.get(c, 0) + 1
        print(counts)

    ### method 2:
        from collections import defaultdict
        counts_Def = defaultdict(int)
        for c in text:
            counts_Def[c] += 1
        print(counts_Def)
        
    ### method 3:

        count_setdef = {}
        for c in text:
            c = c.lower().strip()
            if c:
                count_setdef[c]=count_setdef.setdefault(c, 0)+1
        print(count_setdef)
        

#### example usage:

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
                

# inserting into dictionary:

    ### method 1:
          
        d = {'a': 1, 'b': 2, 'c': 3}
        res_d = d.setdefault('d', 4) 
        # if the key is not present in the dictionary, it will insert the key and value into the dictionary and return the value of the key
        
# updating dictionary:

        d1 = {'a': 1, 'b': 2}
        d1.update(b=20, c=30)
        print(d1)
        
        d1.update((key,ord(key)) for key in 'abc') # ord get the ascii value of the key
        

# combining two dictionaries:

        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        d = {**d1, **d2}
        print(d)
        
        
        ### example 2:
        
        conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
        print(conf_defaults)

        conf_global = {
            'port': 5432,
            'database': 'deepdive'}

        conf_dev = {
            'host': 'localhost',
            'user': 'test',
            'pwd': 'test'
        }

        conf_prod = {
            'host': 'ironman.aws.com',
            'user': '$prod_user',
            'pwd': '$prod_pwd',
            'database': 'deepdive_prod'
        }

        config_dev = {**conf_defaults, **conf_global, **conf_dev}
        config_dev

        config_prod = {**conf_defaults, **conf_global, **conf_prod}
        config_prod
        
    


