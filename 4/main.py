import os

def funkcja_silni(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * funkcja_silni(n - 1)


def dodawanie(aa, bb):
    return aa + bb


def odejmowanie(aa, bb):
    return aa - bb


def pierwiastek(aa, bb):
    return aa ** (1/bb)

menu_options = {
    1: 'dodaj',
    2: 'silnia',
    3: 'odejmowanie',
    4: 'Pierwiastek',
    5: 'Koniec'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Wybierz: '))
        except:
            print('Zły klawisz, wpisz poprawny')
        if option == 1:
            a = int(input(": "))
            b = int(input(": "))
            print(dodawanie(a, b))
            os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif option == 2:
            a = int(input(": "))
            print(funkcja_silni(a))
            os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif option == 3:
            a = int(input(": "))
            b = int(input(": "))
            print(odejmowanie(a, b))
            os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif option == 4:
            b = int(input("stopień pierwiastka: "))
            a = int(input("liczba: "))

            print(pierwiastek(a, b))
            os.system('read -s -n 1 -p "Nacisnij dowolny klawisz"')
        elif option == 5:
            print('Program zakończony')
            exit()
        else:
            print('Zły klawisz. Wybierz od 1 do 4...')




