##################
#FrameTotalView.py
#Date of creation: 15/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from Denomination import INPUT, OUTPUT, TOTAL
from CashRegister import CashRegister

#############
# constants #
#############

COIN = 0
BILL = 1

###########
# classes #
###########

class FrameTotalView(tk.Frame):
    # Logica Cajero
    denomType = None
    refRegister = None

    # Widgets
    title = None # lbl

    countIN = None # lbl
    valueIN = None # lbl

    countOUT = None # lbl
    valueOUT = None # lbl

    countTotal = None # lbl
    valueTotal = None # lbl

    def __init__(self, master, register: CashRegister, type: int):
        super().__init__(master, bg='#c9c9c9')

        # Denominacion asignada
        self.refRegister = register

        # Frame
        self.config(width=610, height=20)
        self.title = tk.Label(self, bg='#c9c9c9')

        self.countIN = tk.Label(self, bg='#c9c9c9')
        self.valueIN = tk.Label(self, bg='#c9c9c9')

        self.countOUT = tk.Label(self, bg='#c9c9c9')
        self.valueOUT = tk.Label(self, bg='#c9c9c9')

        self.countTotal = tk.Label(self, bg='#c9c9c9')
        self.valueTotal = tk.Label(self, bg='#c9c9c9')

        # Posicionamiento
        self.title.place(anchor='center', relx=0.105, rely=0.5)
        
        self.countIN.place(anchor='center', relx=0.284, rely=0.5)
        self.valueIN.place(anchor='center', relx=0.39, rely=0.5)

        self.countOUT.place(anchor='center', relx=0.570, rely=0.5)
        self.valueOUT.place(anchor='center', relx=0.681, rely=0.5)

        self.countTotal.place(anchor='center', relx=0.831, rely=0.5)
        self.valueTotal.place(anchor='center', relx=0.927, rely=0.5)

        if type == COIN:
            self.initCoinLabels()
        elif type == BILL:
            self.initBillLabels()

#############
#  methods  #
#############

    # F: Detalla totales de monedas
    # I: Self
    # O: N/a
    def initCoinLabels(self):
        self.title.config(text='TOTAL DE MONEDAS')
        self.countIN.config(text=self.refRegister.getCoinsAmount(INPUT))
        self.valueIN.config(text=self.refRegister.getTotalCoinValue(INPUT))

        self.countOUT.config(text=self.refRegister.getCoinsAmount(OUTPUT))
        self.valueOUT.config(text=self.refRegister.getTotalCoinValue(OUTPUT))

        self.countTotal.config(text=self.refRegister.getCoinsAmount(TOTAL))
        self.valueTotal.config(text=self.refRegister.getTotalCoinValue(TOTAL))

    # F: Detalla totales de billetes
    # I: Self
    # O: N/a
    def initBillLabels(self):
        self.title.config(text='TOTAL DE BILLETES')
        self.countIN.config(text=self.refRegister.getBillsAmount(INPUT))
        self.valueIN.config(text=self.refRegister.getTotalBillValue(INPUT))

        self.countOUT.config(text=self.refRegister.getBillsAmount(OUTPUT))
        self.valueOUT.config(text=self.refRegister.getTotalBillValue(OUTPUT))

        self.countTotal.config(text=self.refRegister.getBillsAmount(TOTAL))
        self.valueTotal.config(text=self.refRegister.getTotalBillValue(TOTAL))

################
# main program #
################

