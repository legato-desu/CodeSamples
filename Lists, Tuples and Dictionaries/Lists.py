# Lists

"""
Create a program that manipulates the elements of a list
"""
grades = [99, 90, 67, 65, 60, 98, 76, 89]
# We search the list for the maximum value
maximum_note = max(grades)
print(maximum_note)
# We search the list for the minimum value
minimum_grade = min(grades)
print(minimum_grade)
# We look at the number of values ​​contained in the list
note_length = len(grades)
print(note_length)
# We sort the list in order from largest to smallest
sort_notes = sorted(grades)
print(sort_notes)
# We sort the list in reverse order "least to greatest"
sort_list = sorted(grades, reverse=True)
print(sort_list)
# Add new values ​​to the list and show how many values ​​there now
new_notes = grades + [90, 98, 76, 89]
print(new_notes)
print(len(new_notes))
# We remove a value from the list based on its position 
del(new_notes[0])
print(new_notes)
print(len(new_notes))