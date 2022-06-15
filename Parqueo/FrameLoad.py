##################
#FrameLoad.py
#Date of creation: 14/6/22
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

class FrameLoad(tk.Frame):
    
    # Denominacion asociada
    refDenomination = None

    # Widgets
    title = None # lbl

    countPrev = None # lbl
    valuePrev = None # lbl

    countLoad = None # entry
    valueLoad = None # lbl

    countTotal = None # lbl
    valueTotal = None # lbl

    def __init__(self, master, denomination: Denomination, name: str):
        super().__init__(master, bg='#c9c9c9')
        
        # Denominacion asignada
        self.refDenomination = denomination

        # Frame
        self.config(width=610, height=20)
        countStart = self.refDenomination.getAmount(TOTAL)
        valueStart = self.refDenomination.getValueByType(TOTAL)
        self.title = tk.Label(self, text=f'{name} de {self.refDenomination.getValue()}', bg='#c9c9c9')

        self.countPrev = tk.Label(self, text=countStart, bg='#c9c9c9')
        self.valuePrev = tk.Label(self, text=valueStart, bg='#c9c9c9')

        self.countLoad = tk.Entry(self, width=9, justify='right')
        self.valueLoad = tk.Label(self, text='—', bg='#c9c9c9')

        self.countTotal = tk.Label(self, text=countStart, bg='#c9c9c9')
        self.valueTotal = tk.Label(self, text=valueStart, bg='#c9c9c9')

        # Posicionamiento
        self.title.place(anchor='center', relx=0.105, rely=0.5)
        
        self.countPrev.place(anchor='center', relx=0.284, rely=0.5)
        self.valuePrev.place(anchor='center', relx=0.39, rely=0.5)

        self.countLoad.place(anchor='center', relx=0.570, rely=0.5)
        self.valueLoad.place(anchor='center', relx=0.681, rely=0.5)

        self.countTotal.place(anchor='center', relx=0.831, rely=0.5)
        self.valueTotal.place(anchor='center', relx=0.927, rely=0.5)

        # Eventos
        self.countLoad.bind('<KeyRelease>', lambda e: self.updateDisplay())

#############
#  methods  #
#############

    # F: Actualiza valores del frame
    # I: Self
    # O: N/a
    def updateDisplay(self):
        if not self.validateInput():
            self.valueLoad.config(text='—')
            self.updateTotal(0)
        else:
            amountInput = int(self.countLoad.get())
            self.updateLoad(amountInput)
            self.updateTotal(amountInput)

    # F: Actualiza carga de dinero
    # I: Self, valores nuevos
    # O: N/a
    def updateLoad(self, amount: int):
        tempValue = self.refDenomination.calculateTotalValue(amount)
        self.valueLoad.config(text=tempValue)

    # F: Actualiza total de dinero
    # I: Self, valores nuevos
    # O: N/a
    def updateTotal(self, amount: int):
        countTotal = self.refDenomination.getAmount(TOTAL) + amount
        valueTotal = self.refDenomination.getValueByType(TOTAL)\
                     + self.refDenomination.calculateTotalValue(amount)
        self.countTotal.config(text=countTotal)
        self.valueTotal.config(text=valueTotal)

    # F: Valida que las entradas sean numericas
    # I: Self
    # O: Retorna bool
    def validateInput(self) -> bool:
        amountInput = self.countLoad.get()
        return amountInput.isnumeric()

    # F: Guarda las entradas
    # I: Self
    # O: N/a
    def commitInput(self):
        amountInput = int(self.countLoad.get())
        self.refDenomination.increaseAmount(amountInput)

################
# main program #
################

