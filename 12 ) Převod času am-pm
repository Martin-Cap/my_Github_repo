# Zadá časový údaj ve formátu "15:41" do proměnné "time"
time = input('Please enter your time (format HH:MM): ')  # 12:51

# Hodnotu v proměnné rozdělí na list hodnot a uloží do proměnné "time_vals"
time_vals = time.split(':')

# Vytvoří proměnné "hours" and "mins", kterými přiřadí hodnoty z "time_vals"
hours = time_vals[0]
mins = time_vals[1]

# Pokud je hodnota v "hours" větší jak 12, převede na příslušný string
if int(hours) <= 12:
        adjusted_hours = hours

 # ... jinak ponechá hodnotu původní
else:
    adjusted_hours = str(int(hours) - 12)


# Označí denní dobu a uloží "AM"/"PM" do proměnné "daytime"
if int(hours) >= 12:
    daytime = "PM"
else:
    daytime = "AM"

# Vypíše převedený čas s doplňující větou
print('Converted to english format:', adjusted_hours, ':', mins, daytime)
