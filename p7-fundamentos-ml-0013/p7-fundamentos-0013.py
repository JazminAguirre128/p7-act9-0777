# Meredith Aguirre NC = 0013

print ("Variables básicas 0013")
# Ejemplo 1: Asignación de variables numéricas y de texto (string)
edad = 20
nombre = "Juan"
print(nombre)
print(edad)
# Ejemplo 2: Cambio de tipo de dato (tipado dinámico)
x = 6       # x es de tipo int (entero)
x = "Hola"   # x ahora es de tipo str (texto)
print(x)
# Ejemplo 3: Conversión explícita de tipos (Casting)
texto_numero = "100"
numero = int(texto_numero)  # Convierte la cadena "100" al entero 100
print(numero + 50)          # Imprime 150

print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("Variables múltiples")
# Ejemplo 1: Asignar múltiples valores a múltiples variables
fruta, verdura, bebida = "Naranja", "Tomate", "Licuado"
print(fruta)
print(verdura)
print(bebida)
# Ejemplo 2: Asignar un mismo valor a múltiples variables
x = y = z = "Python"
print(x)
print(y)
print(z)
# Ejemplo 3: Desempaquetar una lista (Unpacking)
colores = ["Verde", "Morado", "Celeste"]
c1, c2, c3 = colores
print(c1)
print(c2)
print(c3)

print("+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print("Tipos de datos")
# Ejemplo 1: Tipos numéricos y texto
enteros = 42              # int
decimal = 19.99           # float
saludo = "Hola Mundo"     # str
print(type(enteros), type(decimal), type(saludo))
# Ejemplo 2: Listas y Tuplas (Secuencias)
lista_frutas = ["manzana", "banana"]  # list (mutable)
tupla_puntos = (10, 20)              # tuple (inmutable)
print(type(lista_frutas), type(tupla_puntos))
# Ejemplo 3: Diccionarios y Booleanos
persona = {"nombre": "Ana", "edad": 30}  # dict (clave-valor)
es_mayor_edad = True                     # bool
print(type(persona), type(es_mayor_edad))

print("-3-3-3-3-3-3-3-3-3-3-3-3-3-3")
print("Operadores aritméticos")
# Ejemplo 1: Suma, Resta y Multiplicación
a = 15
b = 4
print("Suma:", a + b)           # 19
print("Resta:", a - b)          # 11
print("Multiplicación:", a * b)  # 60
# Ejemplo 2: División estándar y División entera (Floor division)
print("División:", a / b)        # 3.75 (devuelve un float)
print("División entera:", a // b) # 3 (descarta los decimales)
# Ejemplo 3: Módulo (Resto) y Potencia
print("Módulo (resto):", a % b) # 3 (el residuo de 15 ÷ 4)
print("Exponente:", a ** b)     # 50625 (15 elevado a la 4)

print("-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1")
print("Operadores de comparación")
# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
precio_a = 50
precio_b = 50
print(precio_a == precio_b) # True (son iguales)
print(precio_a != precio_b) # False (no son diferentes)
# Ejemplo 2: Mayor que (>) y Menor que (<)
edad_usuario = 20
print(edad_usuario > 18)   # True (20 es mayor que 18)
print(edad_usuario < 18)   # False
# Ejemplo 3: Mayor/igual que (>=) y Menor/igual que (<=)
puntuacion = 80
print(puntuacion >= 80)    # True (es igual a 80)
print(puntuacion <= 79)    # False

print("-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0")
print("Operadores lógicos")
# Ejemplo 1: Operador `and` (Ambas condiciones deben ser verdaderas)
edad = 22
tiene_licencia = True
puedes_conducir = (edad >= 18) and tiene_licencia
print(puedes_conducir) # True
# Ejemplo 2: Operador `or` (Al menos una condición debe ser verdadera)
es_fin_de_semana = False
es_feriado = True
hay_descanso = es_fin_de_semana or es_feriado
print(hay_descanso) # True
# Ejemplo 3: Operador `not` (Invierte el resultado booleano)
usuario_bloqueado = False
print(not usuario_bloqueado) # True (al invertir False)

print("Meredith Aguirre NC 0013")