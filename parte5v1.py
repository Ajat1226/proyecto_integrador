import os

class Juego:
    mapa: list
    inicio: tuple
    final: tuple

    def crear_mapa_laberinto(self,laberinto_str):
        filas = laberinto_str.strip().split('\n')
        self.mapa = [list(fila) for fila in filas]
        return self.mapa
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_mapa(self, mapa):
        for fila in mapa:
            print(''.join(fila))
    
    def main_loop(self,mapa, inicio, final):
        px, py = inicio
        while (px, py) != final:
            mapa[px][py] = 'P'
            self.limpiar_pantalla()
            self.mostrar_mapa(self.mapa)
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
        self.limpiar_pantalla()
        mapa[px][py] = 'P'
        self.mostrar_mapa(mapa)
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

Jugar = Juego()
Jugar.crear_mapa_laberinto(laberinto)
Jugar.main_loop(Jugar.mapa, (0,0), (len(Jugar.mapa) - 1, len(Jugar.mapa[0]) - 1))

class Juego:
    def __init__(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        
        nombre_archivo = random.choice(archivos_de_mapas)
        
        self.path_completo = f"{path_a_mapas}/{nombre_archivo}"

    def leer_mapa(self):
        try:
            with open(self.path_completo, 'r') as archivo_mapa:
                lineas = archivo_mapa.readlines()

                cadena_mapa = ''.join(lineas).strip()

                return cadena_mapa
        except FileNotFoundError:
            print(f"El archivo {self.path_completo} no fue encontrado.")
            return None

path_a_mapas = path_a_mapas = r"C:\Users\alvar\Desktop\ada_scholl\proyecto_integrador\mapas"
juego = Juego(path_a_mapas)

contenido_mapa = juego.leer_mapa()
if contenido_mapa:
    print("Contenido del mapa:")
    print(contenido_mapa)