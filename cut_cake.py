def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "С ума посходили?"

piece = cut_cake([1, 3, 2])
print(piece)
