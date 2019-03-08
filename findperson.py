name_list = ["вася", "маша", "петя", "валера", "саша", "даша"]


def find_person():
    name = input("Введите имя: ").lower()
    if name in name_list:
        print(f"Имя {name} нашлось!")        
    else:
        print("Нет такого имени")

while True:
    find_person()
    