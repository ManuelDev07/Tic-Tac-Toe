#TRES EN RAYA

'''Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.'''

def check_game(table:list) -> bool:

    #Verifico las Filas pasadas:
    for row in table:
        if row.count(' X ') == 3: #Si hay tres iguales hay un ganador
            return True

        elif row.count(' O ') == 3: #Si hay tres iguales hay un ganador
            return True

def play_game(table:list, player:bool) -> bool:
    """Función que se encargará de llevar los turnos de la partida y de cambiar los " - " por el signo del jugador correspondiente

    Args:
        table (list): tablero en forma de lista/matriz
        player (bool): Si es True será el jugador 1, caso contrario será el jugador 2

    Returns:
        bool: Devuelve en valor booleano el jugador que haya ganado la partida para luego mostrarlo en pantalla al ser llamado por otra función.
    """
    while True:
        if player:
            try:
                print('\nTurno Jugador 1: [X]\n')

                #Si los datos ingresados son válidos se realiza el cambio por el signo correspondiente
                #Caso contrario si el jugador ingresa un dato inválido se avisa
                row = int(input('Ingresa la Fila: '))
                if row < 3:
                    column = int(input("Ingresa la Columna: "))
                    if column < 3:
                        table[row][column] = ' X '
                        for row in table:
                            print(row)

                        #Se hace la llamada enviando el tablero para verificar si hay tres en raya o no:
                        #Primero paso las filas:
                        winner = check_game(table)
                        
                        #Luego paso las columnas:
                        columns = [[table[i][j] for i in range(3)] for j in range(3)] #Paso las columnas a filas para luego verificarlas:
                        winner = check_game(columns)

                    else: 
                        print('ERROR! Se sale de los límites del tablero!!')
                
                else: 
                    print('ERROR! Se sale de los límites del tablero!!')


            except ValueError:
                print('ERROR! Debes hacerlo mediante números como se muestra en el tablero')
        else:
            try:
                print('\nTurno Jugador 2: [O]\n')

                #Si los datos ingresados son válidos se realiza el cambio por el signo correspondiente
                #Caso contrario si el jugador ingresa un dato inválido se avisa
                row = int(input('Ingresa la Fila: '))
                if row < 3:
                    column = int(input("Ingresa la Columna: "))
                    if column < 3:
                        table[row][column] = ' O '
                        for row in table:
                            print(row)

                        #Se hace la llamada enviando el tablero para verificar si hay tres en raya o no:
                        #Primero paso las filas:
                        winner = check_game(table)
                        
                        #Luego paso las columnas:
                        columns = [[table[i][j] for i in range(3)] for j in range(3)] #Paso las columnas a filas para luego verificarlas:
                        winner = check_game(columns)

                    else: 
                        print('ERROR! Se sale de los límites del tablero!!')
                
                else: 
                    print('ERROR! Se sale de los límites del tablero!!')


            except ValueError:
                print('ERROR! Debes hacerlo mediante números como se muestra en el tablero')
            
        return winner

def create_table() -> str:
    """Función que creará el tablero de juego, y definirá cual es el siguiente turno del jugador.

    Returns:
        str: Información que mostrará quién es el ganador de la partida
    """

    #Creo el Tablero:
    table = []
    for i in range(3):
        table.append([' - '] * 3)

    #Se empiezan a realizar los turnos:
    while True:
        for round in range(21):
            if round % 2 == 0:
                winner = play_game(table, player=True)
                if winner:
                    print('FELICIDADES! Jugador 1 [X] ha ganado!!!')
                    break

            else:
                winner = play_game(table, player=False)
                if winner:
                    print('FELICIDADES! Jugador 2 [O] ha ganado!!!')
                    break

def game_menu(): 
    """Función que servirá como menú principal para empezar el juego y mostrará solamente las instrucciones del juego."""
    while True:
        try:
            print(f'''
    \tTres en Raya:
{"-"*100}
- (1) EMPEZAR.
- (2) SALIR.
{"-"*100}
        Tablero:

        0   1   2
    0 | - | - | - |
    1 | - | - | - |
    2 | - | - | - |

INSTRUCCIONES: Elige en qué lugar realizarás el turno indicándolo mediante el número de sus filas y columnas como se muestra en el tablero.
''')    
            option = int(input('>>> '))
            if option == 1:
                print(create_table())
            else:
                print('Juego Finalizado!.')
                break

        except:
            print('ERROR!')

#Llamada a la función:
game_menu()