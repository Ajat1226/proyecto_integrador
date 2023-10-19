import os
import keyboard

def clear_and_print(num):
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)

# Iniciamos en el número 0
num = 0

while num <= 50:
    print("Presiona 'n' para continuar...")
    # Espera a que se presione la tecla "n"
    keyboard.wait('n')
    # Llama a la función para borrar la terminal e imprimir el nuevo número
    clear_and_print(num)
    # Aumenta el número en 1
    num += 1

