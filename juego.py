import random
import time

class Juego:
    def __init__(self,personajes=None, miscanicas=0, canicasrival=0):
        self.personajes={'player1':'Seong Gi-hun (AKA "El prota")', 
             'player2':'Cho Sang-woo (AKA "El banquero")',
             'player3':'Kang Sae-byeok (AKA "La norcoreana")',
             'player4':'Oh Il-nam (AKA "El viejo)"',
             'player5':'Jang Deok-Su (AKA "El malo")'
            }
        
    
    def quien_empieza(self,player=None,rival=None):
        '''Decide al azar que jugador empieza el juegp'''
        self.player=player
        self.rival=rival
        if random.randint(0,1)==0:
            return player
        else:
            return rival
    
    def mano_rival(self):
        '''Decide al azar la eleccion Par o Impar del rival'''
        return "".join(random.choices(["P","I"]))
    
    def mi_mano(self):
        '''Pide al jugador la eleccion Par o Impar'''
        while True:
            try:
                mimano=input(f'Decide si el número de canicas que vas ha tener en tu mano es PAR (P) o IMPAR (I)').upper()
                if mimano == "I" or mimano=="P":
                    break
            except:
                pass
            
        return mimano
        
    
    def apuesta_rival(self,canicasrival,miscanicas):
        '''Da un numero al azar en 1 y el máximo de canica que CPU puede apostar'''
        apuesta_cpu=random.randint(1,min(canicasrival,miscanicas))
        print(f'Tu rival se ha apostado {apuesta_cpu} canica/s')
        return apuesta_cpu
            
    
    def selec_player(self):
        '''Se le pide al jugador seleccionar su personaje de la lista 
        y devuelve el valor que tiene en el diccionario de personajes '''
        while True:
            try:
                p = input('Selecciona tu personaje escribiendo: "player + num. jugador"')
                if isinstance(p, str) and p in self.personajes.keys():
                    break
            except:
                pass

        return self.personajes.get(p)
    
    def selec_rival(self,player):
        '''Se le pide al jugador seleccionar su rival de la (lista de personajes - el personaje ya escogido)
        y devuelve el valor que tiene en el diccionario de personajes '''
        #self.player=player
        while True:
            try:
                r = input('Selecciona tu rival escribiendo: "player + num. jugador"')
                if isinstance(r, str) and r in {key:val for key,val in self.personajes.items() if val != player}.keys():
                    break
            except:
                pass

        return {key:val for key,val in self.personajes.items() if val != player}.get(r)
    
    def apuesta_player(self,miscanicas,canicasrival):
        '''Pide al jugado el número de canicas a apostar'''
        while True:
            try:
                miapuesta=int(input(f'Decide cuantas canicas de tus {miscanicas} quieres apostar (deben ser <= a las canicas de tu rival)'))
                if isinstance(miapuesta, int) and miapuesta <= miscanicas and miapuesta <= canicasrival:
                    break
            except:
                pass
            
        print(f'Has apostado {miapuesta} canica/s')
        return miapuesta
    
    def gess_mano_rival(self):
        '''Pide al jugador que diga un número Par o Impar'''
        while True:
            try:
                migess=input(f'Decide si el número de canicas que hay en la mano de tu rival es PAR (P) o IMPAR (I)').upper()
                if migess == "I" or migess=="P":
                    break
            except:
                pass
            
        return migess
    
    def turno_player(self,miapuesta):
        '''Ejecuta el turno del jugador'''
        migess=self.gess_mano_rival()
        mano_rival=self.mano_rival()
        if migess==mano_rival:            
            resultado=miapuesta              
        else:            
            resultado=-1*(miapuesta)
        
        time.sleep(1)
        print(f'El rival tenia un número {mano_rival}')
        
        return resultado
            
    def turno_cpu(self,suapuesta):
        '''Ejecuta el turno de la máquina'''
        mimano=self.mi_mano()
        cpugess=self.mano_rival()
        if mimano==cpugess:
            resultado=suapuesta
        else:
            resultado=-1*(suapuesta)
        
        time.sleep(1)
        print(f'El rival ha dicho {cpugess}')
        
        return resultado        
        
        
    
    def jugar(self):
        '''Da la bienvenida y invita al jugador a que
            elija su personaje y su rival. Despúes ejecuta el juego'''
        
        print(f'Antes de empezar elije que personaje quieres ser de la siguiente lista:')
        time.sleep(1)
        print(self.personajes)
        time.sleep(1)
        player= self.selec_player() #llamada a la función selec_player
        print(f'Bienvenido/a {player}! Ahora debes seleccionar tu rival de los jugadores que quedan.')
        time.sleep(1)
        print({key:val for key,val in self.personajes.items() if val != player})
        time.sleep(1)
        rival=self.selec_rival(player)
        print(f'{player} se enfrentará a {rival}. Cada jugador cuenta con 10 canicas iniciales. En unos segundos se decidirá quien empieza la partida')
        time.sleep(3)
        primero=self.quien_empieza(player,rival)
        print(f'El azar ha decidido que empiece {primero}')
        miscanicas=10
        canicasrival=10
        if primero==player:
            while miscanicas>0 and canicasrival >0:
                
                miapuesta=self.apuesta_player(miscanicas,canicasrival) #llamada a funcion apuesta_player
                resultado=self.turno_player(miapuesta) #llamada a funcion turno_player que a su vez llama a función gess.mano_rival
                time.sleep(0.5)
                if resultado>0:
                    print(f'Felicidades has ganado esta ronda')
                else:
                    print(f'Lamentablemente has perdido esta ronda')
                miscanicas += resultado       #actualizacion de canicas disponibles para jugador y rival
                canicasrival -= resultado
                if miscanicas==0 or canicasrival==0:     #si alguno se ha quedado sin canicas ir a final del juego
                    break
                else:
                    time.sleep(0.5)
                    print(f'Te quedan {miscanicas} canicas y a tu rival le quedan {canicasrival}.')
                    suapuesta=self.apuesta_rival(canicasrival,miscanicas) #llamada a funcion apuesta_rival
                    resultado=self.turno_cpu(suapuesta) #llamada a funcion turno_rival que a su vez llama a función mi_mano
                    time.sleep(0.5)
                    if resultado>0:
                        print(f'{rival} ha ganado esta ronda.')
                    else:
                        print(f'{rival} ha perdido esta ronda.')
                    miscanicas -= resultado      #actualizacion de canicas disponibles para jugador y rival
                    canicasrival += resultado
                    time.sleep(0.5)
                    print(f'Te quedan {miscanicas} canicas y a tu rival le quedan {canicasrival}.')
        else:
            while miscanicas>0 and canicasrival >0:
                suapuesta=self.apuesta_rival(canicasrival,miscanicas)
                resultado=self.turno_cpu(suapuesta)
                time.sleep(0.5)
                if resultado>0:
                    print(f'{rival} ha ganado esta ronda.')
                else:
                    print(f'{rival} ha perdido esta ronda.')
                miscanicas -= resultado
                canicasrival += resultado
                if miscanicas==0 or canicasrival==0:  #si alguno se ha quedado sin canicas ir a final del juego
                    break
                else:
                    time.sleep(0.5)
                    print(f'Te quedan {miscanicas} canica/s y a tu rival le quedan {canicasrival}.')
                    miapuesta=self.apuesta_player(miscanicas,canicasrival)
                    resultado=self.turno_player(miapuesta)
                    time.sleep(0.5)
                    if resultado>0:
                        print(f'Felicidades has ganado esta ronda')
                    else:
                        print(f'Lamentablemente has perdido esta ronda')
                    miscanicas += resultado
                    canicasrival -= resultado
                    time.sleep(0.5)
                    print(f'Te quedan {miscanicas} canica/s y a tu rival le quedan {canicasrival}.')
        
        if miscanicas==0:
            time.sleep(1)
            print(f'Desafortunadament te has quedado sin caninas, por tanto estás muerto. Pasa al siguiente juego {rival}')
        else:
            time.sleep(1)
            print(f'Enhorabuena has ganado! {rival} ha muerto. {player} pasa al siguiente juego.')
                  

def main():
    while True:
       partida = Juego()
       partida.jugar()

       seguir = input('Quieres seguir jugando? S/N ')
       if seguir != 'S':
          break

if __name__ == '__main__':
    main()
