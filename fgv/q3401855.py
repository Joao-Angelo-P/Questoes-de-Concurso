# Ao executar o código, os valores impressos são
def x(d):
    m = 10000
    dv = 100>>2
    #print(dv)
    match d:
        case [a, du] if a<m:
            return a*10*du/dv
        case [a, du] if a>=m:
            return a*20*du/dv
print ("R1 = ", x([6000,5]), " e R2 = ", x([15000,3]))

