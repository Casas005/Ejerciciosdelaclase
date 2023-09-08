# 1 Que introduzca un mes y que te de la cantidad de dias

def main():
    dias_mes = {
        "Enero": 31,
        "Febrero": 28,
        "Marzo": 31,
        "Abril": 30,
        "Mayo": 31,
        "Junio": 30,
        "Julio": 31,
        "Agosto": 31,
        "Septiembre": 30,
        "Octubre": 31,
        "Noviembre": 30,
        "Diciembre": 31
    }

    mes = input("Dame el mes: ")

    
    if mes in dias_mes:
        dias = dias_mes[mes]
        print(f"El mes de {mes} tiene {dias} días.")
    else:
        print("no existe")

if __name__ == "__main__":
    main()
 #----------------------------------------------------------------------
# 2 Intruduzca el dia de la semana y que de la posicion 

def main():
    dias_semana = {
        "Lunes": 1,
        "Martes": 2,
        "Miercoles": 3,
        "Jueves": 4,
        "Viernes": 5,
        "Sabado": 6,
        "Domingo": 7,
    }

    semana = input("Dame el dia de la semana: ")

    
    if semana in dias_semana:
        dias = dias_semana[semana]
        print(f"El dia {semana} esta en la posicion {dias} de la semana.")
    else:
        print("no existe")

if __name__ == "__main__":
    main()

#--------------------------------------------------------------------------
# 3 año bisiesto
año = int(input("dame un año:  "))

if( año % 4 == 0 and año % 100 != 0) or año % 400:
    print("El año es bisiesto")
else:
    print("no es bisieto")

#------------------------------------------------------------
# 4 datos de un numero par negativo y mayor a 100
numero = int(input("Dame un numero: "))

numeropar = numero

if (numeropar % 2 == 0):
    numeropar = "par"
else:
    numeropar = "impar"

negativo = numero

if (negativo < 0):
    negativo = "negativo"
else:
    negativo = "positivo"

mayor = numero

if (mayor > 100):
    mayor = "mayor"
else:
    mayor = "menor"


print(f"el numero {numero}, es {numeropar}, es {negativo}, es {mayor} a 100")

#---------------------------------------------------------------------------------------
# 5 Ordenar las notas musicales de una cierta forma
notas = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]

print(notas)

notas.remove("Mi")
notas.remove("Fa")
notas.remove("La")
notas.remove("Si")
notas.insert(0, "Si")
notas.insert(0,"Si")
notas.insert(3, "Re")
notas.insert(5,"Do")
notas.insert(6,"Si")
notas.insert(7,"La")
notas.insert(8,"Sol")
notas.insert(10,"Si")
notas.insert(11,"Si")
notas.insert(12,"La")
notas.insert(13,"La")

print(notas)

#----------------------------------------------------------------
# 6 Lista de nombre
nombre = ["Jose Miguel", "Carlos", "Manuel", "Memo"]

nom = str(input("Dame un nombre que aparezca en la lista:  "))

if (nombre.index(nom)):
    print("True")
else: 
    print("False")

#---------------------------------------------------------------
# 7 ordenar los numeros
lista = [12, 456, 2, 123]

print(lista)

lista.sort()

print(lista)
#-----------------------------------------------------------------
# 8 palindromo 
a = int(input("Dame un elemento: "))
b = int(input("Dame un elemento: "))
c = int(input("Dame un elemento: "))
d = int(input("Dame un elemento: "))
e = int(input("Dame un elemento: "))

lista = [a, b, c, d, e]
alreve = [e, d, c, b, a]

print (lista)

print(alreve)

print(lista == alreve)
