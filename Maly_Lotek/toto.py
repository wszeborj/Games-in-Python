import random

liczba = random.randint(1, 10)
# print(f'Wylosowana liczba: {liczba}')

for i in range(3):
    print(f'Próba: {i + 1}')
    odp = input('Jaka liczba od 1 do 10 mam na myśli? ')

    if liczba == int(odp):
        print(f'Zgadłeś! Wylosowana liczba to {liczba}.')
        break
    elif i == 2:
        print(f'Niestety nie udało się... Wylosowana liczba to {liczba}.')
    else:
        print('Spróbuj jeszcze raz ;)')
    print()
print('koniec')