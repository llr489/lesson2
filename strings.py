string1 = input("Введите строку 1: ")
string2 = input("Введите строку 2: ")

def string_compare(string1, string2):
    if type(string1) == str and type(string2) == str:
        if string1 == string2:
            return 1
        elif len(string1) > len(string2):
            if string2 == 'learn':
                return 3
        else:
            return 2   
    else:
        return 0

print(string_compare(string1, string2))