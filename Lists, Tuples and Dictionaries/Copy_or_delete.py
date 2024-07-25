# Copy or delete

"""
Create a program that copies or deletes the items in a list
"""
# Copy or delete list
fruit_list = ["Fresa","Naranja","Mango","Pera"]
tutor = {
    "Nombre":"David",
    "Edad":27,
    "Cursos":["Python","Java","Javascript"]
}
new_list = fruit_list.copy()
print(new_list)
new_dictionary = tutor.copy()
print(new_dictionary)

fruit_list.clear()
print(fruit_list)
tutor.clear()
print(tutor)