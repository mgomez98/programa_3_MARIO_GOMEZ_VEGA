##################
#RegisterWindow.py
#Date of creation: 15/6/22 
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from CashRegister import CashRegister
from FrameView import FrameView
from FrameTotalView import FrameTotalView, COIN, BILL

###########
# classes #
###########

class RegisterWindow():
    
    # Logica cajero
    refRegister = None  # Referencia CashRegister

    # Ventana y widgets
    root = None         # Tkinter toplevel
    coinFrames = None   # Lista de FrameLoad (monedas)
    billFrames = None    # Lista de FrameLoad (billetes)

    # Botones
    btnOk = None        # Boton Ok

    def __init__(self, parent, register: CashRegister):

        # Recibe logica de ventana principal
        self.refRegister = register

        # Ventana cargar cajero
        self.root = tk.Toplevel(parent)
        self.root.geometry('610x390')
        self.root.title('Cargar Cajero')
        self.root.config(bg='#c9c9c9')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Saldo del Cajero', font=('Times New Roman', 16), bg='#c9c9c9')

        # Widgets
        frmCoin = tk.Frame(self.root, bg='#c9c9c9')
        self.initCoinFrames(frmCoin)
        frmBill = tk.Frame(self.root, bg='#c9c9c9')
        self.initBillFrames(frmBill)

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok', width=8)

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)
        self.initHeaderFrame()
        frmCoin.place(anchor='n', relx=0.5, rely=0.23)
        frmBill.place(anchor='n', relx=0.5, rely=0.49)

        self.btnOk.place(anchor='s', relx=0.2, rely=0.925)

        # Comandos
        self.initCommands()

#############
#  methods  #
#############

    # F: Inicializa encabezado
    # I: Self
    # O: N/a
    def initHeaderFrame(self):
        frmHeader = tk.Frame(self.root, bg='#c9c9c9')

        lblPrev = tk.Label(frmHeader, text='Entradas', bg='#c9c9c9')
        lblLoad = tk.Label(frmHeader, text='Salidas', bg='#c9c9c9')
        lblTotal = tk.Label(frmHeader, text='Saldo', bg='#c9c9c9')

        lblDen = tk.Label(frmHeader, text='Denominacion', bg='#c9c9c9')
        
        lblCountPrev = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValuePrev = tk.Label(frmHeader, text='Total', bg='#c9c9c9')
        
        lblCountLoad = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValueLoad = tk.Label(frmHeader, text='Total', bg='#c9c9c9')

        lblCountTotal = tk.Label(frmHeader, text='Cantidad', bg='#c9c9c9')
        lblValueTotal = tk.Label(frmHeader, text='Total', bg='#c9c9c9')

        # Posicionamiento
        frmHeader.place(anchor='nw', relx=0.03, rely=0.10)

        lblPrev.grid(row=0, column=0, columnspan=3, sticky='e', padx=(0,97))
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
                frmView = FrameView(frame, coin, 'Monedas')
                self.coinFrames.append(frmView)
                frmView.grid()
        frmTotal = FrameTotalView(frame, self.refRegister, COIN)
        frmTotal.grid()

    # F: Inicializa apartado de billetes
    # I: Self, parent
    # O: N/a
    def initBillFrames(self, frame: tk.Frame):
        self.billFrames = []
        for bill in self.refRegister.getBills():
            if bill.getValue() > 0:
                frmView = FrameView(frame, bill, 'Billetes')
                self.billFrames.append(frmView)
                frmView.grid()
        frmTotal = FrameTotalView(frame, self.refRegister, BILL)
        frmTotal.grid()

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de RegisterWindow
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
    
    # F: Funcionalidad de btnOk
    # I: Self - Instancia de RegisterWindow
    # O: N/a
    def btnOkCommand(self):
        self.root.destroy()

################
# main program #
################

