def klasyfikuj_bmi(waga_kg: float, wzrost_cm: float) -> str:
    # Przelicz wzrost na metry
    wzrost_m = wzrost_cm / 100
    if wzrost_m <= 0:
        return "Nieprawidłowy wzrost."
    bmi = waga_kg / (wzrost_m ** 2)
    
    if bmi < 18.5:
        return f"Niedowaga (BMI={bmi:.1f})"
    elif bmi < 25:
        return f"Waga prawidłowa (BMI={bmi:.1f})"
    elif bmi < 30:
        return f"Nadwaga (BMI={bmi:.1f})"
    else:
        return f"Otyłość (BMI={bmi:.1f})"

if __name__ == "__main__":
    try:
        waga = float(input("Podaj wagę w kilogramach (kg): "))
        wzrost = float(input("Podaj wzrost w centymetrach (cm): "))
        wynik = klasyfikuj_bmi(waga, wzrost)
        print("Wynik klasyfikacji:", wynik)
    except ValueError:
        print("Błąd: proszę wpisać poprawne liczby.")
