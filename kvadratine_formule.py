
def kvadratine_formule():
    #a*x**2 + b*x + c = 0
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        return "ivestas ne skaicius!"
    else:

        x1 = None
        x2 = None
    
        #diskriminantas = b**2 - 4ac
        diskriminantas = (b**2) - 4*(a*c)

        if diskriminantas == 0:
            x1 = (-b )/ (2*a)
            return f"x1 = x2: {x1: .1f}, nes diskriminatas = {diskriminantas}"


        elif diskriminantas > 0:
            x1 = (-b - (diskriminantas**(1/2))) / 2*a
            x2 = (-b + (diskriminantas**(1/2))) / 2*a

            return f"x1 != x2: x1={x1: .1f}, x2={x2: .1f}, nes diskriminatas = {diskriminantas}"

        elif diskriminantas < 0:
            return f'sprendiniu realiuju skaiciu aibeje nera, nes diskriminantas = {diskriminantas}'
    

print(kvadratine_formule()) 

# tolesni veiksmai:
# padaryt kad sprestu D < 0 (kompleksines) lygtis
# padaryt kad funkcija priimtu argumentus, jei argumentu nera prasytu ivesti input 