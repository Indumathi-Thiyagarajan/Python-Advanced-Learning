Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
3 of 1,169
code ex
Inbox

Indumathi Thiyagarajan <indhut0506@gmail.com>
11:09 AM (47 minutes ago)
to me

# Calling class inside a class 

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

# with using iter and next, when iterating over class instance

    class Car:
        def __init__(self):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
            # self.engine = Engine(horsepower, engine_type)
            self._index = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= len(self.make):
                raise StopIteration
            make = self.make[self._index]
            model = self.model[self._index]
            self._index += 1
            return (make,model)

    car_obj = Car()
    for car in car_obj:
        print(car)

# with just next, when iterating over class instance

    class Car:
        def __init__(self):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
            # self.engine = Engine(horsepower, engine_type)
            self._index = 0
        
        def __next__(self):
            if self._index >= len(self.make):
                raise StopIteration
            make = self.make[self._index]
            model = self.model[self._index]
            self._index += 1
            return (make,model)

    car_obj = Car()
    print(next(car_obj))
    print(next(car_obj))
    print(next(car_obj))
    print(next(car_obj))

# using generator

    class Car:
        def __init__(self):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
            # self.engine = Engine(horsepower, engine_type)
            self._index = 0
        
        def __iter__(self):
            for i,j in zip(self.make , self.model):
                yield (i,j)
                
    car_obj = Car()
    for car in car_obj:
        print(car)

# iterating over class instance within class

    class Car:
        def __init__(self):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
        
        def __iter__(self):
            return Engine(self)
        
        def __len__(self):
            return len(self.make)
        
    class Engine:
        def __init__(self, car_obj):
            self._car_obj = car_obj
            self._index = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= len(self._car_obj):
                raise StopIteration
            make = self._car_obj.make[self._index]
            model = self._car_obj.model[self._index]
            self._index += 1
            return (make,model)

    car_obj = Car()
    for car in car_obj:
        print(car)

# iterating over class instance within class with variable input 

    class Car:
        def __init__(self,horsepower):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
            self.horsepower = horsepower
        def __iter__(self):
            return Engine(self)
        
        def __len__(self):
            return len(self.make)
        
    class Engine:
        def __init__(self, car_obj):
            self._car_obj = car_obj
            self._index = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= len(self._car_obj):
                raise StopIteration
            make = self._car_obj.make[self._index]
            model = self._car_obj.model[self._index]
            horse_power = 0.1* self._car_obj.horsepower
            self._index += 1
            return (make,model,horse_power)

    car_obj = Car(300)
    for car in car_obj:
        print(car)


# with using getitem instead of iter and next

    class Car:
        def __init__(self):
            self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
            self.model = ['model1', 'model2', 'model3', 'model4']
        
        def __getitem__(self, index):
            if index >= len(self.make):
                raise IndexError
            make = self.make[index]
            model = self.model[index]
            return (make, model)

    car_obj = Car()
    for car in car_obj:
        print(car)

# with using getitem and len instead of iter and next:

 class Car:
    def __init__(self):
        self.make = ['Tesla', 'Toyota', 'Ford', 'Chevy']
        self.model = ['model1', 'model2', 'model3', 'model4']
        
    def __len__(self):
        return len(self.make)
    
    def __getitem__(self, index):
        return self.make[index], self.model[index]
    
car_obj = Car()
for car in car_obj:
    print(car)


