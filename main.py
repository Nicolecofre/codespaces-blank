#Es un comentario y esa linea no sera ejecutada.
#para borrar todo del terminal, escribir clear

#Lee la variable, le asigna un valor y la guarda en memoria.

nombre = input ("Ingesa tu nombre: ") #imprime un mesnaje al usiario y espera que ingrese un dato
apellido = input("ingresa tu apellido: ") #Si se necesita más de una variable, podemos seguir poniendo input.
ciudad = input("ingresa tu ciudad: ")

print(f"Hola, {nombre}, {apellido}. Bienvenida a nuestra app.") #la f nis sirve para inyectar la variable. 
#para llamar a la variable, en este caso nombre siempre dentro de las keys {nombre}
# print(f"Hola, {nombre}. Bienvenida a nuestra app.") Podemos ir agregando {apellido, {ciudad}, etc}

print(f"Hola, {nombre}, {apellido}. Seleccionaste la ciudad: {ciudad}.")
# si necesitaramos el nombre completo, podemos hacerlo así

nombre_completo = f"{nombre} {apellido}"

print(f"nombre completo: {nombre_completo}")