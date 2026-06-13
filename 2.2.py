from datetime import datetime

def den_nedeli(den, mesyac, god):
    data = datetime(god, mesyac, den)
    dni = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
    return dni[data.weekday()]

def visokosny(god):
    if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0):
        return True
    return False

def vozrast(den, mesyac, god):
    segodnya = datetime.now()
    data_rozhdeniya = datetime(god, mesyac, den)
    let = segodnya.year - data_rozhdeniya.year
    if (segodnya.month, segodnya.day) < (mesyac, den):
        let -= 1
    return let

def tablo(cifra):
    pattern = {
        '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        '1': ['  *  ', ' **  ', '  *  ', '  *  ', ' *** '],
        '2': [' *** ', '   * ', ' *** ', '*    ', ' *** '],
        '3': [' *** ', '   * ', ' *** ', '   * ', ' *** '],
        '4': ['*   *', '*   *', ' *** ', '   * ', '   * '],
        '5': [' *** ', '*    ', ' *** ', '   * ', ' *** '],
        '6': [' *** ', '*    ', ' *** ', '*   *', ' *** '],
        '7': [' *** ', '   * ', '  *  ', ' *   ', '*    '],
        '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
        '9': [' *** ', '*   *', ' *** ', '   * ', ' *** '],
        ' ': ['     ', '     ', '     ', '     ', '     ']
    }
    return pattern.get(cifra, pattern[' '])

den = int(input("День: "))
mesyac = int(input("Месяц: "))
god = int(input("Год: "))

print("\nДень недели:", den_nedeli(den, mesyac, god))

if visokosny(god):
    print("Год високосный")
else:
    print("Год не високосный")

print("Возраст:", vozrast(den, mesyac, god), "лет")

stroka = f"{den:02d} {mesyac:02d} {god}"

for i in range(5):
    for simvol in stroka:
        print(tablo(simvol)[i], end='  ')
    print()