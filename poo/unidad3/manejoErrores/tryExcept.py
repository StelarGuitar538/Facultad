def test():
    
    
    try:
        varx = 10
        vary = "8"
        varz = varx / vary
        print(varz)
    except TypeError:
        print("error en el tipo de dato")
    else:
        print("se ejecuta el else")
    finally:
        print("ejecucion terminada")
     
if __name__ == "__main__":
    test()