import os

def test():

    try:
        os.mkdir("carpeta1", 0o777)
    except FileExistsError:
        print("la carpeta existe")
    else:
        print("se creo la carpeta")
    finally:
        print("ejecucion terminada")
if __name__ == "__main__":
    test()