import random


def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras lineas del juego donde se da la bienvenida
    print("Bienvenido al juego adivina el numero!!!")
    print("Tienes que adivinar un numero entre 1 y 100")
    print("Intenta adivinarlo!")

    while not adivinado:
        # Pedir al usuario que ingrese un numero del 1 al 100
        adivinanza = input("Ingresa un numero del 1 al 100: ")

    # Varificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo estamos pasando de string a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero es menor a {adivinanza}")
            else:
                print(
                f"¡Felicidades! Adivinaste el numero {adivinanza} secreto en {intentos} intentos."
            )
        else:
            print("Por favor, ingresa un numero valido del 1 al 100")


juego_adivinanza()
