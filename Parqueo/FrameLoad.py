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
from FrameTotalLoad import FrameTotalLoad

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

    refTotalSibling = None # FrameTotalLoad

    def __init__(self, master, denomination: Denomination, name: str):
        super().__init__(master, bg='#c9c9c9')
        
        # Denominacion asignada
        self.refDenomination = denomination

        # Frame
        self.config(width=610, height=20)
        countStart = self.getSavedAmount()
        valueStart = self.getSavedValue()
        self.title = tk.Label(self, text=f'{name} de {self.refDenomination.getValue()}', bg='#c9c9c9')

        self.countPrev = tk.Label(self, text=countStart, bg='#c9c9c9')
        self.valuePrev = tk.Label(self, text=valueStart, bg='#c9c9c9')

        self.countLoad = tk.Entry(self, width=9, justify='right')
        self.countLoad.insert(0, '0')
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
        self.refTotalSibling.updateDisplay()

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
        countTotal = self.getInputTotal(amount)
        valueTotal = self.getValueTotal(amount)
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

    # F: Getter de carga previa (cantidad)
    # I: Self
    # O: int
    def getSavedAmount(self):
        return self.refDenomination.getAmount(TOTAL)

    # F: Getter de carga previa (valor)
    # I: Self
    # O: int
    def getSavedValue(self):
        return self.refDenomination.getValueByType(TOTAL)

    # F: Getter de entrada de usuario
    # I: Self
    # O: int
    def getInput(self):
        return int(self.countLoad.get())

    # F: Getter de valor de entrada
    # I: Self
    # O: int
    def getInputValue(self):
        return self.refDenomination.calculateTotalValue(self.getInput())

    # F: Setter de FrameTotalLoad hermano
    # I: Self, instancia de FrameTotalLoad
    # O: N/a
    def setSibling(self, frame: FrameTotalLoad):
        self.refTotalSibling = frame

    # F: Getter de carga estimada
    # I: Self, cantidad cargada
    # O: int
    def getInputTotal(self, amount: int):
        return self.getSavedAmount() + amount

    # F: Getter de valor estimado
    # I: Self, cantidad cargada
    # O: int
    def getValueTotal(self, amount: int):
        return self.getSavedValue() + self.refDenomination.calculateTotalValue(amount)

    # F: Vacia datos del frame
    # I: Self
    # O: N/a
    def setEmpty(self):
        inputSize = len(self.countLoad.get())
        self.countLoad.delete(0, inputSize)
        self.countLoad.insert(0, '0')
        self.updateDisplay()

################
# main program #
################

