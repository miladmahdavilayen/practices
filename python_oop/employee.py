class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"

    def info(self):
        print(f"Hello my name is {self.first} and I get paid {self.pay}!")

emp_1 = Employee('milad', 'mahdavi', 50000)
emp_2 = Employee('javad', 'mahdavi', 90000)

emp_1.info()
