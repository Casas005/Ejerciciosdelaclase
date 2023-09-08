# 1- un programa que lea 2 numeros e imprima True si el primero es 20 veces el valor del segundo.

a = int(input("Dame el primer numero:  "))
b = int(input("Dame el segundo numero:  "))

print(a == (b * 20))

#------------------------------------------------------------------------------------

# 2- un programa que lea tres numeros e imprima el producto de los tres divido por la suma de los tres.

a = int(input("Dame el primer numero:  "))
b = int(input("Dame el segundo numero:  "))
c = int(input("Dame el tercer numero:  "))

print((a * b * c)/ (a + b + c))

#---------------------------------------------------------------------------------------

# 3- un programa que lea 3 numeros e impria true si estan en orden ascendiente.

a = int(input("dame el primer numero:  "))
b = int(input("dame el segundo numero:  "))
c = int(input("dame el tercero numero:  "))

print(a <= b <= c)


#------------------------------------------------------------------------------------------

# 5- un numero que si es par imprima True y si es impar imprima False.
numero = int(input("Ingrese un número: "))

print((numero % 2) == 0)


#----------------------------------------------------------------------------------------------------------------------

# 6- un programa que lea 3 numero y que imprima True si el primero es menor al segundo y si el segundo no es igual al tercero.

a = int(input("dame el primer valor: "))
b = int(input("dame el segundo valor: "))
c = int(input("dame el tercer valor: "))


print((a < b != c) == True )

#------------------------------------------------------------------------------------------------------------------------------------------

# 7- un programa que lea 3 números e imprima True si el primer y el segundo son iguales o si el primero es almenos 3 unidades mas grande que el segundo.

a = int(input("dame el primer valor: "))
b = int(input("dame el segundo valor: "))



print( (a == b) or (a >= (b + 3)) )

#-------------------------------------------------------------

# 8- un programa que lea 8 numero y los promedie

a = int(input("dame el primer valor: "))
b = int(input("dame el segundo valor: "))
c = int(input("dame el tercer valor: "))
d = int(input("dame el cuarto valor: "))
e = int(input("dame el quinto valor: "))
f = int(input("dame el sexto valor: "))
g = int(input("dame el septimo valor: "))
h = int(input("dame el octavo valor: "))

print((a + b + c + d + e + f + g + h)/8  ) 

#-----------------------------------------------------------------------
# 9- un programa que lea 4 strings y los concatene

a = str(input("dame una palabra:  "))
b = str(input("dame otra palabra:  "))
c = str(input("dame otra palabra:  "))
d = str(input("dame otra palabra:  "))

print(a + b + c + d)

#-----------------------------------------------------------
# 10- Sandia

a = int(input(" Dame el Peso de la Sandia:  "))

print((a % 2) == 0)


