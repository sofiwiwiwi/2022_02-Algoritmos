n = int(input())
ciudades_norte = []
ciudades_sur = []

for i in range(n):
    ciudades_norte.append(input())

for i in range(n):
    ciudades_sur.append(input())

#se crea una matriz como almacenamiento para programacion dinamica
matriz = [[0 for i in range(n+1)] for j in range(n+1)]

def puentes(norte, sur):
#se rellena la matriz con el largo de la secuencia más larga hasta ese caracter
    for i in range(n+1):
        matriz[i][0] = 0

    for j in range(n+1):
        matriz[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if norte[i-1] == sur[j-1]:
                #si los caracteres coinciden, se suma uno al valor que se tenía hasta el caracter anterior
                matriz[i][j] = matriz[i-1][j-1] + 1
            else:
                #si los caracteres no coinciden, es el mayor entre la casilla a la derecha y la casilla a la izquierda
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])

    cantidad = matriz[n][n]
    ciudades_con_puente = []

    i = n
    j = n

#se comienza desde el final de la matriz rellenada anteriormente
    while i > 0 and j > 0:
        #si estos caracteres son iguales, entonces son parte de la secuencia más larga encontrada
        if norte[i-1] == sur[j-1]:
            ciudades_con_puente.append(norte[i-1])
            i -= 1
            j -= 1
        #si no son iguales, la secuencia viene de otro lado
        elif matriz[i-1][j] > matriz[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    #como es iteración bottom-up, se guarda al revez, así que des-hacemos el cambio
    ciudades_con_puente = ciudades_con_puente[::-1]
    
    retorno = (cantidad, ciudades_con_puente)
    
    return retorno

cantidad_puentes, ciudades_con_puente = puentes(ciudades_norte, ciudades_sur)
lista_ciudades = list(ciudades_con_puente)

print(cantidad_puentes)
for i in range(cantidad_puentes):
    print(lista_ciudades[i])