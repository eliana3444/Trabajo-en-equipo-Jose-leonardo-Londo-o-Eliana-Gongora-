def pares(n, m):
    if n <= 0 or m <= 0 or n >= m:
        raise Exception("No es posible continuar con la operación")
    
    for i in range(n, m + 1):
        if i % 2 == 0:
            yield i
            
print("Ingrese dos numeros enteros positivos, el primero menor que el segundo.")
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))
generador_pares = pares(n, m)
print(f"Los numeros pares entre {n} y {m} son:")
for numero in generador_pares:
    print(numero)