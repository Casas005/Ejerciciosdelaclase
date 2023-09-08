#------------------------------------------------------------------
# 1- Suma de los numeros

def productorio(n):
    producto = 0

    for i in range (1, n + 1):
        producto = producto + i

    return producto

n = int(input())

print(productorio(n))

#-------------------------------------------------
# 2- leer numeros indefinidamente y que de el promedio
import statistics

lista = [0]
while(True):
    i = float(input())

    if i != 0:
        lista.insert(0,i)
    else:
        break
prom = sum(lista) / len(lista)

print(prom)

#------------------------------------------------------
# 3- lista de compras alfabeticamente 
compras = []
num = int(input('numero de articulos: '))

for i in range(num):
    art = str(input('articulo: '))
    compras.insert(0,art)

compras.sort()
print(compras)

#---------------------------------------------------------
# 4- Numeros pares
num = int(input('dame un numero: '))

list = []

for i in range(0, num, 2):
    if i % 2 == 0:
        list.insert(-1,i)
    else:
        break
print(list)

#--------------------------------------------------------------
# 5- Vocales
def obtener_vocales(frase):
    vocales = 'aeiouAEIOU'

    return [ c for c in frase if c in vocales]


texto = str(input())

print(obtener_vocales(texto))

#-------------------------------------------------------------------
# 6- si es divisible entre 243
def div(numero):
    if numero % 243 == 0:
        print("es divisible")
    else:
        print('no es divisible')
    return numero


n = int(input())


print(div(n))

#--------------------------------------------------
# 7- multiplicar strings
def multiplicarString(word):
    word = str(input())
    n = int(input())
    new = word * n
    print(new) 
    return new


print(multiplicarString('word'))