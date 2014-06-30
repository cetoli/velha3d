from glow import *
_gs=glow('main')
cena = canvas()
cena.width = 400
cena.height = 400
#box(color=color.blue)
#box(size=(2,2,2),opacity=0.2)
#sphere(pos=(2,2,2), color =color.red)
print("oi")
pecas =[(box,color.blue), (sphere, color.red)] * 5
for linha in range(3):
   for coluna in range(3):
       for camada in range(3):
        box(pos=(coluna*3,linha *3,camada *3), size=(2,2,2), opacity=0.2)
#for linha in range(3):
   #for coluna in range(3):
       #box(pos=(coluna*3,0,0), size=(2,2,2), opacity=0.2)
