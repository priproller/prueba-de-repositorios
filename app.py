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