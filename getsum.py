def get_summ(num_one, num_two):
    return int(num_one) + int(num_two)
    
 
while True:
    num_one = input("Введите число 1: ")
    num_two = input("Введите число 2: ")

    try:
        summ = get_summ(num_one, num_two)
        print(summ)
        break
    except ValueError:
        print("Вводите числа!")