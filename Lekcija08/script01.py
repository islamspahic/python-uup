tajniBroj = 51
broj = 2

while tajniBroj != broj:
    broj = int(input("Pogodite tajni broj: "))

    if tajniBroj == broj:
        print("Pogodak!")
    elif tajniBroj < broj:
        print("Tajni broj je manji od tog broja.")
    else:
        print("Tajni broj je veci od tog broja.")

print("Kraj programa")        
