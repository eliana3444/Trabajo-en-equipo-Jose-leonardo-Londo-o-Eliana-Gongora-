es_positivo = lambda x: x > 0
es_negativo= lambda x: x < 0
numeros =[1,7,5,3,2,4,8,-2,-7,-10]
positivos = list(filter(es_positivo,numeros))
negativos= list(filter(es_negativo,numeros))
print(positivos,negativos)