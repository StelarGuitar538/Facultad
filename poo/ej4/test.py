from gestorMotos import gestorMotos as m
from gestorPedidos import gestorPedidos as p
   
def test():
    while True:
        print("menu de opciones")
        print("1, carga")
        print("2, asignar  nuevos pedidos a motos")
        print("3, modificar tiempo real de entrega")
        print("4, datos del conductor y promedio de entrega")
        print("5, listado para cada moto")
        
        opcion = input("ingrese opcion")
        
        if(opcion == "1"):
            m.cargarmotos()
            p.cargarPedidos()
            
        elif(opcion == "2"):
              p.asignarMoto()
              
        elif(opcion == "3"):
            p.modTiempoReal()
            
        elif(opcion == "4"):
            p.leerPatente()
            p.promedioReal()
            
        elif(opcion == "5"):
            p.total()
            p.mostracomi()
              
        
        