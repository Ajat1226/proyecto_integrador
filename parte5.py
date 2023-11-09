'''
Encapsulando el juego en una clase

Ahora que disponemos de muchas más herramientas, podemos notar que reutilizamos la variable que contiene el mapa muchas veces y es molesto llamar funciones desconectadas enviando el mismo parámetro.

La programación orientada a objetos viene a nuestro rescate!

Implementa la clase Juego, ahora el mapa y las posiciones inicial y final son atributos de esta clase, reescribe todas tus funciones anteriores de forma que sean métodos de la clase y todo esté encapsulado.

Instanciar el juego y ejecutarlo desde el main
Almacenando mapas en archivos

En lugar de almacenar el mapa en el mismo código, podemos guardarlo en archivos con sus posiciones de inicio y fin y las dimensiones del mapa en la primera línea del archivo, de esta manera los componentes de la aplicación estarán separados y podremos mejorar la experiencia del juego.

    Crear una nueva clase JuegoArchivo la cual hereda de Juego,
    Reescribir el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.
        Para listar los archivos de un directorio usar os.listdir(path) , esto devolverá una lista con el nombre los archivos en ese directorio
        Para elegir un elemento aleatorio de una lista usar random.choice(lista).
        Note que para poder leer el archivo tenemos que componer el path, una forma de hacerlo es path_completo = f"{path_a_mapas}/{nombre_archivo}"
    Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin. Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.

'''

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
