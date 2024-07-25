# Emulate join

"""
Create a program to emulate the join operation to concatenate a list
number = [2, 3, 5, 7, 11]
# 2 3 5 7 11
print(''.join([str(n)for n in number]))
"""
def concatenate_list(list):
    result = ''
    for n in list:
        result += str(n)
    return result
numbers = [2, 3, 5, 7, 11]
print(concatenate_list(numbers))