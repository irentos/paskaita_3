import random

#1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”
for i in range(10):
    print('labas')
print('---------2-----------')
#2.Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
for i in range(10):
    print(i)
print('---------3-----------')
#3.Sukurkite masyvą iš dešimties augalų pavadinimų.
plants = ['zamiokulkus', 'alocasia', 'spathiphyllum', 'yucca', 'cactus', 'orchid', 'monstera', 'ficus', 'dieffenbachija', 'calatheas' ]
print(plants)
print('---------4-----------')
#4.Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
for i in plants:
    print(i)
print('---------5-----------')
#5.Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio,
# ir baigiant pirmuoju. (atvirkščias ciklas).
print(plants[::-1])
print('---------6-----------')
#6.Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
for i in range(10, 51, 2):
    print(i)
print('---------7-----------')
#7.Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.)
# (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
for i in range(10, 51):
    if i % 2 != 0:
        continue
    if i % 10 == 0:
        continue
    print(i)
print('---------8-----------')
#8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite,
# kiek kartų kintamasis i turėjo porinę(можно делить на 2) reikšmę;
count = 0
for i in range(21):
    if i % 2 == 0: # == можно /2 // != нельзя /2
        count += 1
print(count)
print('---------9-----------')
#9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
count1 = 0
count2 = 0
for words in plants:
    if len(words) < 5:
        count1 += 1 # += to cont new things / =+ adding to this element
    if len(words) > 7:
        count2 += 1
print("5 simboliai:", count1, ',', "7 simboliai:", count2)
print('---------10-----------')
#10. Suskaičiuokite kiek 3čio uždavinio masyve
# yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai.
# (tarp 5 ir 10 simbolių ilgio)
count = 0
for words in plants:
    if len(words) > 5 and len(words) < 10:
        count += 1
print(count)
# -----------------------------------------------------------
# count = sum(1 for words in plants if 5 < len(words) < 10)
# print(count)
# count = 0
# for words in plants:
#     if 5 < len(words) < 10:
#         count += 1
# print(count)
print('---------sunkesni 1 ciklai-----------')
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300,
# atspausdinkite juos atskirtus tarpais vienoje eiluteje
# ir suskaičiuokite kiek tarp jų yra didesnių už 150.
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
result = []
count = 0
for i in range(300): # only after for randomizing in code
    num = random.randint(0,300)
    if num > 150:
        count += 1
    if num > 275:
        print(f'[{num}]', end =' ')
    else:
        print(num, end =' ')
print()
print('count > 150:', count)

print('---------sunkesni 2 ciklai-----------')
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000,
# kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais.
# Po paskutinio skaičiaus kablelio neturi būti.
kab = []
for i in range(1,3001):
    if i % 77 == 0:
        if i == 77:
            print(i, end='')
        else:
            print(f',{i}', end='')
print()

print('---------sunkesni 3 ciklai-----------')
# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
side = 25
for square in range(side):
    print('* ' * side)
print('---------sunkesni 4-----------')
#Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
# square = []
# for i in range(side):
#     row = ['* '] * side


print('---------sunkesni 5-----------')
# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija,
# kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus
# išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
# применить к 6 заданию
while True: # МЫ КИДАЕМ МОНЕТУ ДО
    coin = random.randint(0,1)
    if coin == 0: # if работает как ON // OFF
        print("H")
        break # КАК ТОЛЬКО ВЫПАДЕТ Н СТОП
    else:
        print("S")
# Tris kartus iškritus herbui;
print("------------")
count = 0
while True: # МЫ КИДАЕМ МОНЕТУ ДО можно задать значение тру count < 3
    coin = random.randint(0,1)
    if coin == 0: # if работает как ON // OFF
        print("H")
        count += 1 # если тут if то быстрее но не видно что делает код
    else:
        print("S")
    if count >= 3: # if тут это второй стоп когда больше равно 3
        break
print("------------")
# Tris kartus iš eilės iškritus herbui;
count = 0
while True: # МЫ КИДАЕМ МОНЕТУ ДО можно задать значение тру count < 3
    coin = random.randint(0,1)
    if coin == 0: # if работает как ON // OFF
        print("H")
        count += 1 # если тут if то быстрее но не видно что делает код
    else:
        print("S")
        count = 0 # обнуляем значения до 0 если выпадает не подряд нужное значение
    if count >= 3: # if тут это второй стоп когда больше равно 3 // >= предохранитель чтоб не ==
        break

