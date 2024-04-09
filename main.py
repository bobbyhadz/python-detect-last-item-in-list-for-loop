# Detect the last item in a list using a for loop in Python

my_list = ['one', 'two', 'three', 'four']

for index, item in enumerate(my_list):
    if index != len(my_list) - 1:
        print(item, 'is NOT last in the list ✅')
    else:
        print(item, 'is last in the list ❌')