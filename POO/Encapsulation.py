# Encapsulation

"""
To practice encapsulation:
Create Person class.
Create the private variables age, name and phone number of the Person class.
Create gets and sets of each property.
Create a person object in main.
Use gets and sets to give values to the age, name and phone properties, 
Finally, show them through the console.
"""
class Person:  
    def __init__(self,age,name,phone):
        self.age = age
        self.name = name
        self.phone = phone
    def set_age(self,age):
        self.age = age
    def set_name(self,name):
        self.name = name
    def set_phone(self,phone):
        self.phone = phone
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
user = Person(age=29, name = "David", phone = "+57 123456789")
print("Nombre:",user.get_name())
print("Edad:",user.get_age(),"años")
print("Telefono:",user.get_phone())