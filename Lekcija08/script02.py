iznos = int(input("Unesite iznos: "))

zaIsplatuod5000 = 0
zaIsplatuod2000 = 0
zaIsplatuod1000 = 0
zaIsplatuod500 = 0
zaIsplatuod200 = 0
zaIsplatuod100 = 0
zaIsplatuod50 = 0
zaIsplatuod20 = 0
zaIsplatuod10 = 0
zaIsplatuod5 = 0
zaIsplatuod2 = 0
zaIsplatuod1 = 0
 
while iznos >= 5000:
    iznos -= 5000
    zaIsplatuod5000 += 1

while iznos >= 2000:
    iznos -= 2000
    zaIsplatuod2000 += 1

while iznos >= 1000:
    iznos -= 1000
    zaIsplatuod1000 += 1
 
while iznos >= 500:
    iznos -= 500
    zaIsplatuod500 += 1

while iznos >= 200:
    iznos -= 200
    zaIsplatuod200 += 1

while iznos >= 100:
    iznos -= 100
    zaIsplatuod100 += 1

while iznos >= 50:
    iznos -= 50
    zaIsplatuod50 += 1

while iznos >= 20:
    iznos -= 20
    zaIsplatuod200 += 1

while iznos >= 10:
    iznos -= 10
    zaIsplatuod10 += 1
    
while iznos >= 5:
    iznos -= 5
    zaIsplatuod5 += 1

while iznos >= 2:
    iznos -= 2
    zaIsplatuod2 += 1

while iznos >= 1:
    iznos -= 1
    zaIsplatuod1 += 1

if zaIsplatuod5000 > 0:
    print("Treba isplatiti od 5000 din x " + str(zaIsplatuod5000))

if zaIsplatuod2000 > 0:
    print("Treba isplatiti od 2000 din x " + str(zaIsplatuod2000))
    
if zaIsplatuod1000 > 0:
    print("Treba isplatiti od 1000 din x " + str(zaIsplatuod1000))

if zaIsplatuod500 > 0:
    print("Treba isplatiti od 500 din x " + str(zaIsplatuod500))

if zaIsplatuod200 > 0:
    print("Treba isplatiti od 200 din x " + str(zaIsplatuod200))
    
if zaIsplatuod100 > 0:
    print("Treba isplatiti od 100 din x " + str(zaIsplatuod100))

if zaIsplatuod50 > 0:
    print("Treba isplatiti od 50 din x " + str(zaIsplatuod50))

if zaIsplatuod20 > 0:
    print("Treba isplatiti od 20 din x " + str(zaIsplatuod20))
    
if zaIsplatuod10 > 0:
    print("Treba isplatiti od 10 din x " + str(zaIsplatuod10))

if zaIsplatuod5 > 0:
    print("Treba isplatiti od 5 din x " + str(zaIsplatuod5))

if zaIsplatuod2 > 0:
    print("Treba isplatiti od 2 din x " + str(zaIsplatuod2))
    
if zaIsplatuod1 > 0:
    print("Treba isplatiti od 1 din x " + str(zaIsplatuod1))
    

