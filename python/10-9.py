try:
    with open('ch10/cat.txt') as cat_list:
        print(cat_list.read())
except FileNotFoundError:
    pass
try:
    with open('ch10/dog.txt') as dog_list:
        print(dog_list.read()) 
except FileNotFoundError:
    pass