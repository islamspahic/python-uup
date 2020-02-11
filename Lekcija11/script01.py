def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
for i in range(0, 11):
        rezultat = fibonaci(i)
        print(rezultat)


                        
