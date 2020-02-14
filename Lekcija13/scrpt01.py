fibVrednosti = [ 0 : 0, 1 : 1 ]

def fib(n):
    if n in fibVrednosti.keys():
        return fibVrednosti[n]
    else:
        rezultat = fib(n-1) + fib(n-2)
        fibVrednosti[n] = rezultat
        return rezultat

 
rezultat = fib(100)

print(rezultat)
