"""
DEFENSORIA PÚBLICA DO ESTADO DE RONDÔNIA
Questão 45
A linguagem Python oferece como recurso a função lambda, ele é
uma ferramenta poderosa que permite que os programadores
criem funções anônimas, ou seja, sem necessidade de nomeá-las.
Analise o código Python abaixo

def myf(n):
  return lambda a : a * a / -n

myx = myf(2)
myy = myf(-3)

print('A= ',myx(12-1), 'e B= ',myy(13-1))

Ao executar o código, os valores impressos são:
(A) A= 22.0 e B= -36.0.
(B) A= -24.0 e B= 39.5.
(C) A= -60.5 e B= 48.0.
(D) A= 288.0 e B= -507.5.
(E) A= 1728.0 e B= -2197.0.
"""

def myf(n):
  return lambda a : a * a / -n

myx = myf(2)
myy = myf(-3)

print('A= ',myx(12-1), 'e B= ',myy(13-1))
