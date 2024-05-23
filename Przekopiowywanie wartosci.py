from datetime import datetime
import openpyxl

current_time = datetime.now()  # czasy
wb2 = openpyxl.load_workbook(r"formatka.xlsx")  # Formatka

print("Ładowanie Ok")

def copy(przesuniecie=0, sciezka="Agenci", skoroszyt="Efektywnosc", dlugosc="BK", typ=""):  # przesuniecie - ile w bok dalej, #dlugosc - ilosc kolumn danych
    print("Start")
    wb1 = openpyxl.load_workbook(sciezka)  # Surowe dane
    s1 = wb1.active  # surowy arkusz
    s2 = wb2[skoroszyt]  # arkusz formatki
    global wyniki
    wyniki = wb2["WYNIKI"]

    print("Dane dostępne")

    znak = chr(
        ord("A") + przesuniecie)  # ustalenie jaki znak bedzie po przesunieciu na drugiej pozycji, uwazac na przeskok z AX na BA, nie zakceptuje tego
    znakx = dlugosc[0] + znak  # ustalenie calej nowej dlugosci

    # Wyliczanie czy wiecej jest wierszy w arkuszu formatki czy danych
    n = 1
    a = s1["A" + str(n)]
    while a.value is not None:
        n = n + 1
        a = s1["A" + str(n)]

    m = 1
    a = s2[znak + str(m)]
    while a.value is not None:
        m = m + 1
        a = s2[znak + str(m)]

    wysokosc = max(n, m) - 1
    print("Wysokosc", wysokosc)



    a = s1['A1':dlugosc + str(n)]  # wspulrzedne skopiowania

    wiersze = []
    kolumny = []

    # Tworzenie tablicy dwuwymiarowej zawierajacej dane z surowych
    for i in a:
        kolumny.append(wiersze)
        wiersze = []
        for j in i:
            wiersze.append(j.value)

    kolumny.append(wiersze)
    print("Dane skopiowane")

    b = s2[znak + "1": znakx + str(n)]  # Wspolrzedne wklejenia
    y = 0
    for i in b:
        y = y + 1
        x = 0
        for j in i:
            j.value = kolumny[y][x]
            x = x + 1

    print("Wklejono", wysokosc, "kolumn")

    if typ == "akt":
        agenci = wysokosc
        style(agenci)

    if typ == "pol":
        rekordy = wysokosc

    return wb2


wb2 = copy(3, r"a1.xlsx", r"Połączenia", "BH", "pol")
wb2 = copy(2, r"a2.xlsx", r"Aktywności 02", "AA", "akt")

# Zapisanie zmian w pliku Excel
wb2.save(r"wynik.xlsx")
print("Zapisano")
print("Akcja zajęła:", datetime.now() - current_time)



