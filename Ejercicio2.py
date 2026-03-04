def leer_datos():
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    return base, altura
    
def calcular_area(base, altura):
    return (base * altura)/2

base , altura = leer_datos()
area = calcular_area(base, altura)
print(f"El area del rectangulo es: {area}")