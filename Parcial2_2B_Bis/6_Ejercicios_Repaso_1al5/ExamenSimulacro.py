def capturar_datos():
    estudiantes = []

    while True:
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        parciales = []
        for i in range(1, 4):
            calificacion = float(input(f"Calificación del parcial {i}: "))
            parciales.append(calificacion)
        proyecto_final = float(input("Calificación del proyecto final: "))
        
        estudiante = {
            'nombre': nombre,
            'carrera': carrera,
            'parciales': parciales,
            'proyecto_final': proyecto_final
        }
        estudiantes.append(estudiante)
        continuar = input("¿Deseas otra captura? (SI/NO): ").strip().upper()
        if continuar != 'si':
            break
    return estudiantes

def calcular_promedio_parciales(parciales):
    return sum(parciales) / len(parciales)
def calcular_calificacion_final(promedio_parciales, proyecto_final):
    return 0.6 * promedio_parciales + 0.4 * proyecto_final
def imprimir_resultados(estudiantes):
    for estudiante in estudiantes:
        nombre = estudiante['nombre']
        carrera = estudiante['carrera']
        parciales = estudiante['parciales']
        proyecto_final = estudiante['proyecto_final']
        
        promedio_parciales = calcular_promedio_parciales(parciales)
        calificacion_final = calcular_calificacion_final(promedio_parciales, proyecto_final)
        print("\n")
        print(f"Estudiante: {nombre}")
        print(f"Carrera: {carrera}")
        print(f"Promedio de parciales: {promedio_parciales:.2f}")
        print(f"Calificación final: {calificacion_final:.2f}")
        if calificacion_final < 80 and proyecto_final > 50:
            print("Presenta examen extraordinario")
    
if __name__ == "__main__":
    estudiantes = capturar_datos()
    imprimir_resultados(estudiantes)

