import random, os
 

#////////////////////////////////////////////////////
# Esta funcion imprime la tabla anterior
# "tabla" es una lista de 10 posiciones que representa la tabla (ignorar posicion 0)
#////////////////////////////////////////////////////
def tablero(tabla):
  if ('X' in tabla and 'O' in tabla): # si hay algun elementos jugado limpia la tabla y cargala de nuevo con print, si ingreso una jugada se mostrara la actualizacion
    os.system ("clear")
  A = '    ||   ||'
  B = '================='
  C = ' '
  print ('')
  print ('ESTAS JUGANDO TRES EN RAYA')
  print ('')
  print (A.center(25, " "))
  print (C.center(8, " ") + tabla[7] + '  || ' + tabla[8] + ' || ' + tabla[9])
  print (A.center(25, " "))
  print (B.center(30, " "))
  print (A.center(25, " "))
  print (C.center(8, " ") + tabla[4] + '  || ' + tabla[5] + ' || ' + tabla[6])
  print (A.center(25, " "))
  print (B.center(30, " "))
  print (A.center(25, " "))
  print (C.center(8, " ") + tabla[1] + '  || ' + tabla[2] + ' || ' + tabla[3])
  print (A.center(25, " "))
  print (" ")
#//////////////////////////////////////////////////// 

#////////////////////////////////////////////////////
#Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario
#Devuelve Falso
#////////////////////////////////////////////////////
def JuegoNuevo():
  print ('')
  #print('Quieres jugar de nuevo? (S o N)')
  decision = input('Quieres jugar de nuevo? (S o N) >>> ')
  #Lower() combierte la entrada en minuscula, si fue ingresada en mayuscula
  #Startswith devuelve verdadero si la entrada comienza con s
  return decision.lower().startswith('s')
#//////////////////////////////////////////////////// 


#////////////////////////////////////////////////////
#GRABAR MOVIMIENTO
#//////////////////////////////////////////////////// 
def movimiento(tabla, letter, move):
    tabla[move] = letter
#////////////////////////////////////////////////////    


#////////////////////////////////////////////////////
#SE ESCOJE AL JUGADOR DE FORMA ALEATORIA EL JUGADOR QUE INICIARA LA PARTIDA Y RETORNO 
#Computadora O Usuario
#////////////////////////////////////////////////////
def primerJugador():
  if random.randint(0, 1) == 0:
    return 'Computadora'
  else:
    return 'Usuario'
#////////////////////////////////////////////////////    

#////////////////////////////////////////////////////
#SOLICITAMOS AL JUGADOR QUE ESCOJA EL SIMBOLO DE SU PREFERENCIA Y RETORNAMOS UNA LISTA
#SI EL JUGADOS ESCOGE X SE DEVUELVE ['X', 'O'], SI NO ES X LA QUE ESCOJE SE DEVUELVE ['O', 'X']
#EL PRIMER ELEMENTO DE LA LISTA SIEMPRE ES EL JUGADOR Y EL SEGUNDO ELEMENTO ES LA MAQUINA
#////////////////////////////////////////////////////
def inputLetraUsuario():
  letra = ''
  while not (letra == 'X' or letra == 'O'):
    print ("-------------------------------")
    #print ('Escoge tu simbolo (X - O) >>> ')
    letra = input('Escoge tu simbolo (X - O) >>> ').upper()
  if letra == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']
 


#/////////////////////////////////////////////////////////
#IA
#/////////////////////////////////////////////////////////
def dameMovimientoPC(tabla, letraPC):#Identificar con que simbolo jugar
  if letraPC == 'X':
    letraUsuario = 'O'
  else:
    letraUsuario = 'X'

  #Verifica si la computadora ganar en el proximo movimiento.
  for i in range(1, 10):
    copy = dameTablero(tabla)
    if espacioLibre(copy, i): #Verificamos si hay espacio
      movimiento(copy, letraPC, i) #Grabamos el movimiento
      if ganador(copy, letraPC):
        return i

  #bloquear jugada del jugador si el jugador puede ganar
  #Verifica si el jugador podria ganar proximo movimiento y bloquear el juego
  for i in range(1, 10):
    copy = dameTablero(tabla)
    if espacioLibre(copy, i):
      movimiento(copy, letraUsuario, i)
      if ganador(copy, letraUsuario):
        return i

  #Intenta tomar una de las esquinas si esta libre
  move = movimientoAleatorio(tabla, [1, 3, 7, 9])
  if move != None:
    return move

  # Intenta tomar el centro, si esta libre.
  if espacioLibre(tabla, 5):
    return 5

  # Mu�vete en uno de los lados.
  return movimientoAleatorio(tabla, [2, 4, 6, 8])
#/////////////////////////////////////////////////////////


#////////////////////////////////////////////////////  
# LA LATRA DEL JUGADOR SE BUSCA EN COMBINACIONES QUE INDICAN QUE A GANADO
#esto retorna true si se encuentra la combinacion
#//////////////////////////////////////////////////// 
def ganador(tabla, letra):
  return ((tabla[7] == letra and tabla[8] == letra and tabla[9] == letra) or
        (tabla[4] == letra and tabla[5] == letra and tabla[6] == letra) or
        (tabla[1] == letra and tabla[2] == letra and tabla[3] == letra) or
        (tabla[7] == letra and tabla[4] == letra and tabla[1] == letra) or
        (tabla[8] == letra and tabla[5] == letra and tabla[2] == letra) or
        (tabla[9] == letra and tabla[6] == letra and tabla[3] == letra) or
        (tabla[7] == letra and tabla[5] == letra and tabla[3] == letra) or
        (tabla[9] == letra and tabla[5] == letra and tabla[1] == letra))
