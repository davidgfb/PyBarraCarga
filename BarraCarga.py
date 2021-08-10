from pygame import init
from pygame.draw import rect
from pygame.display import set_mode, update
from pygame.event import get

PANTALLA, NEGRO, BLANCO, porcentaje, v, ESTA_NEGATIVO = set_mode((500, 400)),\
        (0, 0, 0), (255, 255, 255), 0, 5, False
POSITIVO, NEGATIVO = (BLANCO, NEGRO, NEGRO),\
                     (NEGRO, BLANCO, BLANCO)
COLORES = POSITIVO 

def pintaPorcentaje():
    print("\nporcentaje =", porcentaje)
    

if ESTA_NEGATIVO:
    COLORES = NEGATIVO 

C, C1, C2 = COLORES

PANTALLA.fill(C)
rect(PANTALLA, C1, (200, 150, 100, 50), 1)

init()  
update()
pintaPorcentaje()

arrayRectangulos = [] # todo

while True:
    ent = input("\n+/-:\n")

    if ent in "+-":
        if ent == "+":
            if porcentaje < 100: # (-inf, 100)
                porcentaje += v # todo: repasa limites

            else:
                print("\ne: porcentaje negativo")
                      
        elif ent == "-":
            if porcentaje > 0: # (0, inf)
                porcentaje -= v

            else:
                print("\ne: porcentaje excedido")
                
        rect(PANTALLA, C2, (200, 150,\
                            porcentaje, 50))
    
        update()
        pintaPorcentaje()

    for event in get():
        pass

