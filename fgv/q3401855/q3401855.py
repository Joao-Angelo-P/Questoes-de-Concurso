# enunciado abaixo entre aspas duplas
"""
DEFENSORIA PÚBLICA DO ESTADO DE RONDÔNIA
Questão 46
Analise o código Python abaixo

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

Ao executar o código, os valores impressos são
(A) R1 = 3000.0 e R2 = 9000.0.
(B) R1 = 6000.0 e R2 = 9000.0.
(C) R1 = 6000.0 e R2 = 18000.0.
(D) R1 = 12000.0 e R2 = 36000.0.
(E) R1 = 50000.0 e R2 = 150000.0.
"""
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
