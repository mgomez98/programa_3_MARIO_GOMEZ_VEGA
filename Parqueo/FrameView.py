##################
#FrameView.py
#Date of creation: 15/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from Denomination import Denomination, INPUT, OUTPUT, TOTAL

###########
# classes #
###########

class FrameView(tk.Frame):

    # Denominacion asociada
    refDenomination = None

    # Widgets
    title = None # lbl

    countIN = None # lbl
    valueIN = None # lbl

    countOUT = None # lbl
    valueOUT = None # lbl

    countTotal = None # lbl
    valueTotal = None # lbl

    def __init__(self, master, denomination: Denomination, name: str):
        super().__init__(master, bg='#c9c9c9')

        # Denominacion asignada
        self.refDenomination = denomination

        # Frame
        self.config(width=610, height=20)
        self.title = tk.Label(self, text=f'{name} de {self.refDenomination.getValue()}', bg='#c9c9c9')

        self.countIN = tk.Label(self, text=self.refDenomination.getAmount(INPUT), bg='#c9c9c9')
        self.valueIN = tk.Label(self, text=self.refDenomination.getValueByType(INPUT), bg='#c9c9c9')

        self.countOUT = tk.Label(self, text=self.refDenomination.getAmount(OUTPUT), bg='#c9c9c9')
        self.valueOUT = tk.Label(self, text=self.refDenomination.getValueByType(OUTPUT), bg='#c9c9c9')

        self.countTotal = tk.Label(self, text=self.refDenomination.getAmount(TOTAL), bg='#c9c9c9')
        self.valueTotal = tk.Label(self, text=self.refDenomination.getValueByType(TOTAL), bg='#c9c9c9')

        # Posicionamiento
        self.title.place(anchor='center', relx=0.105, rely=0.5)
        
        self.countIN.place(anchor='center', relx=0.284, rely=0.5)
        self.valueIN.place(anchor='center', relx=0.39, rely=0.5)

        self.countOUT.place(anchor='center', relx=0.570, rely=0.5)
        self.valueOUT.place(anchor='center', relx=0.681, rely=0.5)

        self.countTotal.place(anchor='center', relx=0.831, rely=0.5)
        self.valueTotal.place(anchor='center', relx=0.927, rely=0.5)

#############
#  methods  #
#############



################
# main program #
################