print('---------sunkesni 6-----------')
k_pts_t = 0
p_pts_t = 0
while True:
    k_pts = random.randint(5,25)
    p_pts = random.randint(5,25)
    k_pts_t += k_pts
    p_pts_t += p_pts
    if k_pts > p_pts:
        print (f'Partiją laimėjo Kazys su tasku persvara {k_pts} > {p_pts}. Bendras tasku balansas P: {p_pts_t}, K: {k_pts_t}')
    else:
        print(f'Partiją laimėjo Petras su tasku persvara {p_pts} > {k_pts}. Bendras tasku balansas P: {p_pts_t}, K: {k_pts_t}')
    if k_pts_t >= 222 or p_pts_t >= 222:
        break
if k_pts_t > p_pts_t:
    print('Zaidima laimejo Kazys')
elif p_pts_t > k_pts_t:
    print ("Zaidima laimejo Petras")
else:
    print('Zaidimas baigesi lygiosiomis')
print('---------sunkesni 8-----------')
# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm.
# Suskaičiuokite kiek reikia smūgių.
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm,
# bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti),
# kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
total_count = 0 # посчёт всех операций по ударам молотком так как он перед фор
for i in range(5):
    count = 0 # посчёт в самом рендже ОБЯЗАТЕЛЬНО
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        taukst = random.randint(5, 20)
        total_taukst += taukst
        count += 1
    total_count += count # сохраняет подсчёт каждого цикла из 5 в фор
    print(f'vini ikalem {count} smugiais, is viso sukalta {total_taukst}mm.')
print(f"is viso prireike {total_count} smugiu.")
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm,
total_count = 0 # посчёт всех операций по ударам молотком так как он перед фор
for i in range(5):
    count = 0 # посчёт в самом рендже ОБЯЗАТЕЛЬНО
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        count += 1
        if random.randint(0, 1) == 0:
            continue
        taukst = random.randint(5, 20)
        total_taukst += taukst
    total_count += count # сохраняет подсчёт каждого цикла из 5 в фор
    print(f'vini ikalem {count} smugiais, is viso sukalta {total_taukst}mm.')
print(f"is viso prireike {total_count} smugiu.")

print("------1.START FROM BEGGINING CAUSE I'M DUMB--------")
#Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę,
# gimimo metus ir šiuos metus (nebūtinai tikrus). Parašykite kodą, kuris pagal
# gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų
# tokį sakinį :"Aš esu Vardenis Pavardenis. Man yra XX metai(ų)"

Name = 'Violet'
Surname = 'Evergarden'
b_year = 1875
today_date = 1893
age = today_date - b_year
print("As esu", Name, Surname, '.Man yra', age, 'metu')
print("------2.START FROM BEGGINING CAUSE I'M DUMB--------")
# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą
# jį suapvalinę iki 2 skaičių po kablelio.
smth = random.randint(0,4)
smth2 = random.randint(0,4)
small = min(smth,smth2)
big = max(smth, smth2)
if small == 0:
    print('not possible division by zero')
else:
    print(F'{big/small:.2F}')

print("------3.START FROM BEGGINING CAUSE I'M DUMB--------")
#Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.
smth = random.randint(0,25)
smth2 = random.randint(0,25)
smth3 = random.randint(0,25)
if smth < smth2 < smth3 or smth3 < smth2 < smth:
    print(smth2)
elif smth3 < smth < smth2 or smth2 < smth < smth3:
    print(smth)
elif smth2 < smth3 < smth or smth3 < smth3 < smth:
    print(smth3)
else:
    print('not possible')
print("------4.START FROM BEGGINING CAUSE I'M DUMB--------")
# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji
# (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti
# trikampį ir atsakymą atspausdintų.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
if a + b > c or c + b > a:
    print("horray it's ok")
else:
    print("po po po")

print("------5.START FROM BEGGINING CAUSE I'M DUMB--------")
# Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija
# sugeneruokite jiems reikšmes nuo 0 iki 2. Suskaičiuokite kiek yra nulių,
# vienetų ir dvejetų. (sprendimui masyvo nenaudoti).
a = random.randint(0,2)
b = random.randint(0,2)
c = random.randint(0,2)
d = random.randint(0,2)
# asking for a,b,c,d for zeros, than asking for a,b,c,d for ones, and ect.
co0 = 0
co1 = 0
co2 = 0
if a == 0:
    co0 += 1
