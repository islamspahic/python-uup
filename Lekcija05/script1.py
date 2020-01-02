import math

aX = float(input("Unesite X kordinatu tacka A: "))
aY = float(input("Unesite Y kordinatu tacka A: "))
bX = float(input("Unesite X kordinatu tacka B: "))
bY = float(input("Unesite Y kordinatu tacka B: "))
cX = float(input("Unesite X kordinatu tacka C: "))
cY = float(input("Unesite Y kordinatu tacka C: "))

if aX < bX and aY > bY:
    print("Tacka A je levo gore u odnosu na tacku B, pa program moze da nastavi.")
    
    if aX < cX < bX and aY > cY > bY:
        print("Tacka C jeste unutar pravougaonika uokvirenog tackama A i B")

        if math.hypot(aX - cX, aY - cY) < math.hypot(bX - cX, bY - cY):
            print("Tacka C je bliza tacki A")
        elif (aX - cX, aY - cY) == math.hypot(bX - cX, bY - cY):
            print("Tacka C je podjednako udaljena od tacaka A i B")
        else:
            print("TackaC je bliza tacki B")
        
    else:
        print("Tacka C nije unutar pravougaonika uokvirenog tackama A I B i program ne moze da nastavi")
        
else:
    print("Program ne moze da nastavi,jer tacka A nije levo gore u odnosu na tacku B.")
     

     
