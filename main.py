#print(str("sveiki"))

x = 5 #int(5)
y = 6.0 #float(6)
z = 1 + 0j #complex(1)

#print(type(a), type(b), type(c))
#print(a, b, c)

# ats1 = a + b
# ats2 = a - b
# ats3 = a * b * a
# ats4 = a / b
# ats5 = a**b


# 1, 2 uzduotis
def uzduotis(a, b):
    ats1 = a + b
    ats2 = a - b
    ats3 = a * b * a
    ats4 = a / b
    ats5 = a**b
    return ats1, ats2, ats3, ats4, ats5

#print(uzduotis(x, y))


# trecia uzduotis
ats1 = x // y
ats2 = x % y
#print(ats1, ats2)

#05_logines_salygos_operatoriai
def pirma_uzdt(skaicius):
    if skaicius % 2 == 0:
        #print('lyginis')
        return True
    else:
        #print('Nelyginis')
        return False

def antra_uzdt(skaicius):
    if 5 <= skaicius <= 10:
        print("Skaičius yra tarp 5 ir 10")
    else:
        print("Skaičius nera tarp 5 ir 10")

def trecia_uzdt(skaicius1, skaicius2):
    if skaicius1 > 0 and skaicius2 > 0:
        print("abu skaiciai yra didesni uz 0")
    elif skaicius1 > 0 or skaicius2 > 0:   
        print('bent vienas skaicius nera didesnis uz 0')
    else:
        print('neivienas skaicius nera didesnis uz 0')

def ketvirta_uzdt(skaicius1, skaicius2):
    # jei abu True
    if pirma_uzdt(skaicius1) and pirma_uzdt(skaicius2):
        print("abu skaiciai lyginiai")
    # jei bent vienas True
    elif pirma_uzdt(skaicius1) or pirma_uzdt(skaicius2):   
        print('bent vienas skaicius yra nelyginis')
    # jei neivienas True
    else:
        print('neivienas skaicius nera lyginis')




# try:
#      x = int(input('skaicius: '))
#      #pirma uzduotis
#      print('Lyginis ?: ',  pirma_uzdt(x))
#      #antra uzduotis
#      antra_uzdt(x)
#      #trecia uzduotis
#      trecia_uzdt(1, 1)
#      #ketvirta uzduotis
#      ketvirta_uzdt(1, 1) 
# except:
#     print('ivestas ne naturalusis skaicius!')


#06_simboliu_eilutes_ju_metodai

def kada_sukaks_100(skaicius):
    return 2023 + 100 - skaicius

def ugis():
    cm = int(input("cm: "))
    ugis_m = cm / 100
    return {"ugis metrais ": ugis_m}, {"ugis_cm ": cm}

def atlyginimas():
    x = float(input('atlyginimas: '))
    return f'alga ant popieriaus, {x}, alga i rankas: {x - (x * 0.21)}, mokestis: , {21} %'
#antra
knygos_pavadinimas = 'Nikas Deinas'
#pirma
def simboliu_eilute():
    x = str(input('tekstas: '))
    return x, x[0], x[-1]
#trecia
citata = 'Nereikia gyventi baimeje'
#ketvirta
def du_zodziai():
    zodis1 = str(input('tekstas: '))
    zodis2 = str(input('tekstas: '))
    return str(zodis1[0] + '-' + zodis2[0])

#devinta
def vertimas_i_c(far):
    return (far - 32) / 1.8
def vertimas_i_far(c):
    return (c * 1.8) + 32

lst = [i for i in range(0, 10)]
def list_reverse(list):
    new = []
    for i in range(len(list)):
        new.append(list[-1 -i])
    return new
try:
    #pirma uzduotis
    #print(simboliu_eilute())
    
    #antra uzduotis
    #print(knygos_pavadinimas[:5])


    #trecia uzduotis
    #print(citata[:3])

    #ketvirta uzduotis
    #print(du_zodziai())


    #penkta uzduotis
    #vardas = str(input("vardas: "))
    #amzius = int(input("Amzius: "))

    #sesta uzduotis
    #print(kada_sukaks_100(amzius))

    #septinta uzduotis
    #print(ugis())

    #astunta uzduotis
    #print(atlyginimas())

    #devinta uzduotis
    # print('\u6666')
    # pasirinkimas = str( input("verciam i celcijus ?: "))
    # if pasirinkimas == 'taip':
    #      print( vertimas_i_c( float( input("iveskite far: "))))
    # else:
    #      print( vertimas_i_far( float( input("iveskite c: "))))


    print(list_reverse(lst))
except:
    print("Kazkas netaip")

#Mildos užduotėlė
klausimas = input("Laba diena, koks tavo vardas?")
print("Labas! " + klausimas)