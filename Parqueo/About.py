##################
#About.py
#Date of creation: 21/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class About():
    # Ventana y botones
    root = None

    def __init__(self, parent):
        self.root = tk.Toplevel(parent)
        self.root.geometry('400x140')
        self.root.title('Acerca De')
        self.root.configure(bg='#c9c9c9')
        self.root.focus_set()

        # Widgets locales
        name = tk.Label(self.root, text='Parqueo', font=('Times New Roman', 18), bg='#c9c9c9')
        version = tk.Label(self.root, text='v1.0.0', font=('Times New Roman', 12), bg='#c9c9c9')
        date = tk.Label(self.root, text='Fecha de creacion: 21/06/22', font=('Times New Roman', 12), bg='#c9c9c9')
        auth = tk.Label(self.root, text='Autor: Mario Gomez Vega', font=('Times New Roman', 12), bg='#c9c9c9')

        # Posicionamiento
        name.place(anchor='n', relx=0.5, rely=0.06)
        version.place(anchor='n', relx=0.5, rely=0.29)
        date.place(anchor='n', relx=0.5, rely=0.47)
        auth.place(anchor='n', relx=0.5, rely=0.65)

#############
#  methods  #
#############



################
# main program #
################
