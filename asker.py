def ask_user():
    dict = {"привет": "Привет", "как дела?": "Хорошо", "что делаешь?": "слежу за тобой", "пока": "Пока"}
    
    while True:

        try:
            user_input = input("Поговори со мной: \n").lower()
            if user_input in dict:
                print(dict[user_input])
                if user_input == "пока":
                    break
            else:
                print("Не знаю что и сказать!")
        except KeyboardInterrupt:
            print("Жаль, что ты уходишь")
            break

ask_user()
