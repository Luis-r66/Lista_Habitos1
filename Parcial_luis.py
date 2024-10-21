habitos = []

def agregar_habito(nombre, frecuencia, duracion):
    global habitos
    habito = [nombre, frecuencia, duracion]
    habitos.append(habito)
    ordenar_habitos()
    actualizar_matriz()
    print(f"Hábito '{nombre}' agregado.")

def eliminar_habito(nombre):
    global habitos
    for habito in habitos:
        if habito[0] == nombre:
            habitos.remove(habito)
            actualizar_matriz()
            print(f"Hábito '{nombre}' eliminado.")
            return
    print(f"Hábito '{nombre}' no encontrado.")

def mostrar_habitos():
    if habitos:
        print("Hábitos:")
        for habito in habitos:
            print(f"[Nombre: {habito[0]}, Frecuencia: {habito[1]} veces/semana, Duración: {habito[2]} minutos]")
    else:
        print("No hay hábitos registrados.")

def actualizar_matriz():
    n = len(habitos)
    matriz_habitos = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz_habitos[i][j] = min(habitos[i][1], habitos[j][1])
            else:
                matriz_habitos[i][i] = habitos[i][1]

def ordenar_habitos():
    global habitos
    if habitos:
        habitos = merge_sort(habitos)
        print("Hábitos ordenados por nombre:")
        mostrar_habitos()
    else:
        print("No hay hábitos registrados para ordenar.")

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        merge_sort(izquierda)
        merge_sort(derecha)
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i][0] < derecha[j][0]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

def main():
    while True:
        print("\nMenú:")
        print("1. Ingresar hábito")
        print("2. Eliminar hábito")
        print("3. Mostrar hábitos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del hábito: ")
            frecuencia = int(input("Ingrese la frecuencia del hábito (por semana): "))
            duracion = int(input("Ingrese la duración del hábito (en minutos): "))
            agregar_habito(nombre, frecuencia, duracion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito a eliminar: ")
            eliminar_habito(nombre)
        elif opcion == "3":
            mostrar_habitos()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
