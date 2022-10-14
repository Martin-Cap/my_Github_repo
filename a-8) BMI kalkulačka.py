# Vstupní hodnoty uživatele
vyska = 1.70
vaha = 75
jmeno = 'Martin'


# Výpočet BMI
bmi = int(vaha / vyska ** 2)

# Vytvoří proměnnou "kategorie", kam uloží slovní ohodnocení BMI
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

# Vytiskne odpověď s výsledkem
print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")
