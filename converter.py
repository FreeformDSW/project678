import sys
import json

# ~~~~~~~~~~~ Parsowanie ~~~~~~~~~~~
if len(sys.argv) != 3:
    print("Dozwolone sa tylko dwa argumenty")
else:
    plik_wej = sys.argv[1]
    plik_wyj = sys.argv[2]


# ~~~~~~~~~~~ Wczytanie pliku JSON i weryfikacja składni ~~~~~~~~~~~
def podaj_plik_json(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = json.load(plik)
            return a
    except json.JSONDecodeError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")
