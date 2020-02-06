def min2Broja(a, b):
    if a < b:
        return a
    else:
        return b

def min3Broja(a, b, c):
    return min2Broja(min2Broja(a, b), c)

prviBroj  = float(input("Unesite 1. broj: "))
drugiBroj = float(input("Unesite 2. broj: "))
treciBroj = float(input("Unesite 3. broj: "))

manjiOdPrvaDvaITreceg = min3Broja(prviBroj, drugiBroj, treciBroj)

print("Najmanji od ta 3 je: " + str(manjiOdPrvaDvaITreceg))
