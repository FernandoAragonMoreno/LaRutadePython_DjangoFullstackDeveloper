usuarios_conocidos = ["Alice", "Bob", "Clarie", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(usuarios_conocidos))


while True:
    print("Hola mi nombre es Keto")
    nombre = input("Cual es tu nombre?: ").strip().capitalize()

    if nombre in usuarios_conocidos:
        print("hola {}!".format(nombre))
        eliminar = input("Quieres ser eliminado del sistema (y/n)").lower()

        if eliminar == "y":
            print(usuarios_conocidos)
            #solo remueve la primera coincidencia
            usuarios_conocidos.remove(nombre)
            print(usuarios_conocidos)
    else:
        print("Nombre NO Reconocido")
    
