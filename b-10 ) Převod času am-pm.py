# Zadání časového údaje ve formátu "15:41" do proměnné "time"
time = input("Zadej čas ve formátu HH:MM:")


# Hodnotu v proměné rozdělí na list hodnot a uloží do proměnné "time_vals"
time_vals = time.split(":")


# Vytvoření proměnné "hours" and "mins", kterým přiřadí hodnoty z "time_vals"
hours_str = time_vals[0]
mins_str = time_vals[1]

#Ověří zda bylo zadáno číslo a ve formátu 0-24h a 0-60min
if hours_str.isnumeric() and mins_str.isnumeric() and int(hours_str) < 25 and int(mins_str) < 61:
    print("Zadaný čas:", time)    
    
else:
    print("Chybně zadaný čas HH:MM", time)
    quit()

#Převod hodin a  minut na integer   
hours = int(hours_str)
mins = int(mins_str)
hours_min = hours

#Převod 60min na hodinu
if mins == 60:
    hours_min = hours + 1      
    mins = 0
    
#Převod hodin
if hours_min == 24:
    adjusted_hours = hours_min - 24 

elif 24 > hours_min > 12:
    adjusted_hours = hours_min - 12
    
elif 0 <= hours_min <= 12:
    adjusted_hours = hours_min
    
else:
    print("Chybně zadaný čas 0-24h")
    quit()
    
   

# Označí denní dobu a uloží "AM"/"PM" do proměnné "daytime"
if 23 >= hours_min >= 12:
    daytime = "PM"

else:
    daytime = "AM"
    

# Vypiš převedený čas s doplňující větou

print("Converted to english format:", adjusted_hours, ":",mins, daytime)
