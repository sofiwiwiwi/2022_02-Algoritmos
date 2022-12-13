cantidad_dinero = int(input())
denominaciones = int(input())
monedas = []

#este for rellena el arreglo de denominaciones de la moneda
for i in range(denominaciones):
    moneda = int(input())
    monedas.append(moneda)

"""
¿Cuál es el nombre de la función?: 
    "cambio"
¿Cuáles son los parámetros de la función?:
    - n: la cantidad de dinero a la que hay que dar cambio
    - monedas: lista con las denominaciones posibles 
¿Qué hace la función?:
    evalúa entre el mínimo de la cantidad de monedas que se tienen para dar cambio hasta el minuto, y con la de usar
    otras denominaciones utilizando fuerza bruta recursiva
¿Qué retorna la función?
    cuando ve todos los casos posibles, retorna la mínima cantidad de monedas para dar cambio al valor n
"""
def cambio(n, monedas):
    #caso base
    if n == 0:
        return 0
    else:
        #como queremos minimizar, primero hacermos que el resultado sea lo mas grande posible
        result = float('inf')
        for moneda in monedas:
            if(moneda <= n):
                #llama recursivamente hasta que tengamos todo el cambio
                result = min(result, cambio(n-moneda, monedas) + 1)
    return result

print(cambio(cantidad_dinero, monedas))
        

