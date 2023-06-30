# Vytvoří proměnnou "týden", která obsahuje jednotlivé dny v týdnu malými písmeny
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

# Uživatel vybere číslo
cislo_dne = input('Vyber den v týdnu podle jeho čísla (1 - pondělí): ')

# Ověří, jestli jde o číselný znak a jde o hodnotu <1, 7>
if cislo_dne.isnumeric() and 1 <= int(cislo_dne) <= 7:
    
    # ... pokud ano, získá první písmeno vybraného dne a uloží jej do proměnné
    prvni_pismeno_dne = tyden[int(cislo_dne) - 1][0]
    
    # ... získá tip uživatele na první písmeno vybraného dne
    tip_prvniho_pismena = input('Jakým písmenem začíná tento den?: ')
    
    # Ověří, že písmeno dne v proměnné "tyden" a "prvni_pismeno_dne" 
    if tip_prvniho_pismena == prvni_pismeno_dne:
        
        # ... pokud jsou shodné
        print("Správné písmeno")
    
    else:
        # ... pokud jsou různé
        print("Špatné písmeno!")

else:
    
    # ... pokud ne , upozorní na chybný vstup
    print("Špatná vstupní hodnota!")
