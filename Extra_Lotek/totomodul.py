import random

def ustawienia() -> (int, int, int):
    '''Funckja pobiera ilosc losowych liczb, maksymalną losowaną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry'''
    while True:
        try:
            ile_liczb = int(input('Podaj ilość liczb, które chcesz odgadnąć: '))
            maks_liczba = int(input('Podaj maksymalną losowaną liczbę: '))

            if ile_liczb > maks_liczba:
                print('Błędne dane')
                continue
            ilelos = int(input('Ile losowań: '))
            return (ile_liczb, maks_liczba, ilelos)
        except ValueError:
            print('Błędne dane!')
            continue

def losuj_liczby(ile_liczb: int, maks_liczba: int) -> list:
    '''funkcja losuje ile unikalnych liczb calkowitych od 1 do maks'''
    lista_wylosowanych_liczb = []
    i = 0
    while i < ile_liczb:
        liczba = random.randint(1, maks_liczba)
        if lista_wylosowanych_liczb.count(liczba) == 0:
            lista_wylosowanych_liczb.append(liczba)
            i += 1
    # print(f'Lista wylosowanych liczb: {lista_wylosowanych_liczb}')
    return lista_wylosowanych_liczb


def pobierz_typy(ile_liczb: int, maks_liczba: int) -> set():
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
    return wytypowane_liczby


def wyniki(liczby: list, typy):
        trafione = set(liczby) & typy
        if trafione:
            print(f'Ilość trafień {len(trafione)}')
            print(f'Trafione liczby: {trafione}')
        else:
            print('Brak trafień. Spróbuj jeszcze raz!')
        print('x' * 40, '\n')