if b == 0:
    co1 += 1
if c == 0:
    co2 += 1
if d == 0:
    co0 += 1
if a == 1:
    co1 += 1
if b == 1:
    co2 += 1
if c == 1:
    co0 += 1
if d == 1:
    co1 += 1
if a == 2:
    co2 += 1
if b == 2:
    co0 += 1
if c == 2:
    co1 += 1
if d == 2:
    co2 += 1
print('zeros:', co0, 'ones:', co1, 'twos', co2)

print("------6.START FROM BEGGINING CAUSE I'M DUMB--------")
# Naudokite funkcija random.randint(x,x).
# Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10.
# Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [],
# 0 -  (), didesni už 0 {}.
a = random.randint(-10,10)
b = random.randint(-10,10)
c = random.randint(-10,10)
if a < 0:
    print(f'[{a}]')
if a == 0:
    print(f'({a})')
if a > 0:
    print('{' + str(a) + '}')
if b < 0:
    print(f'[{b}]')
if b == 0:
    print(f'({b})')
if b > 0:
    print('{' + str(b) + '}')
if c < 0:
    print(f'[{c}]')
if c == 0:
    print(f'({c})')
if c > 0:
    print('{' + str(c) + '}')

print("------7.START FROM BEGGINING CAUSE I'M DUMB--------")
# Įmonė parduoda žvakes po 1 EUR.
# Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida,
# daugiau kaip 2000 vienetų- 4 % nuolaida. Parašykite programą,
# kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių
# ir kokia kaina perkama. Žvakių kiekį generuokite nuo 5 iki 3000.

psc = random.randint(5, 3000)
price = psc * 1
if psc >= 2000: #
    disc = 0.04 # BODY
elif psc >= 1000: # sorting
    disc = 0.03 #
else:
    disc = 0
disc_amount = price * disc #NOT IN PRINT. make for yourself formulas after sorting
total = price - disc_amount
print("How many psc:",psc)
print("TOTAL:", total, 'EUR')

print("------8.START FROM BEGGINING CAUSE I'M DUMB--------")
# Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį.
# Ir aritmetinį vidurkį atmetus tas reikšmes,
# kurios yra mažesnės nei 10 arba didesnės nei 90. Abu vidurkius atspausdinkite.
# Rezultatus apvalinkite iki sveiko skaičiaus.
nr = random.randint(0, 100)# Sukurkite tris kintamuosius
nr2 = random.randint(0, 100)# su atsitiktinėm reikšmėm
nr3 = random.randint(0, 100)# nuo 0 iki 100.
count = 0
s = 0
avg_all = round((nr + nr2 + nr3) / 3) # Paskaičiuokite jų aritmetinį vidurkį.
print(avg_all)
if  nr > 10 and nr < 90:
    s = s + nr
    count += 1
if nr2 > 10 and nr < 90:
    s = s + nr2
    count += 1
if nr3 > 10 and nr < 90:
    s = s + nr3
    count += 1
else:
    print('num not exist')
new_avg = s//count
print(new_avg)

print("------10.START FROM BEGGINING CAUSE I'M DUMB--------")
# Sugeneruokite 6 kintamuosius su atsitiktinem reikšmėm nuo 1000 iki 9999.
# Atspausdinkite reikšmes viename stringe, išrūšiuotas nuo didžiausios iki mažiausios,
# atskirtas tarpais. Naudoti ciklų ir masyvų NEGALIMA.
aa = random.randint(1000,9999)
ss = random.randint(1000,9999)
dd = random.randint(1000,9999)
ff = random.randint(1000,9999)
gg = random.randint(1000,9999)
hh = random.randint(1000,9999)
nums = (aa, ss, dd, ff, gg, hh)
result = sorted(nums, reverse = True) #reverse - atvirksciai
print(*result)

print("------1. 4masyvai--------")
#Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29),
# kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
arr = []  # naaujas tuscias ciklas
for i in range(30):  #Sugeneruokite masyvą iš 30 elementų
    num = random.randint(5, 25) # kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
    arr.append(num)
    print(arr)
print()

