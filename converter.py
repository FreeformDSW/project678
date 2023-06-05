import sys
import json
import yaml
import xmltodict

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


# ~~~~~~~~~~~ Zapisanie danych do pliku JSON ~~~~~~~~~~~
def zapisz_do_pliku_json(a, plik_wyj):
    try:
        with open(plik_wyj, 'w') as plik:
            json.dump(a, plik)
        print("Udana konwersja do formatu JSON")
    except:
        print("Błąd")


# ~~~~~~~~~~~ Wczytanie pliku yml i weryfikacja składni ~~~~~~~~~~~
def podaj_plik_yml(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = yaml.safe_load(plik)
            return a
    except yaml.YAMLError:
        print("Taki plik nie istnieje, sprawdź nazwę")
    except FileNotFoundError:
        print("Taki plik nie istnieje")


# ~~~~~~~~~~~ Zapisanie danych do pliku YML (yaml) ~~~~~~~~~~~
def zapisz_do_pliku_yml(a, plik_wyj):
    try:
        with open(plik_wyj, 'w') as plik:
            yaml.dump(a, plik)
        print("Udana konwersja do formatu YML")
    except:
        print("Błąd")


# ~~~~~~~~~~~ Wczytanie pliku XML i weryfikacja składni ~~~~~~~~~~~
def wczytaj_z_pliku_xml(plik_wej):
    try:
        with open(plik_wej, 'r') as plik:
            a = xmltodict.parse(plik.read())
            return a
    except FileNotFoundError:
        print("Taki plik nie istnieje")
