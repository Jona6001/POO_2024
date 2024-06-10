# Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

porcentaje = float(input("Introduce el porcentaje que deseas obtener (sin el signo %): "))
num = float(input("Introduce el número del cual deseas obtener el resultado: "))

def calcular_porcentaje(porcentaje, num):
    return (porcentaje / 100) * num
resultado = calcular_porcentaje(porcentaje, num)

print(f"{porcentaje}% de {num} es: {resultado}")
