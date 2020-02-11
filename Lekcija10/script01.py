def faktorijel(n):
    if n == 0:
        return 1
    else:
        return n * faktorijel(n-1)

rezultat = faktorijel(25206)

print(rezultat)
