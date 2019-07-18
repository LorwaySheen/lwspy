try:
    with open('ch10/cat.txt') as cat_list:
        print(cat_list.read())
except FileNotFoundError:
    print("cat.txt不存在")
try:
    with open('ch10/dog.txt') as dog_list:
        print(dog_list.read()) 
except FileNotFoundError:
    print("dog.txt不存在")
    