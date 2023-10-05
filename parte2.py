from readchar import readkey, key

print("Presiona la tecla UP para salir del bucle.")
while True:
    key_event = readkey()
    if key_event == key.UP: 
        print("saliste del juego")
        break
    else:
        print(key_event)

