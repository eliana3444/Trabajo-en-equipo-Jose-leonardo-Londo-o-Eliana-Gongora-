def sumatoria (num):
    if num== 1:
        return 1
    else :
        return num+sumatoria(num-1)
    
num=15
print(f"La sumatoria de los numeros entre 1 y {num} es: {sumatoria(num)}")