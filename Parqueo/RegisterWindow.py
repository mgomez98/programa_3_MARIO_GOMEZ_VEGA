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
from Vehicle import Vehicle
from pdfUtils import generateLog

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
    billing = None
    change = None
    userPayment = None
    userInputs = None # [[], []]

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

        # Variables de cobro
        self.billing = 0
        self.change = 0
        self.userPayment = 0
        self.userInputs = [[], []]
        
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
        lblShowCredit = tk.Label(self.root, text='*Clic para revelar', bg='#c9c9c9')
        lblBill = tk.Label(frmBilling, text='A pagar', bg='#c9c9c9')
        lblPaid = tk.Label(frmBilling, text='Pagado', bg='#c9c9c9')
        lblChange = tk.Label(frmBilling, text='Cambio', bg='#c9c9c9')

        # Widgets
        self.entPlate = tk.Entry(self.root, justify='right')

        self.lblEntryTime = tk.Label(frmTime, text='HH:MM    dd/mm/aaaa', bg='#c9c9c9')
        self.lblExitTime = tk.Label(frmTime, text='HH:MM    dd/mm/aaaa', bg='#c9c9c9')
        self.lblBillTime = tk.Label(frmTime, text='XXh YYm  ZZZd', bg='#c9c9c9')

        self.initCoinBtns(frmCoinBtns)

        self.initBillBtns(frmBillBtns)

        self.entCredit = tk.Entry(self.root, justify='right', show='*')

        self.initCoinChange(frmCoinChange)

        self.initBillChange(frmBillChange)

        self.lblBill = tk.Label(frmBilling, text='—', bg='#ffc9c9')
        self.lblPaid = tk.Label(frmBilling, text='—', bg='#c9ffc9')
        self.lblChange = tk.Label(frmBilling, text='—', bg='#c9ffc9')

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
        lblShowCredit.place(anchor='nw', relx=0.5, rely=0.37)
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
        self.entCredit.bind('<Return>', lambda e: self.payWithCard())
        self.entCredit.bind('<Button-1>', lambda e: self.showCard())
        self.entCredit.bind('<ButtonRelease-1>', lambda e: self.hideCard())

    # F: Funcionalidad de btnVoid
    # I: Self
    # O: N/a
    def btnVoidCommand(self):
        self.userPayment = 0
        self.change = 0
        for i, inputList in enumerate(self.userInputs):
            for j, num in enumerate(inputList):
                self.userInputs[i][j] = 0
        self.getUserPayment()
        self.displayChange()
        self.lblChange.config(text=self.change)
        self.btnConfirm.config(state='disabled')

    # F: Funcionalidad de btnConfirm
    # I: Self
    # O: N/a
    def btnConfirmCommand(self):
        outputs = self.refRegister.calculateChange(self.change)
        self.refRegister.commitInputs(self.userInputs[0], self.userInputs[1])
        self.refRegister.commitOutputs(outputs[0], outputs[1]) # TO DO agregar funcionalidad correos si cantidad menor a 5
        self.refVehicle.setBilling(self.billing)
        self.refVehicle.setPayTime(self.payTime)
        self.btnVoidCommand()
        self.entPlate.delete(0, len(self.entPlate.get()))
        self.lblBill.config(text=0)
        generateLog(self.refVehicle)
        infoBox(self.root, 'Cajero', 'Pago realizado exitosamente')

    # F: Deshabilita opciones de pago si se cumplen las condiciones
    # I: Self
    # O: N/a
    def finishPayment(self):
        if self.userPayment >= self.billing:
            self.change = self.userPayment - self.billing
            self.lblChange.config(text=self.change)
            self.disablePayment()
            if not self.refRegister.isChangePossible(self.change):
                warningBox(self.root, 'Cajero', 'No es posible dar vuelto, pago anulado')
                self.btnVoidCommand()
            else:
                self.displayChange()
                self.btnConfirm.config(state='normal')

    # F: Incrementa conteo de denominacion
    # I: Self, boton de moneda
    # O: N/a
    def coinInputIncrease(self, btn: tk.Button):
        for i, coinBtn in enumerate(self.listCoinBtns):
            if btn == coinBtn:
                self.userInputs[0][i] += 1
                break
        self.getUserPayment()
        self.finishPayment()

    # F: Incrementa conteo de denominacion
    # I: Self, boton de billete
    # O: N/a
    def billInputIncrease(self, btn: tk.Button):
        for i, billBtn in enumerate(self.listBillBtns):
            if btn == billBtn:
                self.userInputs[1][i] += 1
                break
        self.getUserPayment()
        self.finishPayment()

    # F: Actualiza desglose de cambio
    # I: Self
    # O: N/a
    def displayChange(self):
        coins = self.refRegister.getCoins()
        bills = self.refRegister.getBills()
        outputs = self.refRegister.calculateChange(self.change)
        for i, quantity in enumerate(outputs[0]):
            self.listCoinChange[i].config(text=f'{quantity} de {coins[i].getValue()}')
        for i, quantity in enumerate(outputs[1]):
            self.listBillChange[i].config(text=f'{quantity} de {bills[i].getValue()}')

    # F: Calcula acumulado de pago
    # I: Self
    # O: N/a
    def getUserPayment(self):
        self.userPayment = self.refRegister.calculatePayment(self.userInputs[0], self.userInputs[1])
        self.lblPaid.config(text=self.userPayment)

    # F: Obtiene cobro
    # I: Self
    # O: N/a
    def getBilling(self):
        self.billing = self.refRegister.calculateBill(self.refVehicle,\
                                                      self.payTime,\
                                                      self.refParking.getHourlyRate(),\
                                                      self.refParking.getMinRate())
        self.lblBill.config(text=self.billing)

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
            self.userInputs[0].append(0)
            btn.config(command=lambda b=btn: self.coinInputIncrease(b))
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
            self.userInputs[1].append(0)
            btn.config(command= lambda b=btn: self.billInputIncrease(b))
            btn.grid(pady=2)

    # F: Inicializa cambio en monedas
    # I: self, parent
    # O: N/a
    def initCoinChange(self, parent):
        self.listCoinChange = []
        lblTitle = tk.Label(parent, text='Monedas', bg='#c9c9c9')
        lblTitle.grid(pady=1)
        for coin in self.refRegister.getCoins():
            if coin.getValue() == 0:
                continue
            lbl = tk.Label(parent, text=f'— de {coin.getValue()}', bg='#c9c9c9')
            self.listCoinChange.append(lbl)
            lbl.grid(pady=1)

    # F: Inicializa cambio en billetes
    # I: self, parent
    # O: N/a
    def initBillChange(self, parent):
        self.listBillChange = []
        lblTitle = tk.Label(parent, text='Billetes', bg='#c9c9c9')
        lblTitle.grid(pady=1)
        for bill in self.refRegister.getBills():
            if bill.getValue() == 0:
                continue
            lbl = tk.Label(parent, text=f'— de {bill.getValue()}', bg='#c9c9c9')
            self.listBillChange.append(lbl)
            lbl.grid(pady=1)

    # F: Busca un vehiculo en el parqueo
    # I: self
    # O: N/a
    def searchVehicle(self):
        self.btnVoidCommand()
        plate = self.entPlate.get()
        self.refVehicle = self.refParking.findVehicle(plate)
        self.enablePayment()
        if self.refVehicle == None:
            self.lblBill.config(text=0)
            warningBox(self.root, 'Parqueo', 'Vehiculo no encontrado')
            return
        if self.refVehicle.hasPaid():
            self.disablePayment()
            warningBox(self.root, 'Cajero', 'Vehiculo ya ha pagado')
            return
        self.payTime = getTimeFloat()
        self.lblEntryTime.config(text=getTimeString( self.refVehicle.getEntryTime() ))
        self.lblExitTime.config(text=getTimeString(self.payTime))
        self.lblBillTime.config(text=getTimeBill( self.payTime - self.refVehicle.getEntryTime() ))
        self.lblChange.config(text=self.change)
        self.lblPaid.config(text=self.userPayment)
        self.getBilling()

    # F: Habilita opcion de pago
    # I: Self
    # O: N/a
    def enablePayment(self):
        if self.refVehicle == None:
            self.disablePayment()
        else:
            for btn in self.listCoinBtns:
                btn.config(state='normal')
            for btn in self.listBillBtns:
                btn.config(state='normal')
            self.btnVoid.config(state='normal')
            self.entCredit.config(state='normal')

    # F: Deshabilita opciones de pago
    # I: Self
    # O: N/a
    def disablePayment(self):
        for btn in self.listCoinBtns:
            btn.config(state='disabled')
        for btn in self.listBillBtns:
            btn.config(state='disabled')
        self.btnVoid.config(state='disabled')
        self.btnConfirm.config(state='disabled')
        self.entCredit.config(state='disabled')

    # F: Maneja pagos con tarjeta
    # I: Self
    # O: N/a
    def payWithCard(self):
        card = self.entCredit.get()
        self.entCredit.delete(0, len(card))
        if len(card) != 10:
            errorBox(self.root, 'Cajero', 'Numero de tarjeta incorrecta')
        else:
            self.userPayment = self.billing
            self.finishPayment()

    # F: Muestra numero de tarjeta
    # I: Self
    # O: N/a
    def showCard(self):
        self.entCredit.config(show='')

    # F: Oculta numero de tarjeta
    # I: Self
    # O: N/a
    def hideCard(self):
        self.entCredit.config(show='*')

################
# main program #
################

