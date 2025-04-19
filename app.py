def klasyfikacja(temp, wilgotnosc):
    if temp > 30 and wilgotnosc > 70:
        return "Upał i duża wilgotność – możliwe burze."
    elif temp < 0 and wilgotnosc < 40:
        return "Mróz i sucho – możliwe oblodzenia."
    else:
        return "Warunki normalne."

if __name__ == "__main__":
    try:
        temp = float(input("Podaj temperaturę (°C): "))
        wilgotnosc = float(input("Podaj wilgotność (%): "))
        print("Decyzja:", klasyfikacja(temp, wilgotnosc))
    except ValueError:
        print("Podano niepoprawne dane.")
