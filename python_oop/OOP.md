# Object Oriented Programming with Python

## Why do we use Classes in any programming language
- They allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if need be.
- Attributes and methods refer to data and functions associated with a Class
  

## Let's see some examples:

- Simple employee class:
  
```python:
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def info(self):
        print(f"Hello my name is {self.first} and I get paid {self.pay}!")

emp_1 = Employee()
emp_2 = Employee()

emp_1.name = "milad"
emp_1.pay = 50000

emp_2.name = "javad"
emp_2.pay = 60000

print()
```

## Class variables vs instance variables

- Class variable is a data that would be associate with all the instances created from the same class

