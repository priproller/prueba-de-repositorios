
print("==============================")
print("       BÓVEDA DIGITAL")
print("==============================")

nombre = input("¿Cómo te llamas? ")
cantidad = int(input("¿Cuántos archivos quieres guardar? "))

espacio_por_archivo = 50
espacio_total = cantidad * espacio_por_archivo

print(f"¡Hola, {nombre}! Bienvenido a Bóveda Digital.")
print(f"Quieres guardar {cantidad} archivos.")
print(f"Necesitarás {espacio_total} MB de espacio.")

registros = []
opcion = ""

while opcion != "6":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular espacio para archivos")
    print("2. Conocer la aplicación")
    print("3. Consejos de seguridad")
    print("4. Agregar registro")
    print("5. Ver registros")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cantidad = int(input("¿Cuántos archivos quieres guardar? "))

        if cantidad >= 0:
            espacio_total = cantidad * espacio_por_archivo
            print(f"Necesitarás {espacio_total} MB de espacio.")
        else:
            print("La cantidad no puede ser negativa.")

    elif opcion == "2":
        print("Bóveda Digital ayuda a organizar y calcular el espacio para tus archivos.")

    elif opcion == "3":
        print("Consejo: utiliza contraseñas seguras y no las compartas.")

    elif opcion == "4":
        registro = input("Escribe el nombre o descripción del registro: ")
        registros.append(registro)
        print("Registro agregado correctamente.")

    elif opcion == "5":
        if len(registros) == 0:
            print("Todavía no hay registros.")
        else:
            print("\n--- REGISTROS GUARDADOS ---")

            for i in range(len(registros)):
                print(f"{i + 1}. {registros[i]}")

            print(f"Total de registros: {len(registros)}")

    elif opcion == "6":
        print(f"Hasta pronto, {nombre}.")

    else:
        print("Opción no válida.")
