lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

resultado = map(lambda x, y, z: x + y + z, lista1, lista2, lista3)
print(list(resultado))

# Describir paso a paso lo que hizo la función Map junto con la función lambda de acuerdo con la siguiente línea de código. 

# map toma el primer elemento de cada lista, los pasa a la funcion lambda y esta los suma, luego el segundo elemento de cada lista, los suma y así sucesivamente. 
# El resultado es una nueva lista con la suma de los elementos correspondientes de las tres listas.