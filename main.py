import json

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        calificaciones = input(f"Ingrese las calificaciones de {nombre} separadas por comas: ")
        try:
            lista_calificaciones = list(map(float, calificaciones.split(',')))
            estudiantes[nombre] = lista_calificaciones
        except ValueError:
            print("Error: ingrese solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(calificaciones)/len(calificaciones) for nombre, calificaciones in estudiantes.items()}
    return promedios

def obtener_mejor_estudiante(promedios):
    return max(promedios, key=promedios.get)

def guardar_en_archivo(estudiantes, promedios, mejor_estudiante):
    with open('resultados.txt', 'w') as f:
        f.write("Resultados de los estudiantes:\n")
        for nombre in estudiantes:
            f.write(f"{nombre}: Calificaciones: {estudiantes[nombre]}, Promedio: {promedios[nombre]:.2f}\n")
        f.write(f"\nEl mejor estudiante es: {mejor_estudiante} con promedio {promedios[mejor_estudiante]:.2f}")

def main():
    estudiantes = ingresar_datos()
    if estudiantes:
        promedios = calcular_promedios(estudiantes)
        mejor_estudiante = obtener_mejor_estudiante(promedios)
        guardar_en_archivo(estudiantes, promedios, mejor_estudiante)
        print("Datos guardados en resultados.txt")
    else:
        print("No se ingresaron datos.")

if __name__ == "__main__":
    main()
