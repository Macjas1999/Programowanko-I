import os

while True:
    print('KalkulatorXD')
    print('Odpowiednio działania odpowiadają znakom [*,/,+,-]')
    print('Aby wyść naciśniij q')
    znak = input('Działanie: ')
    if znak == '*':
        a = int(input('Pierwsza liczba: '))
        b = int(input('Druga liczba: '))
        fab = a * b
        print(fab)
    elif znak == '/':
        a = int(input('Pierwsza liczba: '))
        b = int(input('Druga liczba: '))
        fab = a / b
        print(fab)
    elif znak == '+':
        a = int(input('Pierwsza liczba: '))
        b = int(input('Druga liczba: '))
        fab = a + b
        print(fab)
    elif znak == '-':
        a = int(input('Pierwsza liczba: '))
        b = int(input('Druga liczba: '))
        fab = a - b
        print(fab)
    elif znak == 'q':
        os.system("cls")
        break
    else:
        os.system("cls")
        print('syf')
