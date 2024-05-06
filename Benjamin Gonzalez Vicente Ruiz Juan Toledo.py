#Benjamin Gonzalez - Vicente Ruiz - Juan ignacio Toledo
import random
import time

# Definir las oraciones
oraciones = ['Me quiere mucho', 'Me quiere poquito', 'Me quiere nada']

# Generar el número aleatorio
numero_aleatorio = random.randint(6,15)

# Menú en pantalla
print("\nD e s a r r o l l a d o   p o r ")
print("       Calfún's Planet       \n")

time.sleep(2)
print("Cargando...\n")

time.sleep(3)
print("1. Tomar una flor\n2. Salir del juego")

# Acción usuario
acción_menu=input("Acción -> ")
print("")

#Mientras usuario no escriba 1 o 2, repetir
while not (acción_menu=="1"or acción_menu=="2"):
    print("Respuesta invalida\n")
    acción_menu=input("1. Tomar una flor\n2. Salir del juego\nAcción -> ")
    print("")
   
if (acción_menu=="1"):
    # Operación del programa
    for i in range(1, numero_aleatorio + 1):
        resultado_oraciones = oraciones[(i - 1) % len(oraciones)]

        # Acción del usuario
        input("Presiona >>enter<< para quitar un pétalo")

        # Resultado
        print(f"Petalo {i} --> {resultado_oraciones}\n")

    #Mensaje en pantalla
    print("---------- Resultado ----------")
    time.sleep(3)
    if (resultado_oraciones=="Me quiere mucho"):
        print("FELICIDADES, TE QUIEREN MUCHO\nMUCHO\nMUCHO\nMUCHO\nMUCHO")
    elif (resultado_oraciones=="Me quiere poquito"):
        print("No desanimarse, te quieren poquito\npoquito\npoquito\npoquito\npoquito")
    else:
        print("Malas noticias, no te quieren nada\nnada\nnada\nnada\nnada")
else:
    print("Saliendo")

