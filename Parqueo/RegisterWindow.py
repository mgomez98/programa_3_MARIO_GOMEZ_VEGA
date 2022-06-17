##################
#RegisterWindow.py
#Date of creation: 16/6/22 
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from msgUtils import *
from timeUtils import getTimeFloat, getTimeString, getTimeBill
from CashRegister import CashRegister
from ParkingLot import ParkingLot

###########
# classes #
###########

class RegisterWindow():

    # Referencias logica
    refRegister = None
    refParking = None

    # Variables
    payTime = None
    refVehicle = None

    # Ventana y widgets
    root = None            # Tkinter toplevel
    entPlate = None        # entry placa
    lblEntryTime = None    # label hora entrada
    lblExitTime = None     # label hora salida
    lblBillTime = None     # label tiempo cobrado

    listCoinBtns = None    # lista botones monedas
    listBillBtns = None    # lista botones billetes
    entCredit = None         # entry tarjeta credito

    listCoinChange = None  # lista cambio monedas
    listBillChange = None  # lista cambio billetes

    lblBill = None         # label a pagar
    lblPaid = None         # label pagado
    lblChange = None       # label cambio

    btnVoid = None         # boton anular
    btnConfirm = None      # boton confirmar

    def __init__(self, parent, register: CashRegister, parking: ParkingLot):

        # Logica
        self.refRegister = register
        self.refParking = parking
        
        # Ventana cajero
        self.root = tk.Toplevel(parent)
        self.root.geometry('650x600')
        self.root.title('Cajero')
        self.root.config(bg='#c9c9c9')

        # Frames
        frmTime = tk.Frame(self.root, bg='#c9c9c9')
        frmCoinBtns = tk.Frame(self.root, bg='#c9c9c9')
        frmBillBtns = tk.Frame(self.root, bg='#c9c9c9')
        frmCoinChange = tk.Frame(self.root, bg='#c9c9c9')
        frmBillChange = tk.Frame(self.root, bg='#c9c9c9')
        frmBilling = tk.Frame(self.root, bg='#c9c9c9')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Cajero del Parqueo', font=('Times New Roman', 16), bg='#c9c9c9')
        lblHourly = tk.Label(self.root, text=f'{self.refParking.getHourlyRate()} por hora', bg='#c9c9c9')

        lblEntry = tk.Label(frmTime, text='Hora de entrada', bg='#c9c9c9')
        lblExit = tk.Label(frmTime, text='Hora de salida', bg='#c9c9c9')
        lblBillTime = tk.Label(frmTime, text='Tiempo cobrado', bg='#c9c9c9')

        lblStep1 = tk.Label(self.root, text='Paso 1: Su placa', bg='#c9c9c9')
        lblStep2 = tk.Label(self.root, text='Paso 2: Su pago en:', bg='#c9c9c9')
        lblStep3 = tk.Label(self.root, text='Paso 3: Su cambio en:', bg='#c9c9c9')

        lblCredit = tk.Label(self.root, text='Tarjeta de Credito', bg='#c9c9c9')
        lblBill = tk.Label(frmBilling, text='A pagar', bg='#c9c9c9')
        lblPaid = tk.Label(frmBilling, text='Pagado', bg='#c9c9c9')
        lblChange = tk.Label(frmBilling, text='Cambio', bg='#c9c9c9')

        # Widgets
        self.entPlate = tk.Entry(self.root, justify='right')

        self.lblEntryTime = tk.Label(frmTime, text='HH:MM    dd/mm/aaaa', bg='#c9c9c9')
        self.lblExitTime = tk.Label(frmTime, text='HH:MM    dd/mm/aaaa', bg='#c9c9c9')
        self.lblBillTime = tk.Label(frmTime, text='XXh YYm  ZZZd', bg='#c9c9c9')

        # Crear lista botones moneda
        self.initCoinBtns(frmCoinBtns)

        # Crear lista botones billete
        self.initBillBtns(frmBillBtns)

        self.entCredit = tk.Entry(self.root, justify='right')

        # Crear lista cambio monedas
        self.initCoinChange(frmCoinChange)

        # Crear lista cambio billetes
        self.initBillChange(frmBillChange)

        self.lblBill = tk.Label(frmBilling, text='XXXXXX', bg='#ffc9c9')
        self.lblPaid = tk.Label(frmBilling, text='XXXXX', bg='#c9ffc9')
        self.lblChange = tk.Label(frmBilling, text='XXXXX', bg='#c9ffc9')

        # Botones
        self.btnVoid = tk.Button(self.root, text='Anular el pago')
        self.btnConfirm = tk.Button(self.root, text='Confirmar pago')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)
        lblHourly.place(anchor='nw', relx=0.5, rely=0.039)

        lblStep1.place(anchor='w', relx=0.03, rely=0.1)
        self.entPlate.place(anchor='w', relx=0.2, rely=0.1)

        frmTime.place(anchor='nw', relx=0.03, rely=0.15)
        lblEntry.grid(row=0, column=0, pady=1, sticky='w')
        lblExit.grid(row=1, column=0, pady=1, sticky='w')
        lblBillTime.grid(row=2, column=0, pady=1, sticky='w')
        self.lblEntryTime.grid(row=0, column=1, pady=1, sticky='e')
        self.lblExitTime.grid(row=1, column=1, pady=1, sticky='e')
        self.lblBillTime.grid(row=2, column=1, pady=1, sticky='e')

        lblStep2.place(anchor='nw', relx=0.03, rely=0.3)
        frmCoinBtns.place(anchor='nw', relx=0.225, rely=0.3)
        frmBillBtns.place(anchor='nw', relx=0.325, rely=0.3)

        lblStep3.place(anchor='w', relx=0.03, rely=0.65)
        frmCoinChange.place(anchor='nw', relx=0.25, rely=0.632)
        frmBillChange.place(anchor='nw', relx=0.37, rely=0.632)

        lblCredit.place(anchor='nw', relx=0.5, rely=0.3)
        self.entCredit.place(anchor='nw', relx=0.5, rely=0.34)

        frmBilling.place(anchor='nw', relx=0.8, rely=0.3)
        lblBill.grid(row=0, column=0)
        self.lblBill.grid(row=1, column=0, columnspan=2, pady=(0, 4))
        lblPaid.grid(row=2, column=0)
        self.lblPaid.grid(row=3, column=0, pady=(0, 4))
        lblChange.grid(row=4, column=0)
        self.lblChange.grid(row=5, column=0)

        self.btnVoid.place(anchor='w', relx=0.03, rely=0.95)
        self.btnConfirm.place(anchor='w', relx=0.19, rely=0.95)

        # Comandos
        self.initCommands()
        self.enablePayment()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self
    # O: N/a
    def initCommands(self):
        self.btnVoid.config(command=self.btnVoidCommand)
        self.btnConfirm.config(command=self.btnConfirmCommand)
        self.entPlate.bind('<Return>', lambda e: self.searchVehicle())

    # F: Funcionalidad de btnVoid
    # I: Self
    # O: N/a
    def btnVoidCommand(self):
        print('Anular')

    # F: Funcionalidad de btnConfirm
    # I: Self
    # O: N/a
    def btnConfirmCommand(self):
        pass

    # F: Inicializa botones de moneda
    # I: self, parent
    # O: N/a
    def initCoinBtns(self, parent):
        self.listCoinBtns = []
        lblTitle = tk.Label(parent, text='Monedas', bg='#c9c9c9')
        lblTitle.grid(pady=2)
        for coin in self.refRegister.getCoins():
            if coin.getValue() == 0:
                continue
            btn = tk.Button(parent, text=coin.getValue(), width=7)
            self.listCoinBtns.append(btn)
            btn.grid(pady=2)

    # F: Inicializa botones de billete
    # I: self, parent
    # O: N/a
    def initBillBtns(self, parent):
        self.listBillBtns = []
        lblTitle = tk.Label(parent, text='Billetes', bg='#c9c9c9')
        lblTitle.grid(pady=2)
        for bill in self.refRegister.getBills():
            if bill.getValue() == 0:
                continue
            btn = tk.Button(parent, text=bill.getValue(), width=7)
            self.listBillBtns.append(btn)
            btn.grid(pady=2)

    # F: Inicializa cambio en monedas
    # I: self, parent
    # O: N/a
    def initCoinChange(self, parent):
        self.listCoinChange = []
        lblTitle = tk.Label(parent, text='Monedas', bg='#c9c9c9')
        lblTitle.grid(pady=1)
        for num in range(3):
            lbl = tk.Label(parent, text='XX de 500', bg='#c9c9c9')
            self.listCoinChange.append(lbl)
            lbl.grid(pady=1)

    # F: Inicializa cambio en billetes
    # I: self, parent
    # O: N/a
    def initBillChange(self, parent):
        self.listBillChange = []
        lblTitle = tk.Label(parent, text='Billetes', bg='#c9c9c9')
        lblTitle.grid(pady=1)
        for num in range(5):
            lbl = tk.Label(parent, text='XX de 50000', bg='#c9c9c9')
            self.listBillChange.append(lbl)
            lbl.grid(pady=1)

    # F: Busca un vehiculo en el parqueo
    # I: self
    # O: N/a
    def searchVehicle(self):
        plate = self.entPlate.get()
        self.refVehicle = self.refParking.findVehicle(plate)
        self.enablePayment()
        if self.refVehicle == None:
            warningBox(self.root, 'Parqueo', 'Vehiculo no encontrado')
            return
        self.payTime = getTimeFloat()
        self.lblEntryTime.config(text=getTimeString( self.refVehicle.getEntryTime() ))
        self.lblExitTime.config(text=getTimeString(self.payTime))
        self.lblBillTime.config(text=getTimeBill( self.payTime - self.refVehicle.getEntryTime() ))

    # F: Habilita opcion de pago
    # I: Self
    # O: N/a
    def enablePayment(self):
        if self.refVehicle == None:
            for btn in self.listCoinBtns:
                btn.config(state='disabled')
            for btn in self.listBillBtns:
                btn.config(state='disabled')
            self.btnVoid.config(state='disabled')
            self.btnConfirm.config(state='disabled')
            self.entCredit.config(state='disabled')
        else:
            for btn in self.listCoinBtns:
                btn.config(state='normal')
            for btn in self.listBillBtns:
                btn.config(state='normal')
            self.btnVoid.config(state='normal')
            self.btnConfirm.config(state='normal')
            self.entCredit.config(state='normal')

################
# main program #
################

