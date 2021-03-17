from turtle import *
from freegames import vector 

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    #Declarar punto de inicio
    up()
    goto(start.x, start.y)
    #Declarar puntos de la circunferencia 
    down()
    #Comenzar a llenar la figura
    begin_fill()
    #Utilizar la función circle para trazar un círculo cuyo radio es la diferencia del punto final y el inicial en x
    circle(-start.x+end.x)
    #Terminar el llenado
    end_fill()



def rectangle(start, end):
    "Draw rectangle from start to end."
    #Extremo inicial del vector que traza la figura
    up()
    goto(start.x, start.y)

    #Extremo que va a cambiar de coordenadas para describir la figura del rectángulo
    down()
    #Inicializar el llenado del contorno de la figura
    begin_fill()

    #Ciclo que traza el rectángulo en dos pasos, primero traza la base descrita por la diferencia entre el punto inicial y final en x, luego gira a 90 grados hacia la izquierda y avanza la distancia correspondiente 
    #a la diferencia de puntos de y para trazar la altura del rectángulo y vuelve a girar 90 grados a la izquierda. El proceso se repite 2 veces y para cerrar el contorno de la figura y se termina el llenado. 
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    #Declarar el punto inicial como el primer vértice de la figura
    up()
    goto(start.x, start.y)

    #Declar el segundo punto del vector 
    down()
    #Inicializar el llenado
    begin_fill()
    #Mover el segundo punto del vector una distancia equivalente a la diferencia entre las coordenadas x del primer punto y el segundo y rotar 120 grados hacia la izquierda, repetir este paso 3 veces para completar 
    #el perímetro del triángulo
    for count in range(3):
        forward(end.x - start.x)
        left(120)
    #Finalizar el llenado
    end_fill()
    

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#1.- Agregar el color rosa a las opciones
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()