#Pedir nombre al usuario
nombre = input("Cual es tu nombre?: ")
print(nombre)

#Pedir edad
edad = input("Cual es tu edad?: ")
print(edad)

#Pedir direccion
ciudad = input("En que ciudad vives?: ")
print(ciudad)

#Pedir hobbie
hobbie = input("Cual es tu hobbie?: ")
print(hobbie)

#crear texto de salida
string = "Tu nombre es {} y tienes {} años vives en {} y te gusta {}"
salida = string.format (nombre, edad, ciudad, hobbie)

#Imprimir texto de salida
print(salida)
