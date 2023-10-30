import os

def crear_mapa_laberinto(laberinto_str):
    filas = laberinto_str.strip().split('\n')
    mapa = [list(fila) for fila in filas]
    return mapa

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, inicio, final):
    px, py = inicio
    while (px, py) != final:
        mapa[px][py] = 'P'
        limpiar_pantalla()
        mostrar_mapa(mapa)
        mapa[px][py] = '.'
        
        direccion = input("Introduce una direccion (arriba, abajo, izquierda, derecha): ")
        
        if direccion == "arriba":
            if px > 0 and mapa[px - 1][py] != '#':
                px -= 1
        elif direccion == "abajo":
            if px < len(mapa) - 1 and mapa[px + 1][py] != '#':
                px += 1
        elif direccion == "izquierda":
            if py > 0 and mapa[px][py - 1] != '#':
                py -= 1
        elif direccion == "derecha":
            if py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
                py += 1

    limpiar_pantalla()
    mapa[px][py] = 'P'
    mostrar_mapa(mapa)
    print("¡Has llegado a la meta!")

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = crear_mapa_laberinto(laberinto)
inicio = (0, 0)
final = (len(mapa) - 1, len(mapa[0]) - 1)
main_loop(mapa, inicio, final)
