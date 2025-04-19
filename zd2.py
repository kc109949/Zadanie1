def iloczyn_skalarny_lista(x: list, y: list) -> float:
    iloczyn = 0.
    for i in range(len(x)):
        iloczyn += x[i] * y[i]
    return iloczyn

a = list(range(5))
b = list(range(5))

print("Iloczyn skalarny (lista):", iloczyn_skalarny_lista(a, b))
