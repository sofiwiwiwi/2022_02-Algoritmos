soluciones = []
suma_deseada = 0
num_disponibles = []
conjuntito = []

"""
¿Cuál es el nombre de la función?: 
    "suma"
¿Cuáles son los parámetros de la función?:
    - t: entero para el cual se deben encontrar las sumas
    - usa: lista de enteros con los cuales podemos hacer las sumas
    - sol: lista vacía en la cual iremos agregando las soluciones
¿Qué hace la función?:
    Añade número de la lista usa a la solución y luego revisa si es factible. Si no lo es lo elimina y sigue con el siguiente 
    número en usa.
¿Qué retorna la función?
    En este caso, como usamos backtracking recursivo, la función al retornar se llama a sí misma con un cambio en los parámetros, hasta que llega al caso base.
"""
def suma(t, usa, sol):
    if sum(sol) == t:
        sol.sort()
        sol.reverse()
        if sol not in conjuntito:
            conjuntito.append(sol)
        return   
    if len(usa) == 0 or sum(sol) > t:
        return
    
    sol.append(usa[0])
    suma(t, usa[1:], sol[:])

    sol.pop()
    suma(t, usa[1:], sol[:])

#Entramos en un loop while que termina una vez recibimos todos los inputs a calcular con la función "suma"
while(1):
    linea = input()
    valores = linea.split(' ')
    nums = [eval(i) for i in valores]
    if nums[1] == 0:
        break

    suma_deseada = nums[0]
    soluciones.clear()
    num_disponibles.clear()
    num_disponibles +=  nums[2:]
    print("Suma de "+ str(suma_deseada) + ":")
    suma(suma_deseada, num_disponibles, soluciones)
    conjuntito.sort()
    conjuntito.reverse()
    for sol in conjuntito:
        s=""
        if len(sol) == 1:
            print(sol[0])

        elif len(sol) > 1:
            for x in sol:
                s+=(str(x)+"+")
            print(s[0:len(s)-1]) 
    if len(conjuntito) == 0:
        print("NADA")
    conjuntito.clear()