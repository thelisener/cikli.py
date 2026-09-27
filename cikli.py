# 1.  uzdevums

C = float(input("Ievadiet temperatūru celsija grādos:"))
F = C*9/5 +32
K = C + 273.15
print(f"Temperatūra {C}°C Fārenheitos: {F}°F, un Kelvinos: {K}°K")
if C <= -273.15:
    print("Temperatūra zem absolūtās nulles fiziski nav iespējama.")
    exit()
else:
    if F > 212:
        print("Temperatūra ir virs ūdens viršanas temperatūras.")
    elif F < 32:
        print("Temperatūra ir zem ūdens sasalšanas punkta.")
    else:
        print("Temperatūra ir starp ūdens sasalšanas un viršanas temperatūru.")

# 2. uzdevums
c = 299792458
while True:
    atrums = int(input("Uzminiet aptuveno gaismas ātrumu:"))
    if atrums > c:
        print("Pārāk liels skaitlis!")
    elif atrums < c:
        print("Pārāk mazs skaitlis!")
    else:
        print("Pareizi! Gaismas ātrums ir 299 792 458 m/s.")
        break

# 3. uzdevums
parole = "E=mc^2"
meginajumi = 0
while True:
    ievade = str(input("Ievadiet paroli:"))
    if ievade != parole:
        print("Nepareiza parole, mēģiniet vēlreiz.")
        meginajumi += 1
        if meginajumi == 3:
            print("Pārāk daudz nepareizu mēģinājumu, piekļuve liegta.")
            break
    else:
        print("Piekļuve piešķirta.")
        break

# 4. uzdevums
vienadojums = ["F = ma", "E = mc^2", "V = IR", "P = IV", "K.E. = 1/2 mv^2"]
for vien in vienadojums:
    print(vien)
    if vien == "E = mc^2":
        break
        
# 5.uzdevums
ievaddati = [0, 1, 2, 3]
for i in ievaddati:
    print()
    for a in range(len(ievaddati)):
        if i != a:
            print(ievaddati[0], end="\t")
        else:
            print(a, end="\t")

# 6.uzdevums

veselie_skaitli = [70, 19, -8, 59, -62, 90, -7, -15, -14, 51, 1, 93,\
                    -42, 68, 4, 33, -53, -29, 21, 34]

#veselie_skaitli = [int(i) for i in input().split()]

for i in veselie_skaitli:
    if i < 0 and i % 2 == 0:
        continue
    elif i > 0 and i % 2 == 0:
        print(f"{i} ir Pozitīvs un pāra.")
    elif i < 0 and i % 2 == 1:
        print(f"{i} ir Negatīvs un nepāra.")
    elif i > 0 and i % 2 == 1:
        print(f"{i} ir Pozitīvs un nepāra.")
    elif i == 0:
        print(f"{i} ir Nulle nav ne pozitīva, ne negatīva.")
    if 5 < i < 15:
        print(f"{i} ir Skaitlis ir diapazonā: no 5 līdz 15.")
    if i < -10 or i > 20:
        print(f"{i} ir Ārpus diapazona.")

# 7.uzedvums

fizikalais_lielums = input("Ko vēlaties aprēķināt (1. F, 2. Fg, 3. KE, 4. PE):")
match fizikalais_lielums:
    case 1:
        m = float(input("Ievadi masu:"))
        a = float(input("Ievadi paātrinājumu"))
        if m < 0:
            print("masa nedrīkst būt negatīva!")
            
        F = m*a
        print(f"Spēks ir {F}")
            
    case 2:
        m = float(input("Ievadi masu:"))
        g = 9.81
        if m < 0:
            print("masa nedrīkst būt negatīva!")
            
        Fg = m*g
        print(f"Spēks ir {Fg}")
        
    case 3:
        m = float(input("Ievadi masu:"))
        v = float(input("Ievadi ātrumu:"))
        if m < 0:
            print("masa nedrīkst būt negatīva!")
            
        KE = 0.5*m*v^2
        print(f"Kinētiskā enerģija ir {KE}")
            
       
    case 4:
        m = float(input("Ievadi masu:"))
        h = float(input("Ievadi augstumu:"))
        g = 9.81
        if m < 0:
            print("masa nedrīkst būt negatīva!")
            
        KP = m*g*h
        print(f"Potenciālā enerģija ir {KP}")