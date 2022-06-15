##################
#LoadWindow.py
#Date of creation: 7/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from FrameLoad import FrameLoad
from CashRegister import CashRegister
from Denomination import Denomination

###########
# classes #
###########

class LoadWindow():
    
    # Logica cajero
    refRegister = None  # Referencia CashRegister

    # Ventana y widgets
    root = None         # Tkinter toplevel
    coinFrames = None   # Lista de FrameLoad (monedas)
    billFrames = None    # Lista de FrameLoad (billetes)

    # Botones
    btnOk = None        # Boton Ok
    btnCancel = None    # Boton Cancelar
    btnEmpty = None     # Boton Vaciar Cajero

    def __init__(self, parent, register: CashRegister):

        # Recibe logica de ventana principal
        self.refRegister = register

        # Ventana cargar cajero
        self.root = tk.Toplevel(parent)
        self.root.geometry('610x350')
        self.root.title('Cargar Cajero')
        self.root.config(bg='#c9c9c9')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Cargar Cajero', font=('Times New Roman', 16), bg='#c9c9c9')

        # Widgets
        frmCoin = tk.Frame(self.root, bg='#c9c9c9')
        self.initCoinFrames(frmCoin)
        frmBill = tk.Frame(self.root, bg='#c9c9c9')
        self.initBillFrames(frmBill)

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok')
        self.btnCancel = tk.Button(self.root, text='Cancelar')
        self.btnEmpty = tk.Button(self.root, text='Vaciar cajero')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)
        self.initHeaderFrame()
        frmCoin.place(anchor='n', relx=0.5, rely=0.28)
        frmBill.place(anchor='n', relx=0.5, rely=0.6)

#############
#  methods  #
#############

    # F: Inicializa encabezado
    # I: Self
    # O: N/a
    def initHeaderFrame(self):
        frmHeader = tk.Frame(self.root, bg='#c9c9c9')

        lblPrev = tk.Label(frmHeader, text='Saldo antes de la carga', bg='#c9c9c9')
        lblLoad = tk.Label(frmHeader, text='Carga', bg='#c9c9c9')
        lblTotal = tk.Label(frmHeader, text='Saldo', bg='#c9c9c9')

        lblDen = tk.Label(frmHeader, text='Denominacion', bg='#c9c9c9')
        
        lblCountPrev = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValuePrev = tk.Label(frmHeader, text='Total', bg='#c9c9c9')
        
        lblCountLoad = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValueLoad = tk.Label(frmHeader, text='Total', bg='#c9c9c9')

        lblCountTotal = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValueTotal = tk.Label(frmHeader, text='Total', bg='#c9c9c9')

        # Posicionamiento
        frmHeader.place(anchor='nw', relx=0.03, rely=0.15)

        lblPrev.grid(row=0, column=0, columnspan=3, sticky='e', padx=(32,52))
        lblLoad.grid(row=0, column=3, columnspan=2, padx=(0,46))
        lblTotal.grid(row=0, column=5, columnspan=2)

        lblDen.grid(row=1, column=0, padx=(4, 40))

        lblCountPrev.grid(row=1, column=1, padx=(0, 22))
        lblValuePrev.grid(row=1, column=2, padx=(0, 66))

        lblCountLoad.grid(row=1, column=3, padx=(0, 25))
        lblValueLoad.grid(row=1, column=4, padx=(0, 49))

        lblCountTotal.grid(row=1, column=5, padx=(0, 15))
        lblValueTotal.grid(row=1, column=6)

    # F: Inicializa apartado de monedas
    # I: Self, parent
    # O: N/a
    def initCoinFrames(self, frame: tk.Frame):
        self.coinFrames = []
        for coin in self.refRegister.getCoins():
            if coin.getValue() > 0:
                frmLoad = FrameLoad(frame, coin, 'Moneda')
                self.coinFrames.append(frmLoad)
                frmLoad.grid()
        # TO DO Agregar frame total

    # F: Inicializa apartado de billetes
    # I: Self, parent
    # O: N/a
    def initBillFrames(self, frame: tk.Frame):
        self.billFrames = []
        for bill in self.refRegister.getBills():
            if bill.getValue() > 0:
                frmLoad = FrameLoad(frame, bill, 'Billete')
                self.billFrames.append(frmLoad)
                frmLoad.grid()
        # TO DO Agregar frame total

################
# main program #
################

# TO DO Crear frame total
# TO DO Agregar botones
# TO DO Agregar validacion colectiva
# TO DO Agregar commit colectivo