#juego de logica en python 3.4.6
#para 1 o 2 jugadores
#es un proyecto de aprendizaje ya que me encuentro e los primeros pasos de la programacion
#sientanse libres de brindar cualquier sugarencia
#desde ya gracias por visitar

import random
import time
import sqlite3


#---variables globales-----
ingreso=""
enigma=""
tur=0
deco='=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*='
vidas=0


class Jugador:
    def __init__(self,nombre=""):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    
def contar_vidas():
    global vidas
    vidas+=1
    return vidas
def vidas_reset():
    global vidas
    vidas=0

def presentacion_single():
    print('          HOLA !! ',p1.get_nombre().upper())
    time.sleep(0.5)
    print('  TE ANIMAS A ADIVINAR EL NUMERO QUE ESTOY PENSADO?? ')
    time.sleep(1)
    print('                     ** ** COMENZAMOS !!  ** **')
    time.sleep(1)
    single()
def presentacion_dobles():
    print('          HOLA !! ',p1.get_nombre().upper(),' & ',p2.get_nombre().upper())
    time.sleep(0.5)
    print('  SE ANIMAN A ADIVINAR EL NUMERO QUE ESTOY PENSADO?? ')
    time.sleep(1)
    print('                     ** ** COMENZAMOS !!  ** **')
    time.sleep(1)
    dobles()
#--generan el rango del numero a adivinar y separan single de  dobles--- 
def single():
    vidas_reset()
    generar(200)
    procesar(1)
def dobles():
    vidas_reset()
    generar(500)
    procesar(2)
#------------------------------------------------------------------------
def cant_players(numero_players):
    if numero_players == 1:
        return 's'
    else:
        return 'd'
def contador():
    global tur
    tur+=1
def tur_reset():
    global tur
    tur=0
#--------generador del numero a adivinar--------
def generar(rang):
    global enigma
    enigma=random.randint(1,rang)
     #----    ATENCION : esta linea se usa para q te muestre el numero que la maquina eligio  ------
     #-----sacarle el ' # ' para usaro en modo debugg----
    #print(enigma)#solo modo debugg  <<<<<--- BORRAR ESTA LINEA O HACERLA COMENTARIO ---

    
#------señala al ganador -------------
def ganaste(nro_player):
    if nro_player == 1:
        print(deco)
        print('GANASTEEEEEEEEEEEEEEE ' ,p1.get_nombre().upper())
        print("USASTE ",vidas,' INTENTOS .')
        
        tur_reset()
    else:
        
        print(deco)
        print('GANASTEEEEEEEEEEEEEEE ' ,p2.get_nombre().upper())
        print("USASTE ",vidas,' INTENTOS .')
        tur_reset()

def printing(c):
    if c == 1:
        print(deco)
        print('NUMERO MUY ALTO')
    elif c ==2:
        print(deco)
        print('NUMERO MUY BAJO')
        

#---------LOGICA PRINCIPAL---------

def procesar(modo):
    global ingreso
    while ingreso != enigma:
        #-----------------------logica para single player
        if modo  == 1:
            try:
                ingreso=int(input(' DIME TU NUMERO '+str(p1.get_nombre().upper())+' : '))
            except:
                print('Solo valores numericos  ** PIERDES EL TURNO **')
                ingreso=int(input(' DIME TU NUMERO '+str(p1.get_nombre().upper())+' : '))
            contar_vidas()
            
            if ingreso>enigma:
                time.sleep(0.5)
                printing(1)
            elif ingreso<enigma:
                time.sleep(0.5)
                printing(2)
            else:
                ganaste(1)
                print(deco)
                time.sleep(1)
                choice=input('QUERES LA REVANCHA??  si/no : ')
                print(deco)
                if choice== 'si' or choice=='SI' or choice== 's' or choice=='S' or  choice== 'Si' :
                    presentacion_single()
                else:
                    inicio()
        #-------- logca de los dobles-------------------------
        elif modo == 2:
            
            if tur %2==0:
                contador()
                try:
                    ingreso=int(input(' DIME TU NUMERO '+str(p1.get_nombre().upper())+' : '))
                except:
                    print('Solo valores numericos  ** PIERDES EL TURNO **')
                    
                if ingreso>enigma:
                    time.sleep(0.5)
                    printing(1)
                elif ingreso<enigma:
                    time.sleep(0.5)
                    printing(2)
                else:
                    ganaste(1)
                    time.sleep(1)
                    print(deco)
                    choice=input('QUIEREN LA REVANCHA??  si/no : ')
                    print(deco)
                    if choice== 'si' or choice=='SI' or choice== 's' or choice=='S' or  choice== 'Si' :
                        presentacion_dobles()
                    else:
                        inicio()
            else:
                contador()
                try:
                    ingreso=int(input(' DIME TU NUMERO '+str(p2.get_nombre().upper())+' : '))
                except:
                    print('Solo valores numericos  ** PIERDES EL TURNO **')
                if ingreso>enigma:
                    printing(1)
                elif ingreso<enigma:
                    printing(2)
                else:
                    ganaste(2)
                    time.sleep(1)
                    print(deco)
                    choice=input('QUIEREN LA REVANCHA??  si/no : ')
                    print(deco)
                    if choice== 'si' or choice=='SI' or choice== 's' or choice=='S' or  choice== 'Si' :
                        presentacion_dobles()
                    else:
                        inicio()
            
    
#-----------------presentacion del juego------------    
def inicio():
    global p1,p2
    print('        BIENVENIDOS !!!')
    time.sleep(0.5)
    print(' ###   ADIVINA2    ###                                      v.1.2.0')
    time.sleep(0.5)
    try:
        cant_p = cant_players(int(input('   CUANTOS JUGADORES? : ')))
    except:
        print('*DEBES INGRESAR EL NUMERO 1 O EL 2*')
        try:
            cant_p = cant_players(int(input('   CUANTOS JUGADORES? : ')))
        except:
            inicio()
    
        
    if (cant_p=='s'):
        p1=Jugador(input(' DECIME TU NOMBRE :)  > '))
        presentacion_single()
    else:
        p1=Jugador(input(' DECIME TU NOMBRE JUGADOR 1 :  > '))
        p2=Jugador(input(' DECIME TU NOMBRE JUGADOR 2 :  > '))
        presentacion_dobles()
    
        
inicio()

