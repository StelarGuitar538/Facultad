import csv

def calcular():
    i = 0
    f = open("/home/la-net-05/Escritorio/practica1/movimientosabril2024.csv", "r")
    reader = csv.reader(f)
    for linea in reader:
        i += 1
    return(i)