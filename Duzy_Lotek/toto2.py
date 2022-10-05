import random

try:
    ile_liczb = int(input('Podaj ilość liczb, które chcesz odgadnąć: '))
    maks_liczba = int(input('Podaj maksymalną losowaną liczbę: '))

    if ile_liczb > maks_liczba:
        print('Błędne dane')
        exit()
except ValueError:
    print('Błędne dane!')
    exit()

lista_wylosowanych_liczb = []

for i in range(3):
    i = 0
    while i < ile_liczb:
        liczba = random.randint(1, maks_liczba)
        if lista_wylosowanych_liczb.count(liczba) == 0:
            lista_wylosowanych_liczb.append(liczba)
            i += 1
    print(f'Lista wylosowanych liczb: {lista_wylosowanych_liczb}')
    print(f'Wytypuj {ile_liczb} z {maks_liczba} liczb:')
    wytypowane_liczby = set()
    i = 0
    while i < ile_liczb:
        try:
            typ = int(input(f'Podaj liczbę {i+1}: '))
        except ValueError:
            print('Błędne dane!')
            continue

        if 0 < typ <= maks_liczba and typ not in wytypowane_liczby:
            wytypowane_liczby.add(typ)
            i += 1
    # print(f'Wytypowane liczy to: {wytypowane_liczby}' )

    trafienia = set(lista_wylosowanych_liczb) & wytypowane_liczby
    trafienia2 = set(lista_wylosowanych_liczb).intersection(wytypowane_liczby)
    print(f'trafienia = {trafienia}')
    # print(f'trafienia2 = {trafienia2}')
    if trafienia:
        print(f'Ilość trafień: {len(trafienia)}')
        print(f'Trafione liczby: {trafienia}')
    else:
        print('Brak trafień.')