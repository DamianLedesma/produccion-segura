print ('Introduce 25 números. Pulsa enter después de introducir cada número:')

# Crear una lista de 25 números por input:
numeros = []
while len(numeros) < 25:
    numeros.append(input())
######

# Convertir elementos de la lista a ints:
numeros = [int(x) for x in numeros]
#####

# Funciones para calcular máximo y el mínimo en la lista:
def numero_maximo (lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max

def numero_minimo (lista):
    min = numero_maximo (lista)
    for i in lista:
        if i < min:
            min = i
    return min
#####

# Calcular los pares e impares de la lista:
pares = 0
for i in numeros:
    if i % 2 == 0:
        pares+=1

impares = len(numeros) - pares
#####

# Almacenar los números primos de la lista en lista primos:
primos = []
for i in numeros:
    x = 2
    while x < i:
        if i % x == 0 and x != i:
            x = i
        if i % x != 0:
            x+=1
            if i % x == 0 and x == i:
                primos.append(i)
                x = i
#####

# Fórmula para calcular número factorial
def factorial (numero):
    x = 1
    resultado = numero
    while x < numero:
        resultado = x * resultado
        x += 1
    return resultado
#####

print ('La edad mayor de la clase es', numero_maximo(numeros))
print ('La edad menor de la clase es', numero_minimo(numeros))
print ('Hay', pares, 'números pares.')
print ('Hay', impares, 'números impares.')
print ('El número factorial de', numero_maximo(primos), "(el número primo mayor de la lista), es", factorial(numero_maximo(primos)))
