import numpy as np

class AreglosNumpy:
    def __init__(self):
        self.arreglo1 = np.arr1([234, 452, 567, 823, 900])
        self.arreglo2 = np.arr2([22, 15, 54, 70, 15, 34, 49, 15])
        self.arrcopy = None
        self.arrview = None
        self.fappend = None
        self.fsplit = None
        self.fwhere = None
        self.fsort = None
        
#funcion copy
def copy (self):
    self.arrcopy = np.copy(self.arreglo1)


#funcion view
def view(self):
    self.arrview = np.view(self.arreglo2)

#funcion append

def append(self):
    self.fappend = np.concatenate((self.arreglo1, self.arreglo2))

#funcion split
def split(self):
    self.fsplit = np.split(self.arreglo1, 3)

#funcion where
def where(self):
    self.fwhere = np.where(self.arreglo2 == 15)

#funcion sort
def sort(self):
    self.fsort = np.sort(self.arreglo1)

