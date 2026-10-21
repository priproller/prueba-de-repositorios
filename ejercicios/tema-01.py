# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: Matías Toro García
# Mi app se llama: Bóveda Digital
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí: 
nombre = "Matías"
edad = 17
estatura = 1.76

print(f"Soy {nombre}, tengo {edad} años y mido {estatura} m.")



# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:
a = "100"
b = 100
c = 100.0
d = "cien"

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Respuesta: 
# "100" es texto (str) y 100 es un entero (int).


# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:
cuenta = float(input("Valor de la cuenta: "))
personas = int(input("¿Cuántas personas van a pagar? "))
porcentaje = float(input("Porcentaje de propina: "))

propina = cuenta * porcentaje / 100
total = cuenta + propina
pago_persona = total / personas

print(f"Propina:       ${propina:,.0f}")
print(f"Total:         ${total:,.0f}")
print(f"Cada uno paga: ${pago_persona:,.0f}")


# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:
precio = float(input("Precio del producto: "))
unidades = int(input("Unidades: "))

print(f"Total a pagar: ${precio * unidades:,.0f}")

# Error 1: el precio se recibía como texto y debía convertirse a float.
# Error 2: las unidades se recibían como texto y debían convertirse a int.


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:
producto = input("Nombre del producto: ")
unidades = int(input("¿Cuántas unidades hay? "))
precio_unidad = float(input("Precio de cada unidad: "))

valor_total = unidades * precio_unidad

print("===== INVENTARIO =====")
print(f"Producto:    {producto}")
print(f"Unidades:    {unidades}")
print(f"Precio:      ${precio_unidad:,.0f}")
print(f"Valor total: ${valor_total:,.0f}")
print("======================")



# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================