#//////////////////////////////////////////////////// 



 
#//////////////////////////////////////////////////// 
#Hacer un duplicado de la lista de tabla y devolverlo el duplicado
#//////////////////////////////////////////////////// 
def dameTablero(tabla):
  retorno = []
  for i in tabla:
    retorno.append(i)
  return retorno
#////////////////////////////////////////////////////   
 

#//////////////////////////////////////////////////// 
# Devuelve TRUE si el movimiento pasado es libre en la tabla pasada.
#//////////////////////////////////////////////////// 
def espacioLibre(tabla, move):
  return tabla[move] == ' '# si la posicion esta vacia devuelve true
#//////////////////////////////////////////////////// 
 

#OJO
#//////////////////////////////////////////////////// 
# Deja que el jugador haga su movimiento.
#//////////////////////////////////////////////////// 
def dameMoviemiento(tabla):
  movimiento = ' '
  #Miestra la jugada no sea un numero correcto o 
  while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not espacioLibre(tabla, int(movimiento)):
    #split conviente una cadena en una lista
    print ("-------------------------------")
    movimiento = input('Ingresa jugada (1 - 9) >>> ')
  return int(movimiento)
#////////////////////////////////////////////////////   
 

#//////////////////////////////////////////////////// 
#Devuelve un movimiento valido de la lista pasada en la tabla pasada.
#Devuelve Ninguno si no hay un movimiento valido.
#//////////////////////////////////////////////////// 
def movimientoAleatorio(tabla, listaMovimientos):
  pisibleMovimiento = []
  for i in listaMovimientos:
    if espacioLibre(tabla, i):
      pisibleMovimiento.append(i)
 
  if len(pisibleMovimiento) != 0:
    return random.choice(pisibleMovimiento)
  else:
    return None
#////////////////////////////////////////////////////



#////////////////////////////////////////////////////
#Busca espacios libre en la lista de jugadas
#///////////////////////////////////////////////////
def tablaLlena(tabla):    
  for i in range(1, 10):
    if espacioLibre(tabla, i):
      return False
  return True
#///////////////////////////////////////////////////




#///////////////////////////////////////////////////
#PRESENTACION
#SE EJECUTA UNA VEZ AL INICIO DEL PROGRAMA
#///////////////////////////////////////////////////
def init():
  os.system ("clear")
  print('BIENVENIDO A TRES EN RAYA!')
  print ("")
  print ('Por:       Benjamin S�nchez')
  print ('Matricula: 2011-0534')
  print ("")
  print ("")
  print ("     **     ||            ||   **   **    ")
  print ("   **  **   ||            ||    ** **     ")
  print ("   **  **   ||            ||     ***      ")
  print ("   **  **   ||            ||    ** **     ")
  print ("     **     ||            ||   **   **    ")
  print ("===========================================")
  print ("   **   **  ||   **   **  ||     **       ")
  print ("    ** **   ||    ** **   ||   **  **     ")
  print ("     ***    ||     ***    ||   **  **     ")
  print ("    ** **   ||    ** **   ||   **  **     ")
  print ("   **   **  ||   **   **  ||     **       ")
  print ("===========================================")
  print ("            ||            ||              ")
  print ("     **     ||            ||              ")
  print ("   **  **   ||            ||              ")
  print ("   **  **   ||            ||              ")
  print ("   **  **   ||            ||              ")
  print ("     **     ||            ||              ")
  print ("")
  print ("")

init() 
  #///////////////////////////////////////////////////
 




while True:
  # Reset the tabla
  elTablero = [' '] * 10 #iniciamos 'elTablero' el tablero con 10 posiciones
  letraUsuario, letraPC = inputLetraUsuario() #Solicitamos simbolos de los jugadores
  retorno = primerJugador() #Escoje quien iniciara la partida
  os.system ("clear") #Limpia la pantalla
  print('' + retorno + ' Juega primero!') # se nos muestra en pantalla quien fue el escogido para iniciar el juego
  juegoOn = True #indicamos la que variable con la que trabajara el while es true, para que nunca se detenga por si sola
 
  while juegoOn:
    if retorno == 'Usuario': # Si el usuario juega primero
      tablero(elTablero) #Mostramos la tabla actualizada con las jugadas
      move = dameMoviemiento(elTablero) #Si el table tiene espacio y no el juego aun no termina
      movimiento(elTablero, letraUsuario, move) # grava el movimiento

      if ganador(elTablero, letraUsuario):#Si el jugador gano
        tablero(elTablero)
        hasGanado = 'GANASTE!'
        print (hasGanado.center(29, " "))
        juegoOn = False
      else:                               #Si el jugador no gano
        if tablaLlena(elTablero):         
          tablero(elTablero)
          empate = 'EMPATE!'
          print (empate.center(29, " "))
          break
        else:
          retorno = 'computadora'
 
    else: #RETORNO ES IGUAL  A LA COMPUTADORA
      move = dameMovimientoPC(elTablero, letraPC) #retorna el movimiento de la pc
      movimiento(elTablero, letraPC, move) # grabar movimiento
 
      if ganador(elTablero, letraPC):
        tablero(elTablero)
        hasPerdido = 'PERDISTE!'
        print (hasPerdido.center(29, " "))
        juegoOn = False
      else:
        if tablaLlena(elTablero):
          tablero(elTablero)
          empate = ' EMPATE!'
          print (empate.center(29, " "))
          break
        else:
          retorno = 'Usuario'
 
  if not JuegoNuevo():
    init()