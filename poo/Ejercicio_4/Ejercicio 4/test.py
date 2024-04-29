from manejadorMotos import ManejadorM
from manejadorPedidos import ManejadorP
#import os

def test():
    """cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))"""
    M=ManejadorM()
    P=ManejadorP()
    M.cargarmotos()
    P.cargarpedidos()
    M.mostrar()
    P.mostrar()
    
    P.ordenado()
    