print("------2. 4masyvai--------")
# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
# Raskite didžiausią masyvo reikšmę;
# Suskaičiuokite visų reikšmių sumą;
# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
count = 0
num = []
print(arr)
for num in arr:
    if num > 10:
        count += 1
print("kiek skaiciu >10:", count)
big = max(arr)
print("didziause reiksme:", big)
reiksmiu_suma = sum(arr)
print("reikšmių sumą:", reiksmiu_suma)
#Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
new_arr = []
for i in range(len(arr)):
    new_arr.append(arr[i] - i)
print(new_arr)
# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
for i in range(10):
    rr = random.randint(5,25)
    new_arr.append(arr[i] + rr)
print(len(new_arr))
# Iš masyvo elementų sukurkite du naujus masyvus.
# Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
po = []
npo = []
for i in range(len(new_arr)):
    if i % 2 == 0:
        po.append(new_arr[i] - i)
print("poriniai:",po)
for i in range(len(new_arr)):
    if i % 2 != 0:
        npo.append(new_arr[i] - i)
print("neporiniai:",npo)
#Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
print(new_arr)
for i in range(len(new_arr)): # БЕРЕМ МАССИВ ВЕСЬ ПО ЭТОМУ FOR индекс LEN(ГДЕ ИЩЕМ)
    if i % 2 == 0: #ЕСЛИ ЗНАЧЕНИЕ ЧЁТНОЕ
        if new_arr[i] > 15:
            new_arr[i] = 0
print("pakeiciam i 0:", new_arr)
# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
for i in range(len(new_arr)): #БЕРЕМ ЦИКЛ
    if new_arr[i] > 10:       #ИЩЕМ ЗНАЧЕНИЕ
        print("first index:", i) #НАПЕЧАТАЙ НАЙДЕНОЕ ЗНАЧЕИЕ
        break #ПРЕРВИСЬ ЕСЛИ НАШЁЛ

print("------3. 4masyvai--------")
# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D,
# o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės. СКОЛЬКО РАЗ В 200 ПОВТОРЕНИЯХ ПОВТОРЯЮТСЯ А В С и D
arr1 = [] #ДЕЛАЕМ ПУСТОЙ МАССИВ
letters = ["A", "B", "C", "D"] #МАССИВ ИЗ БУКВ
for i in range(200): #генерируем массив ПОДСЧЁТА
    arr1.append(random.choice(letters)) #добавляем рандом
# СОЗДАЁМ ВВОДНЫЕ ДЛЯ ПОМОЩИ
count_A = 0
count_B = 0
count_C = 0
count_D = 0
# ДЕЛАЕМ ЦИКЛ С ПОДСЧЁТАМИ
for letters in arr1:
    random.choice(letters)
    if letters == "A":
        count_A += 1
    if letters == "B":
        count_B += 1
    if letters == "C":
        count_C += 1
    if letters == "D":
        count_D += 1
#НУЖНО ПОКАЗАТЬ СКОЛЬКО РАЗ ПОВТОРЯЮТСЯ A, B, C ir D.
print(count_A, count_B, count_C, count_D)

print("------4. 4masyvai--------")
# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
sorted_arr1 = sorted(arr1)
print(sorted_arr1)
print("------5. 4masyvai--------")
# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą.
# Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių).
# Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.
arr1 = []
arr2 = []
arr3 = []
mass = []
letters = ["A", "B", "C", "D"]
count = 0
for i in range(200): #генерируем массив ПОДСЧЁТА
    arr1.append(random.choice(letters)) #добавляем рандом
    arr2.append(random.choice(letters))
    arr3.append(random.choice(letters))
    combin = arr1[i] + arr2[i] + arr3[i] # из 3 строк берёт 3 значения и получается arr1[А] + arr2[А] + arr1[А] = "ААА"
    mass.append(combin) # ЗАПОЛНЯЕМ МАССИВ mass
uniq_comb = set(mass) # # set инструмент проверки / удаления повторов
print(len(uniq_comb)) # len ПОДСЧЁТ значений
print("------6. 4masyvai--------")
# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999.
# Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
one = []
two = []
while len(one) < 100: #сколько элементов в массиве one / цикл работает, пока
    num = random.randint(100, 999)
    if num not in one:
        one.append(num)
while len(two) < 100:
    num2 = random.randint(100, 999)
    if num2 not in two:
        two.append(num2)

