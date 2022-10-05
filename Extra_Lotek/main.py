from totomodul import ustawienia, losuj_liczby, pobierz_typy, wyniki

def main(args):
        ile_liczb, maks_liczba, ilerazy = ustawienia()
        liczby = losuj_liczby(ile_liczb, maks_liczba)
        for i in range(ilerazy):
            typy = pobierz_typy(ile_liczb, maks_liczba)
            wyniki(liczby, typy)



if __name__=='__main__':
    import sys
    sys.exit(main(sys.argv))