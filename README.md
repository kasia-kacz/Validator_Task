# Validator

Program do walidacji harmonogramu czasu pracy.

## Autor

Katarzyna Kaczorowska

## Biblioteki

Stosowane biblioteki i moduły:
  * pandas
  * datetime
  * calendar
  * unittest
  * pathlib

## Uruchomienie programu

  1. Pobranie programu z GitHub (https://github.com/kasia-kacz/Validator.git)
  2. Aktywacja wirtualnego środowiska uruchomieniowego (sciezka_do_projektu/validator/venv/Scripts/activate)
  3. Uruchomienie programu (./main.py)
  4. Uruchomienie testów (./tests/run_tests.py)

## Założenia

W celu realizacji wymagań założono, że każdy dzień pracy rozpoczyna się o tej samej godzinie (brak elastycznych godzin pracy).

## Uwagi

1. Wszystkie pliki .csv z danymi znajdują się w folderze ./validator/data/
2. Aby odpowiednio zrealizować wymagania, została wprowadzona konwencja nazw plików z danymi - rok_miesiac.csv (przykład: 2023_03.csv)
3. Na podstawie konkretnego roku i miesiąca ustalane są dni tygodnia dla odpowiednich dni danego miesiąca
4. Aby zmienić wczytywany plik z danymi należy zmienić zmienną 'filename' w module 'main.py'
5. Wszystkie testy oraz dane potrzebne do przeprowadzenia testów jednostkowych zapisane są w folderze ./tests
6. Aby przeprowadzić wszystkie testy wystarczy uruchomić skrypt ./tests/run_tests.py
