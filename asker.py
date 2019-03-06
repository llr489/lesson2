def ask_user():
    while True:
        answer = input("Как дела?\n")
        if answer == "Хорошо" or answer == "хорошо":
            print("Рад за тебя!")
            break

ask_user()