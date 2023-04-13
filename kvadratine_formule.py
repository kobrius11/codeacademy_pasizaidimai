
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
        diskriminantas = (b ** 2) - 4 * (a * c)

        if diskriminantas == 0:
            x1 = (-b )/ (2 * a)
            return f"x1 = x2:\n {x1: .1f}\n nes diskriminatas = {diskriminantas}"


        elif diskriminantas > 0:
            x1 = (-b - (diskriminantas ** (1/2))) / 2 * a
            x2 = (-b + (diskriminantas ** (1/2))) / 2 * a

            return f"x1 != x2:\n x1={x1: .1f}\n x2={x2: .1f}\n nes diskriminatas = {diskriminantas}"

        elif diskriminantas < 0:

            x1 = complex((-b), - ((-1 * diskriminantas) ** (1/2)))
            x2 = complex((-b), + ((-1 * diskriminantas) ** (1/2)))
            #print(f"{x1 / (2* a): .4f}, {x2 / (2* a): .4f}")

            return f'sprendiniu realiuju skaiciu aibeje nera, nes diskriminantas = {diskriminantas}, kompleksiniai sprendimai:\n x1 = {x1 / (2* a): .4f}\n x2 = {x2 / (2* a): .4f}'
    

print(kvadratine_formule()) 

# tolesni veiksmai:
# padaryt kad sprestu D < 0 (kompleksines) lygtis - baigta
# padaryt kad funkcija priimtu argumentus, jei argumentu nera prasytu ivesti input 