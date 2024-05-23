def mostrar_partos_multiples(self, GM):
        multiples = []
        i = 0
        while i < len(self.__lista):
            nacimiento = self.__lista[i]
            j = 0
            while j < len(multiples):
                if multiples[j][0] == nacimiento:  
                    multiples[j].append(nacimiento)
                    break
                j += 1
            else:
                multiples.append([nacimiento])
            i += 1

        i = 0
        while i < len(multiples):
            parto_multiple = multiples[i]
            if len(parto_multiple) > 1:
                j = 0
                while j < len(GM.getarreglo()):
                    mama = GM.getarreglo()[j]
                    if mama.get_dni() == parto_multiple[0].get_dni_madre():
                        print(f"Mamá: {mama.get_nombre_apellido()}, DNI: {mama.get_dni()}, Edad: {mama.get_edad()}")
                        print(f"Fecha de parto múltiple: {parto_multiple[0].get_fecha()}")
                        k = 0
                        while k < len(parto_multiple):
                            nacimiento = parto_multiple[k]
                            print(f"  Tipo de parto: {nacimiento.get_tipoparto()}, Peso: {nacimiento.get_peso()}, Altura: {nacimiento.get_altura()}")
                            k += 1
                        break
                    j += 1
            i += 1