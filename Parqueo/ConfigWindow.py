##################
#ConfigWindow.py
#Date of creation: 4/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk
from msgUtils import *
import pyisemail
from re import match

from CashRegister import CashRegister
from ParkingLot import ParkingLot

###########
# classes #
###########

class ConfigWindow():

    # Logica Parqueo
    refParking = None  # Instancia ParkingLot
    refRegister = None  # Instancia CashRegister

    # Ventana y widgets
    root = None      # Tkinter toplevel
    frmText = None   # Frame texto
    frmEntry = None  # Frame entry

    # Labels
    lblLots = None      # Label espacios
    lblHourly = None    # Label precio hora
    lblMin = None       # Label precio minimo
    lblMail = None      # Label correo
    lblMinutes = None   # Label minutos para salir

    lblCoinType = None  # Label tipo moneda
    lblCoin1 = None     # Label moneda 1
    lblCoin2 = None     # Label moneda 2
    lblCoin3 = None     # Label moneda 3

    lblBillType = None  # Label tipo billete
    lblBill1 = None     # Label billete 1
    lblBill2 = None     # Label billete 2
    lblBill3 = None     # Label billete 3
    lblBill4 = None     # Label billete 4
    lblBill5 = None     # Label billete 5

    # Entries
    entLots = None     # Entry espacios
    entHourly = None   # Entry precio hora
    entMin = None      # Entry precio minimo
    entMail = None     # Entry correo
    entMinutes = None  # Entry minutos para salir

    entCoin1 = None    # Entry moneda 1
    entCoin2 = None    # Entry moneda 2
    entCoin3 = None    # Entry moneda 3

    entBill1 = None    # Entry billete 1
    entBill2 = None    # Entry billete 2
    entBill3 = None    # Entry billete 3
    entBill4 = None    # Entry billete 4
    entBill5 = None    # Entry billete 5

    # Botones
    btnOk = None      # Boton Ok
    btnCancel = None  # Boton Cancelar

    def __init__(self, parent, parking: ParkingLot, register: CashRegister):
        # Recibe logica de ventana principal
        self.refParking = parking
        self.refRegister = register

        # Ventana configuracion
        self.root = tk.Toplevel(parent)
        self.root.geometry('600x550')
        self.root.title('Configuracion')
        self.root.config(bg='#c9c9c9')
        self.root.focus_set()

        # Frame texto
        self.frmText = tk.Frame(self.root, height=600, bg='#c9c9c9')

        # Frame entries
        self.frmEntry = tk.Frame(self.root, height=600, bg='#c9c9c9')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Configuracion', font=('Times New Roman', 16), bg='#c9c9c9')

        # Labels
        self.lblLots = tk.Label(self.frmText, text='Cantidad de espacios en el parqueo (entero >= 1)', anchor='w', bg='#c9c9c9')
        self.lblHourly = tk.Label(self.frmText, text='Precio por hora (flotante con m??ximo 2 decimales >=0)', anchor='w', bg='#c9c9c9')
        self.lblMin = tk.Label(self.frmText, text='Pago m??nimo (flotante con m??ximo 2 decimales >=0)', anchor='w', bg='#c9c9c9')
        self.lblMail = tk.Label(self.frmText, text='Correo electr??nico del supervisor', anchor='w', bg='#c9c9c9')
        self.lblMinutes = tk.Label(self.frmText, text='Minutos m??ximos para salir despu??s del pago (entero >=0)', anchor='w', bg='#c9c9c9')

        self.lblCoinType = tk.Label(self.frmText, text='Tipos de moneda (m??ximo 3 tipos, enteros >= 0):', anchor='w', bg='#c9c9c9')
        self.lblCoin1 = tk.Label(self.frmText, text='Moneda 1, la de menor denominaci??n (ejemplo 50)', anchor='w', bg='#c9c9c9')
        self.lblCoin2 = tk.Label(self.frmText, text='Moneda 2, denominaci??n siguiente a la anterior (ejemplo 100)', anchor='w', bg='#c9c9c9')
        self.lblCoin3 = tk.Label(self.frmText, text='Moneda 3, denominaci??n siguiente a la anterior (ejemplo 500)', anchor='w', bg='#c9c9c9')

        self.lblBillType = tk.Label(self.frmText, text='Tipos de billetes (m??ximo 5 tipos, enteros >= 0):', anchor='w', bg='#c9c9c9')
        self.lblBill1 = tk.Label(self.frmText, text='Billete 1, el de menor denominaci??n (ejemplo 1000)', anchor='w', bg='#c9c9c9')
        self.lblBill2 = tk.Label(self.frmText, text='Billete 2, denominaci??n siguiente a la anterior (ejemplo 2000)', anchor='w', bg='#c9c9c9')
        self.lblBill3 = tk.Label(self.frmText, text='Billete 3, denominaci??n siguiente a la anterior (ejemplo 5000)', anchor='w', bg='#c9c9c9')
        self.lblBill4 = tk.Label(self.frmText, text='Billete 4, denominaci??n siguiente a la anterior (ejemplo 10000)', anchor='w', bg='#c9c9c9')
        self.lblBill5 = tk.Label(self.frmText, text='Billete 5, denominaci??n siguiente a la anterior (ejemplo 20000)', anchor='w', bg='#c9c9c9')

        # Entries parqueo
        self.entLots = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entHourly = tk.Entry(self.frmEntry, justify='right', width=10)
        self.entMin = tk.Entry(self.frmEntry, justify='right', width=10)
        self.entMail = tk.Entry(self.frmEntry, justify='right', width=30)
        self.entMinutes = tk.Entry(self.frmEntry, justify='right', width=7)

        # Entries cajero
        self.entCoin1 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entCoin2 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entCoin3 = tk.Entry(self.frmEntry, justify='right', width=7)

        self.entBill1 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entBill2 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entBill3 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entBill4 = tk.Entry(self.frmEntry, justify='right', width=7)
        self.entBill5 = tk.Entry(self.frmEntry, justify='right', width=7)

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok', width=8, anchor='center')
        self.btnCancel = tk.Button(self.root, text='Cancelar', width=8, anchor='center')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)

        self.frmText.place(anchor='w', relx=0.03, rely=0.5)

        self.lblLots.grid(row=0, pady=(0, 20), sticky='w')
        self.lblHourly.grid(row=1, pady=(0, 20), sticky='w')
        self.lblMin.grid(row=2, pady=(0, 20), sticky='w')
        self.lblMail.grid(row=3, pady=(0, 20), sticky='w')
        self.lblMinutes.grid(row=4, pady=(0, 20), sticky='w')

        self.lblCoinType.grid(row=5, sticky='w')
        self.lblCoin1.grid(row=6, sticky='w')
        self.lblCoin2.grid(row=7, sticky='w')
        self.lblCoin3.grid(row=8, pady=(0, 20), sticky='w')

        self.lblBillType.grid(row=9, sticky='w')
        self.lblBill1.grid(row=10, sticky='w')
        self.lblBill2.grid(row=11, sticky='w')
        self.lblBill3.grid(row=12, sticky='w')
        self.lblBill4.grid(row=13, sticky='w')
        self.lblBill5.grid(row=14, sticky='w')


        self.frmEntry.place(anchor='e', relx=0.97, rely=0.5)

        self.entLots.grid(row=0, pady=(0, 22))
        self.entHourly.grid(row=1, pady=(0, 22))
        self.entMin.grid(row=2, pady=(0, 22))
        self.entMail.grid(row=3, pady=(0, 22))
        self.entMinutes.grid(row=4, pady=(0, 42))

        self.entCoin1.grid(row=5, pady=(0, 2))
        self.entCoin2.grid(row=6, pady=(0, 2))
        self.entCoin3.grid(row=7, pady=(0, 44))

        self.entBill1.grid(row=8, pady=(0, 2))
        self.entBill2.grid(row=9, pady=(0, 2))
        self.entBill3.grid(row=10, pady=(0, 2))
        self.entBill4.grid(row=11, pady=(0, 2))
        self.entBill5.grid(row=12)


        self.btnOk.place(anchor='s', relx=0.43, rely=0.98)
        self.btnCancel.place(anchor='s', relx=0.57, rely=0.98)

        # Comandos
        self.initCommands()

        # Carga configuraciones parqueo
        self.loadParkingConfig()
        self.enableParkingConfig()
        self.loadRegisterConfig()
        self.enableRegisterConfig()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de Config
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
        self.btnCancel.config(command=self.btnCancelCommand)

    # F: Habilita entries de configuracion (parqueo)
    # I: Self - Instancia de Config
    # O: N/a
    def enableParkingConfig(self):
        isParkingEmpty = self.refParking.isEmpty()
        isParkingEmpty = ('disabled', 'normal')[isParkingEmpty]

        self.entLots.config(state=isParkingEmpty)
        self.entHourly.config(state=isParkingEmpty)
        self.entMin.config(state=isParkingEmpty)
        self.entMail.config(state=isParkingEmpty)
        self.entMinutes.config(state=isParkingEmpty)

    # F: Carga configuracion de parqueo
    # I: Self - Instancia de Config
    # O: N/a
    def loadParkingConfig(self):
        self.entLots.insert(0, self.refParking.getMaxLots())
        self.entHourly.insert(0, self.refParking.getHourlyRate())
        self.entMin.insert(0, self.refParking.getMinRate())
        self.entMail.insert(0, self.refParking.getManagerMail())
        self.entMinutes.insert(0, self.refParking.getMaxMinutes())

    # F: Guarda configuracion de parqueo
    # I: Self - Instancia de Config
    # O: N/a
    def saveParkingConfig(self):
        self.refParking.setMaxLots( int(self.entLots.get()) )
        self.refParking.setHourlyRate( float(self.entHourly.get()) )
        self.refParking.setMinRate( float(self.entMin.get()) )
        self.refParking.setManagerMail( self.entMail.get() )
        self.refParking.setMaxMinutes( int(self.entMinutes.get()) )

    # F: Verifica si un numero en un string es un flotante
    # I: Self, string
    # O: bool
    def isFloat(self, string):
        if match('\d+\.\d+', string):
            return True
        return False

    # F: Valida configuracion de parqueo
    # I: Self
    # O: bool
    def validateParkingConfig(self) -> bool:
        entLots = self.entLots.get()
        entHourly = self.entHourly.get()
        entMin = self.entMin.get()
        entMail = self.entMail.get()
        entMinutes = self.entMinutes.get()
        '''print(not (entLots.isnumeric() and entHourly.isnumeric()\
            and entMin.isnumeric() and entMinutes.isnumeric()))
        print((entLots.isnumeric(), entHourly.isdecimal(), entMin.isdecimal(), entMinutes.isnumeric()))'''

        if not (entLots.isnumeric() and self.isFloat(entHourly)\
            and self.isFloat(entMin) and entMinutes.isnumeric()):
            errorBox(self.root, 'Configuracion Parqueo', 'Debe dar entradas validas')
            return False
        if not pyisemail.is_email(entMail, True):
            errorBox(self.root, 'Configuracion Parqueo', 'Ingrese un correo valido')
            return False
        if int(entLots) < 1 or float(entHourly) < 0 or float(entMin) < 0\
            or int(entMinutes) < 0:
            errorBox(self.root, 'Configuracion Parqueo', 'Debe dar entradas validas')
            return False
        return True

    # F: Habilita entries de configuracion (cajero)
    # I: Self - Instancia de Config
    # O: N/a
    def enableRegisterConfig(self):
        isRegisterEmpty = self.refRegister.isEmpty()
        isRegisterEmpty = ('disabled', 'normal')[isRegisterEmpty]

        self.entCoin1.config(state=isRegisterEmpty)
        self.entCoin2.config(state=isRegisterEmpty)
        self.entCoin3.config(state=isRegisterEmpty)

        self.entBill1.config(state=isRegisterEmpty)
        self.entBill2.config(state=isRegisterEmpty)
        self.entBill3.config(state=isRegisterEmpty)
        self.entBill4.config(state=isRegisterEmpty)
        self.entBill5.config(state=isRegisterEmpty)

    # F: Carga configuracion de cajero
    # I: Self - Instancia de Config
    # O: N/a
    def loadRegisterConfig(self):
        coinList = self.refRegister.getCoins()
        billList = self.refRegister.getBills()
        self.entCoin1.insert(0, coinList[0].getValue())
        self.entCoin2.insert(0, coinList[1].getValue())
        self.entCoin3.insert(0, coinList[2].getValue())

        self.entBill1.insert(0, billList[0].getValue())
        self.entBill2.insert(0, billList[1].getValue())
        self.entBill3.insert(0, billList[2].getValue())
        self.entBill4.insert(0, billList[3].getValue())
        self.entBill5.insert(0, billList[4].getValue())

    # F: Guarda configuracion de cajero
    # I: Self - Instancia de Config
    # O: N/a
    def saveRegisterConfig(self):
        self.refRegister.initCoins(
            [int(self.entCoin1.get()),
             int(self.entCoin2.get()),
             int(self.entCoin3.get())]
        )
        self.refRegister.initBills(
            [int(self.entBill1.get()),
             int(self.entBill2.get()),
             int(self.entBill3.get()),
             int(self.entBill4.get()),
             int(self.entBill5.get())]
        )

    # F: Valida configuracion de cajero
    # I: Self
    # O: bool
    def validateRegisterConfig(self) -> bool:
        entCoins = (self.entCoin1.get(), self.entCoin2.get(), self.entCoin3.get())
        entBills = (self.entBill1.get(), self.entBill2.get(), self.entBill3.get(),\
                    self.entBill4.get(), self.entBill5.get())
        if not self.validateDenomination(entCoins):
            return False
        if not self.validateDenomination(entBills):
            return False
        return True

    # F: Valida denominaciones
    # I: Self, tupla de denominaciones
    # O: bool
    def validateDenomination(self, moneyTuple):
        hasZero = False
        prevEntry = '0'
        for coin in moneyTuple:
            if not coin.isnumeric():
                errorBox(self.root, 'Configuracion Cajero', 'Debe dar entradas validas')
                return False
            if int(coin) == 0:
                hasZero = True
            if int(coin) != 0 and hasZero:
                errorBox(self.root, 'Configuracion Cajero', 'Denominaciones despues de una omision deben ser 0')
                return False
            if not hasZero and int(coin) <= int(prevEntry):
                errorBox(self.root, 'Configuracion Cajero', 'Denominaciones deben seguir orden ascendente')
                return False
            prevEntry = coin
        return True

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de Config
    # O: N/a
    def btnOkCommand(self):
        isParkingConfigValid = self.validateParkingConfig()
        isRegisterConfigValid = self.validateRegisterConfig()
        if isParkingConfigValid:
            self.saveParkingConfig()
        if isRegisterConfigValid:
            self.saveRegisterConfig()
        if isParkingConfigValid and isRegisterConfigValid:
            infoBox(self.root, 'Configuracion', 'Se han guardado los cambios')
            self.root.destroy()

    # F: Funcionalidad de btnCancel
    # I: Self - Instancia de Config
    # O: N/a
    def btnCancelCommand(self):
        self.root.destroy()

################
# main program #
################

