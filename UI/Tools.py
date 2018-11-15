#Deberiamos crear metodos que manejen la dataa que el usuario envia sobre la catastrofe
#UNo q diga la implicacion en base a la categoria que recibe
#Otro podria ser que en base a la hubicacion del usuario y la ubicacion de la tormeta para desarollar estrategias de ataque
#por ejemplo si esta muy cerca la tormenta deberia buscar un safe place, si esta lejos puede desarollar lo q quiere

#------------------------
# TOOLS
#------------------------
from UI.Event import *

def createevent(type, location, sendto, comment):
    global event
    event = Event.Event()
    type = type.title()
    location = location.title()
    sendto = sendto
    comment = comment.title()
    event.create(type, location, sendto, comment)

#def set(id, param1, param2):



