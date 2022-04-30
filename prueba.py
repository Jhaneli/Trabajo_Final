import sqlite3
import random


Link = sqlite3.connect("Resultados.Db")
Mando = Link.cursor()

Op = ("Piedra", "Papel", "Tijeras")


def Game():
    
    Check = False
    
    while Check == False: 

       
        Jg = (input("""
        
        
        Inserte su jugada

        1 = Piedra
        2 = Papel
        3 = Tijeras 
"""))


        if Jg.isnumeric():
            Select = int(Jg)
            Select = int(Select -1)
            if Select >= 0 and Select < 3:
                Check = True 
            else:
                print ("Opción incorrecta")
                print ("Intente nuevamente")

        else:
            print ("Opción incorrecta")
            print ("Intente nuevamente")
           
    Pc = (random.choice([0,1,2]))
    Op_Pc = (Op[Pc])
    Op_Jg = (Op[Select])
    print  ("Usted ha elegido: ",Op_Jg)
    print  ("La maquina ha elegido: ",Op_Pc)
  

    def Result():
            
            Resul = ("Empate", "Jugador", "Maquina")

            if Select == Pc: 
                Save = (Resul[0])
                print ("Ha sido un empate")
            elif Select == 0:
                if Pc == 1:
                    print ("Gana: Computador")
                    Save = (Resul[2])
                else:
                    print ("Gana: Jugador")
                    Save = (Resul[1])
            elif Select == 1:
                if Pc == 2:
                    print ("Gana: Computador")
                    Save = (Resul[2])
                else:
                    print ("Gana: Jugador")
                    Save = (Resul[1])
            elif Select == 2:
                if Pc == 0:
                    print ("Gana: Computador")
                    Save = Resul[2]
                else:
                    print ("Gana: Jugador")
                    Save = Resul[1]
            
        
            def DB():
                Link = sqlite3.connect("Resultados.Db")
                Mando = Link.cursor()
                       
                Mando.execute(
                    """CREATE TABLE IF NOT EXISTS Resultado(
                        PC text,
                        Jugador text,
                        Ganador text)
                        
                    """
                )

                Mando.execute("""INSERT INTO
                Resultado (Pc, Jugador, Ganador) Values (?,?,?)""", (Op_Pc, Op_Jg, Save))



                Link.commit()
            DB()
    
    Result()
   
def Scores():

    Link = sqlite3.connect("Resultados.Db")
    Mando = Link.cursor()     
    for a in Mando.execute("SELECT COUNT(*) FROM Resultado WHERE Ganador =?", ("Empate",) ):
        print ("Las partidas empatadan han sido: ",a)
    for b in Mando.execute("SELECT COUNT(*) FROM Resultado WHERE Ganador =?", ("Jugador",) ):
        print ("Las partidas ganadas han sido: ",b)
    for c in Mando.execute("SELECT COUNT(*) FROM Resultado WHERE Ganador =?", ("Maquina",) ):
        print ("Las partidas perdidas han sido: ",c)
    Link.commit()





    


