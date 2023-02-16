def extra_ennymerate(x):
    frac, cum = 0, 0
    for i in range(len(x)):
        cum += x[i]
        frac = cum/sum(x)
        yield 0, x[i] , cum , frac
x = [1,3,4,2]
for i, elem, cum, frac in extra_ennymerate(x):
    print(elem, cum, frac)