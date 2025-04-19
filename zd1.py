# mnożenie list z obsługą błędu
a = [1, 2, 3]
b = [4, 5, 6]

try:
    print(a * b)
except TypeError:
    print("Operacja niezdefiniowana dla mnożenia list.")
