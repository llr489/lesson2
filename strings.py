string1 = 'somestring'
string2 = 'otherstring'
string3 = '4symstring'
string4 = 'learn'
integer = 3
decimal = 1.0


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

print(string_compare(string1, string1))
print(string_compare(string3, string3))
print(string_compare(string1, string2))
print(string_compare(string1, string3))
print(string_compare(string1, string4))
print(string_compare(string2, string3))
print(string_compare(string2, string4))
print(string_compare(string3, string4))
print(string_compare(string1, integer))
print(string_compare(decimal, string2))
