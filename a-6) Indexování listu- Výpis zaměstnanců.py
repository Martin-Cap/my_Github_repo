# Zadaný seznam "zamestnanci"
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]

# Hodnota na druhém indexu
print('Na indexu 2 je:', zamestnanci[2])

# Zjištění kolikátý je poslední index
posledni_index = len(zamestnanci) - 1

# Výpis hodnoty na posledním indexu
print('Na', posledni_index, "indexu je:",  zamestnanci[posledni_index])

# Výpis hodnot na indexech 2-5
print('V intervalu od 2 do 5 je:', zamestnanci[2:6])

# Výpis každého třetího prvku listu "zamestnanci"
print('Každý třetí člen je:', zamestnanci[::3])
