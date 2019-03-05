def age_check():

    age = input('Введите возраст: ')

    try:
        age = int(age)
    except ValueError:
        print('Возраст должен быть числом!')
        age_check()
    else:
        if age < 3 or age > 99:
            print("Возраст должен быть от 3 до 99 лет")
            age_check()
        else:
            if age in range(3,7):
                print('Детский сад')
            elif age in range (7,18):
                print('Школа')
            elif age in range(18,55):
                print('Работа')
            else: 
                print('Пенсия')

age_check()