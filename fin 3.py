import numpy as np
import matplotlib.pyplot as plt

def comenzar_juego():
    print ("\nBienvenido a los juegos del examen final de Pedro German Gainza alumno de Digital")
    while True:
        print("\nElije un juego entre las opciones: \n")
        print("1. Piedra, Papel o Tijera.")
        print("2. Adivina un numero.")
        print("3. Tira el dado.")
        print("4. Grafica una funcion matematica.")
        print("5. Salir del juego."),

        opcion = input("\nElige una opción: ")
        if opcion=="1":
            import random

            opciones_compu=["Piedra", "Papel", "Tijera"]

            juego_compu=random.choice(opciones_compu)

            elige_jugador=input("\nElija Piedra, Papel o Tijera: ")

            if elige_jugador == juego_compu :
             print("\nEmpataste\n")
            elif elige_jugador=="Piedra" and juego_compu=="Papel":
             print("\nPerdiste", "la computador eligió Papel\n")
            elif elige_jugador=="Papel" and juego_compu=="Piedra":
             print("\nGanaste\n")
            elif elige_jugador=="Papel" and juego_compu=="Tijera":
             print("\nPerdiste", "la computadora elijgió Tijera\n")
            elif elige_jugador=="Tijera" and juego_compu=="Papel":
             print("\nGanaste\n")
            elif elige_jugador=="Tijera" and juego_compu=="Piedra":
             print("\nPerdiste", "la computadora eligió Piedra\n")
            elif elige_jugador=="Piedra" and juego_compu=="Tijera":
             print("\nGanaste\n")
            else:
             print("\nno está en las opciones\n")

        elif opcion=="2":
            import random

            numero_jugador=int(input("\nElige un número del 1 al 20: "))
            numero_compu=random.randint(1,20)

            if numero_jugador == numero_compu:
             print("\nAdivinaste", "elegiste", numero_jugador, "y la computadora eligió", numero_compu,"\n")
            if numero_jugador > 20:
               print ("¡¡¡ERROR!!! Ingresaste un numero invalido")         
             
            else:
             print("\nNo Adivinaste", "elegiste", numero_jugador, "y la computadora eligió", numero_compu,"\n")
        
    
        elif opcion=="3":
            import random

            dado=random.randint(1,6)

            juego=input("\nTire el dado presionando enter \n")

            print("El valor del dado es", dado ,"\n")

        elif opcion == "4":
            x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
            y = np.sin(x)

            plt.plot(x, y)
            plt.title('Gráfico de y = sin(x)')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)

            plt.show()      

        elif opcion == "5":
            salir = input("\n¿Quieres salir del juego? escribe SALIR \n")
            if salir== "SALIR":
                break
            elif salir== "salir":      
                break
        else:
            print("Opción inválida. Elige una opción válida.")

comenzar_juego()
           