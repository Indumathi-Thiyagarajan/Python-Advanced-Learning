
## Everything is an object
- Every entity in Python, from integers to classes, is an object with a unique memory address, making it easy to assign, pass, or return from functions.
- When we are assigning a=6 its not a being assigned to 6. Its just that a is pointing to memory address where a is stored. 
- **Interning:** Python optimizes memory usage by reusing the same memory location for small integers (-5 to 256) and frequently used strings upto 4096 char length.
- **Parameters** belong to methods (inside the class).
- **Attributes** belong to the instance (object) of the class.
- **Functions** are independent and do not belong to a class.
- **Methods** are functions inside a class and must be called with an instance.
- **class** is a blueprint for creating objects. It defines attributes (variables) and methods (functions inside the class).
- **Module** is a file that is stored in python memory that can be imported. It can also be a .py file stored manually by you in your working environment.
  
## Immutability and Mutability
- **Immutable:** Tuples, strings, and integers. Immutable objects can’t be changed after creation, making them fast and ideal for constant values in multimedia/games.
- **Mutable:** Lists. These can be modified after creation. For mutable objects, any modification affects the original object directly when passed into a function.
- **Unsubcriptable:** Sets are unsubsriptible , in the process of keep non duplicate unique values inside, it changes the index of object inside so making it unsubscriptble

## Data Structures
categorized as linear and non-linear structures.

1️⃣ Linear Data Structures

    List (list) – Ordered, mutable, allows duplicates.  
    Tuple (tuple) – Ordered, immutable, allows duplicates.
    String (str) – Ordered, immutable sequence of characters.
    Stack (list or collections.deque) – Follows LIFO (Last In, First Out).
    Queue (collections.deque or queue.Queue) – Follows FIFO (First In, First Out).

2️⃣ Non-Linear Data Structures

    Set (set) – Unordered, mutable, unique elements.
    Dictionary (dict) – Key-value pairs, ordered (since Python 3.7+), mutable.
    Graph (dict with lists/sets) – Nodes and edges representation.
    Tree (Custom implementation) – Hierarchical structure with parent-child relationships.
  
## Python Behavior (Pass by Object Reference)
Python behavior is pass by object references. Variables are references to objects in memory. When passing arguments to functions, you're passing these references. 

1️⃣ Immutable objects ( str, int and tuple), these behaves like pass by value behaviour. So any modification creates a new object, leaving the original unchanged. But when u are assigning the fucntion to a new variable it creates a new object, so then it wil change.before and after function prints same number, the num variable is unchange. But when u assign it to new varibale ass it becomes new object and get new value assigned. 
          
    def modify_integer(x):
        x += 1
        print(f"Inside function: {x}")
        return x
    num = 5
    print(f"Before function: {num}")
    modify_integer(num)
    print(f"After function: {num}")
    ass = modify_integer(num)
    print(f" assigning integer: {ass}")                                      
                        
2️⃣ For mutable objects, modifications affect the original object directly. 

    def modify_list(lst):
      lst.append(4)
      print(f"Inside function: {lst}")
  
    my_list = [1, 2, 3]
    print(f"Before function: {my_list}")
    modify_list(my_list)
    print(f"After function: {my_list}")

## Why hashing is helpful ?
Sequence referes to list, tuple, string, range where the items are ordered. So when we search an item that is sequence it goes from 0th index to the item index. if there is million records its time consuming, so hashing is useful
Hashing is the process of converting an input (like a string, file, or data) into a fixed-length string of characters using a mathematical function. Hashing speeds up the process. Hashing is used when encoding is expensive like one hot enocding, storing hashing of passwords and senstive information instead of plain text for security, in a larger dataset to find duplicates or to search data instead of raw data if we hash and look up its faster. One thing to note is hashing is one way operation so u have to hash partial data like unique id's or store hashed data and raw input somewhere to look up. Hash value u same all the time for same input. so u can match hashes. 

## All about Iterators:
Iterators travers over a sequence one element at a time. They dont store entire sequence in memory. Iterator must have __iter__() and __next__(). 

- **Iterable** is an object that stores values and can be looped over. even though iterable has iter , it needs __iter__() to convert it to iterator. We can use next over the new iterator object and loop over. Iterable can be looped over in one of below methods
  1️⃣ Convert it into an iterator using iter() → then use next() manually.
  2️⃣ Use a for loop, which automatically calls iter() and next() in the background.
  
- **Iterator** is an object that do not store and produces one value at a time. this is memory efficient. Needs both __iter__() and __next__().

One of the major difference between using iterable and iterator is that, once the iterator ends u have to create a new object again and then loop over. example. 

    # Create a new iterator from the same list
    numbers = [1]
    num_iter = iter(numbers)  # Create a new iterator
    print(next(num_iter))  # num_iter has exhausted and cannot be reused,. now you have to create a new 

    for num in numbers:
      print(num) # can be called multiple times without re-initialization

  
Iterators are classified into three

  1️⃣ **Inbuilt iterator**:
  Python’s built-in has iterable objects as lists, tuples, dictionary, sets, file objects, strings, etc. These objects can be converted to iterators using iter()
  
  2️⃣ **Custom iterator**:
  A User-Defined Iterator (Custom Iterator) is when you create your own class with iter and next and make the class iterable

  3️⃣ **Generators**:
  
## Functions and Methods
- **Appending vs Extending:** `append()` adds a single element, while `extend()` adds multiple elements.
- **Pop:** Removes and returns an element (removes the last by default).
- **Deep vs Shallow Copy:** A shallow copy shares references to nested objects, while deep copy recursively copies all elements.
- **Map/Reduce:** `map()` applies a function to all items in an iterable, while `reduce()` aggregates elements into a single value.

### Iterators
- **Iterable vs Iterator:** An iterable returns an iterator, while an iterator supports `__iter__` and `__next__` methods to return items one at a time.
- **For loop:** Looks for `__iter__` and `__next__` methods to retrieve items from an iterator until `StopIteration` is raised.
  
### Custom Classes and Iterators
- **__iter__():** Returns the iterator object.
- **__next__():** Retrieves the next item in a sequence. Custom classes can implement these for iteration.

### Generators
- **Generators:** Functions that yield values one at a time (use `yield` keyword) and are more memory efficient.
- **List Comprehension vs Generator Expression:** Use list comprehensions for multiple iterations, while generators are lazy, providing values on the fly.

### Dictionaries
- **Hashing:** Used for fast search operations. Immutable types can be used as dictionary keys.
- **Dictionary Operations:** `get()`, `setdefault()`, `update()` methods provide efficient ways to handle key-value pairs.
  
### Decorators and Context Managers
- **@property:** Allows getter/setter methods to provide controlled access to attributes.
- **@staticmethod:** Lets you define methods that don’t require an instance of the class.
- **Context Managers:** Use `with` statements to automatically handle setup and teardown actions (e.g., file handling).

### Magic Methods
- **__len__():** Allows using `len()` on custom objects.
- **__getitem__():** Enables indexing like lists or dictionaries.
- **__eq__() and __gt__():** Implement comparison operations between objects.

Does this help clarify the concepts, or would you like more examples or elaborations on any particular topic?
