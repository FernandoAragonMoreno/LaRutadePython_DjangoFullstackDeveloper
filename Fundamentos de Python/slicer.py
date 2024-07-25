#Obterer email
email = input("Cual es tu email?: ").strip()

#Cortar el nombre del usuario
usuario = email[:email.index("@")]

#Cortar el nombre del dominio
dominio = email [email.index("@")+1:]



#Formatear el mensaje
salida = "tu nombre de usuario es {} y tu dominio es {}".format(usuario, dominio)


#Mostrar mensaje de salida
print(salida)
