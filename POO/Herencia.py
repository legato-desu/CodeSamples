# Herencia

"""
Create a Person class with the following variables:

Age
Name
The phone

Once the class is created, create a new Customer class that inherits 
of Person, this new class will have the credit variable only 
for that class.

Now create an object of the Customer class that must have as 
properties, age, phone number, name and credit, 
You have to give them value and show them on the screen.

Once this is done, do the same with the Worker class that 
inherits from Person, and with a salary variable that only has 
the Worker class.
"""
class Person():
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone 
    def user(self):
        print("Nombre:", self.name, "Edad:", self.age, "Telefono:", self.phone)    
class Client (Person):
    def __init__(self, name, age, phone,credit):
        super().__init__(name, age, phone)
        self.credit = credit
    def user(self):
        super().user()
        print("El credit fue", self.credit)
class Job (Person):
    def __init__(self, name, age, phone,salary):
        super().__init__(name, age, phone)
        self.salary = salary
    def user(self):
        super().user()
        print("El salario es", self.salary)
Persona_1 = Client ("David","29","+571234567","Aprobado")
Persona_1.user()
Job_1 = Job("Jorge","27","+57290834","4086590")
Job_1.user()