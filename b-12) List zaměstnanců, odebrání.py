# Zadané seznamy "kandidati" a "zamestnanci"
kandidati = ['Bruno', 'Anežka']
zamestnanci = ['František', 'Jan', 'Anna', 'Jakub', 'Klára']

# Odstranění stringu ze seznamu "kandidati"
print(kandidati)
vymaz = (input("koho odstranit?:")).capitalize()
kandidati.remove(vymaz)

# Výpis zbývajícího obsahu v seznamu "kandidati"
print(vymaz, "odstraněn z kandidatu:", kandidati)

# Opakovat třikrát jméno uvnitř seznamu "kandidati"
kandidati_3 = kandidati * 3

# Výpis zopakovaného stringu v "kandidati"
print("Opakování prvku v kandidati:", kandidati_3)

# Spojení seznamů "kandidati" a "zamestnanci"
zamestnanci = zamestnanci + kandidati

# Výpis spojených seznamů
print('Spojení kandidati a zamestnanci: ' + str(zamestnanci))
