#Object-oriented programming concepts, such as classes, objects, and inheritance

'''class Employee:#initializing employee class with no attr. pass function allows you to leave it empty otherwise you will get an error
    pass

empl_1 = Employee()#Instance of employee class
empl_2 = Employee()#Instance of employee class

empl_1.first = "Corey"#Manually adding attributes to class
empl_1.last = "Wilson"

empl_2.first = "Kyle"
empl_2.last = "Watson"

print(empl_1.first)
print(empl_2.last)'''


class Employee:#initializing class with init method

    raise_amount = 1.04

    def __init__(self, first, last, pay):#methods always take the instance as the first argument which is self
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):#method to print employee fulname
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

empl_1 = Employee("Corey", "Wilson", 100000)
empl_2 = Employee("Kyle", "Watson", 95000)

print(empl_1.fullname())