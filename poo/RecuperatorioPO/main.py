from gestorMiembro import gestor_miembro
from gestorVisualizacion import Gestor_Visualizacion
gm=gestor_miembro()
gv=Gestor_Visualizacion()
gm.leerdatos()
print("Datos de miembros cargados")
gv.leerdatos()
print("Datosde visualizaciones cargados")
if __name__=='__main__':
    ban=True
    while ban==True:
        print("======MENU DE OPCIONES======")
        print("0.Salir")
        print("1.Mostrar cantidad total de minutos que ha visto peliculas un miembro")
        print("2.Mostrar apellido,nombre y correo de los miembros que han realizado visualizaciones simultaneas")
        opcion=int(input("Ingrese su opcion:"))
        if opcion==0:
            ban=False
        if opcion==1:
            mail=input("Ingresar mail del miembro:")
            gm.buscarid(mail,gv)
        if opcion==2:
            gm.visusimul()
#id;apellidoNombre;correo
#idmiembro;idpelicula;fecha;hora;minutos