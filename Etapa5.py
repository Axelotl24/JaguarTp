def Puntaje(Aciertos,Desaciertos,Puntos=0):
    """
    Toma como parametros: Aciertos(int), Desaciertos(int)
    Retorna los puntos del usuario
    Firma: FedeBacelar
    """
    PUNTOS_ACIERTOS = 2
    PUNTOS_DESACIERTOS = 1
    Puntos += (Aciertos*PUNTOS_ACIERTOS - Desaciertos*PUNTOS_DESACIERTOS)
    return Puntos

def SeguirJuego():
    """
    Retorna la solicitud de "seguir jugando" del usuario en forma de: True o False
    FedeBacelar: FedeBacelar
    """
    seguir = str(input("Desea seguir jugando? (s/n)"))
    return seguir.lower() == "s"