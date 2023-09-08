import math 

pi = 3.14169

newpi = math.floor(pi)
oldpi = math.ceil(pi)

print(newpi)
print(oldpi)
#-----------------------------------------------
import random

x = int(input())
y = int(input())

ran = random.randint(x,y)

print(ran)
#-----------
import random
def rng(a,b):
    return random.randint(a,b)


x = int(input())
y = int(input())


for i in range(1):
    randomnumber = rng(x,y)
    print(randomnumber)

#------------------------------------------------------------------------

def max(a,b):
    return math.gcd(a,b)

import math


def rng(a,b):
    return math.floor(a/b)

print(rng(6.4,78.1))
#-------------------------------------------------------------
import math

def areac(radio):
    area = (math.pi) * (radio ** 2)

    return area

print(areac(3))
#-----------------------------------------------------------
def productorio(n):
    producto = 1

    for i in range (1, n + 1):
        producto = producto * i

    return producto

print(productorio(4))
