# Crear un programa que solicite la calificacion de 15 alumnos 
# e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
reprobados = 0

for Numalumn in range(1, 16):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación del alumno {Numalumn}: "))
            if 0 <= calificacion <= 10: 
                break
            else:
                print("La calificación debe estar entre 0 y 10. Ingresa otro número.")
        except ValueError:
            print("Ingresa un número válido.")

    if calificacion >= 6:
        aprobados += 1
    else:
        reprobados += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")

x=33