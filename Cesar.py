abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
mensaje = "" 
clave = 0
indices = []
mensaje_cifrado = ""
mensaje_decifrado = ""
letra_cifrada_global = ""
letra_decifrada_global = ""

op = 0

while op != 5:
    print()
    print("---- Sistema de cifrado ' Cesar ' ----")
    print("1. Ingreso de la clave")
    print("2. Ingreso del mensaje a cifrar")
    print("3. Cifrado del mensaje")
    print("4. Decifrado del mensaje")
    print("5. Presiona 5 para salir")
    op = int(input("Ingresa una opcion: "))

    match op :
        case 1:
            print(" !! Ingresa la clave !!")

            clave = int(input())

            print("Tu clave es: ", clave)

        case 2:
            print(" !! Ingresa el mensaje que deseas cifrar !!")

            mensaje = input().lower()  # Convertir a minúsculas

            print("El mensaje es: ", mensaje)

        case 3:
            indices.clear() 
            mensaje_cifrado = ""
            for letra in mensaje:
                if letra in abecedario:
                    indice = abecedario.index(letra)
                    indice_cifrado = (indice + clave) % len(abecedario)
                    letra_cifrada = abecedario[indice_cifrado]
                    mensaje_cifrado += letra_cifrada 
                    letra_cifrada_global = letra_cifrada  
                else:
                    mensaje_cifrado += letra  # Mantener caracteres no alfabéticos

            print("Mensaje Cifrado:", mensaje_cifrado)

        case 4:
            indices.clear() 
            mensaje_decifrado = ""
            for letra in mensaje_cifrado:
                if letra in abecedario:
                    indice = abecedario.index(letra)
                    indice_decifrado = (indice - clave) % len(abecedario)
                    letra_decifrada = abecedario[indice_decifrado]
                    mensaje_decifrado += letra_decifrada 
                    letra_decifrada_global = letra_decifrada  
                else:
                    mensaje_decifrado += letra  # Mantener caracteres no alfabéticos

            print("Mensaje Decifrado:", mensaje_decifrado)

        case 5:
            print("Saliendo del sistema de cifrado Cesar ..............")

        case _:
            print("ERROR, ! Ingresa una opcion correcta !")
