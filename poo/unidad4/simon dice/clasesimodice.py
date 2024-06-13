from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from gestor import GestorDeJugadores
from clasejugador import Jugador
import datetime

class SimonDice:
    __ventana_principal: object
    __dialogo_usuario = None

    def __init__(self, ventana_principal):
        self.__ventana_principal = ventana_principal
        self.__ventana_principal.title("Py -SimonGame")
        self.colores = ["#ff0000", "#00ff00", "#0000ff", "#ffff00"]
        self.secuencia = []
        self.secuencia_usuario = []
        self.secuencia_usuario_activa = False
        self.boton_verde = self.crear_boton(self.colores[0], 0)
        self.boton_rojo = self.crear_boton(self.colores[1], 1)
        self.boton_amarillo = self.crear_boton(self.colores[2], 2)
        self.boton_azul = self.crear_boton(self.colores[3], 3)
        self.mostrar_dialogo_nuevo_usuario()

        # Posiciona los botones en la ventana
        self.boton_verde.grid(row=0, column=0)
        self.boton_rojo.grid(row=0, column=1)
        self.boton_amarillo.grid(row=1, column=0)
        self.boton_azul.grid(row=1, column=1)

    def crear_boton(self, color, indice):
        canvas = tk.Canvas(self.__ventana_principal, bg=color, width=100, height=100, relief="raised")
        canvas.bind("<Button-1>", lambda event, c=color: self.al_hacer_click_en_boton(event, canvas, c))
        return canvas

    def iniciar_juego(self):
        self.secuencia = []
        self.secuencia_usuario = []
        self.secuencia_usuario_activa = False
        self.agregar_color_a_juego()

    def agregar_color_a_juego(self):
        self.secuencia.append(random.choice(self.colores))
        self.mostrar_secuencia()

    def mostrar_secuencia(self):
        if self.dificultad == "Principiante":
            retraso = 1000  # Milisegundos
        elif self.dificultad == "Intermedio":
            retraso = 700
        elif self.dificultad == "Avanzado":
            retraso = 500

        for i, color in enumerate(self.secuencia):
            self.__ventana_principal.after(retraso * i, lambda color=color: self.cambiar_color_botones(color))
            self.__ventana_principal.after(retraso * i + retraso // 2, self.restaurar_color_botones)
        self.__ventana_principal.after(retraso * len(self.secuencia), self.activar_botones)

    def cambiar_color_botones(self, color):
        if color == self.colores[0]:
            self.boton_verde.config(bg="#ffffff")
        elif color == self.colores[1]:
            self.boton_rojo.config(bg="#ffffff")
        elif color == self.colores[2]:
            self.boton_amarillo.config(bg="#ffffff")
        elif color == self.colores[3]:
            self.boton_azul.config(bg="#ffffff")

    def restaurar_color_botones(self):
        self.boton_verde.config(bg=self.colores[0])
        self.boton_rojo.config(bg=self.colores[1])
        self.boton_amarillo.config(bg=self.colores[2])
        self.boton_azul.config(bg=self.colores[3])

    def mostrar_dialogo_nuevo_usuario(self):
        self.__dialogo_usuario = tk.Toplevel()
        self.__dialogo_usuario.geometry('300x200')
        self.__dialogo_usuario.resizable(0, 0)
        tk.Label(self.__dialogo_usuario, text="Nombre de Usuario:").pack()
        self.entrada_nombre = tk.Entry(self.__dialogo_usuario)
        self.entrada_nombre.pack()

        tk.Label(self.__dialogo_usuario, text="Selecciona la Dificultad:").pack()
        self.var_dificultad = tk.StringVar(value="Principiante")
        dificultades = ["Principiante", "Intermedio", "Avanzado"]
        for dificultad in dificultades:
            tk.Radiobutton(self.__dialogo_usuario, text=dificultad, variable=self.var_dificultad, value=dificultad).pack()

        self.boton_confirmar = tk.Button(self.__dialogo_usuario, text='Confirmar', command=self.guardar_nombre_usuario)
        self.boton_confirmar.pack()

    def guardar_nombre_usuario(self):
        nombre_usuario = self.entrada_nombre.get()
        dificultad = self.var_dificultad.get()
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        nuevo_jugador = Jugador(nombre_usuario, fecha_actual, hora_actual, 0, dificultad)
        gestor_jugadores = GestorDeJugadores("pysimonpuntajes.json")
        gestor_jugadores.guardar_jugador(nuevo_jugador)
        self.__dialogo_usuario.destroy()
        self.dificultad = dificultad
        self.nombre_usuario = nombre_usuario
        self.iniciar_juego()

    def al_hacer_click_en_boton(self, event, canvas, color):
        if not self.secuencia_usuario_activa:
            return
        canvas.config(bg="#ffffff")
        self.__ventana_principal.after(500, lambda: canvas.config(bg=color))
        self.secuencia_usuario.append(color)
        if self.secuencia[:len(self.secuencia_usuario)] == self.secuencia_usuario:
            if len(self.secuencia) == len(self.secuencia_usuario):
                messagebox.showinfo("¡Bien hecho!", "Has completado la secuencia. Tu puntuación es: " + str(len(self.secuencia)))
                self.actualizar_puntuacion(len(self.secuencia))
                self.secuencia_usuario = []
                self.desactivar_botones()
                self.agregar_color_a_juego()
        else:
            messagebox.showinfo("¡Oh no!", "Has perdido. Tu puntuación final es: " + str(len(self.secuencia) - 1))
            self.actualizar_puntuacion(len(self.secuencia) - 1)
            self.__ventana_principal.quit()

    def actualizar_puntuacion(self, puntaje):
        gestor_jugadores = GestorDeJugadores("pysimonpuntajes.json")
        for jugador in gestor_jugadores.jugadores:
            if jugador.get_nombre() == self.nombre_usuario:
                jugador._Jugador__puntaje = puntaje
                gestor_jugadores.guardar_jugadores()
                break

    def desactivar_botones(self):
        self.boton_verde.unbind("<Button-1>")
        self.boton_rojo.unbind("<Button-1>")
        self.boton_amarillo.unbind("<Button-1>")
        self.boton_azul.unbind("<Button-1>")
        self.secuencia_usuario_activa = False

    def activar_botones(self):
        self.boton_verde.bind("<Button-1>", lambda event: self.al_hacer_click_en_boton(event, self.boton_verde, self.colores[0]))
        self.boton_rojo.bind("<Button-1>", lambda event: self.al_hacer_click_en_boton(event, self.boton_rojo, self.colores[1]))
        self.boton_amarillo.bind("<Button-1>", lambda event: self.al_hacer_click_en_boton(event, self.boton_amarillo, self.colores[2]))
        self.boton_azul.bind("<Button-1>", lambda event: self.al_hacer_click_en_boton(event, self.boton_azul, self.colores[3]))
        self.secuencia_usuario_activa = True

if __name__ == '__main__':
    ventana = tk.Tk()
    juego = SimonDice(ventana)
    ventana.mainloop()
