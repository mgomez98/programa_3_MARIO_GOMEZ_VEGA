##################
#EarningsWindow.py
#Date of creation: 7/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from CashRegister import CashRegister
from ParkingLot import ParkingLot
from timeUtils import validateDateString, getTimeFloat
from msgUtils import *

###########
# classes #
###########

class EarningsWindow():
    # Logica parqueo
    refRegister = None
    refParking = None

    # Ventana y widgets
    root = None              # Tkinter toplevel
    fromDate = None          # Entry inicio fecha
    untilDate = None         # Entry final fecha

    cashEarnings = None      # Label efectivo
    cardEarnings = None      # Label tarjeta
    totalEarnings = None     # Label total
    estimateEarnings = None  # Label estimado

    btnOk = None             # Boton OK

    def __init__(self, parent, register: CashRegister, parking: ParkingLot):

        self.refRegister = register
        self.refParking = parking
        
        # Ventana Ingresos
        self.root = tk.Toplevel(parent)
        self.root.geometry('400x250')
        self.root.title('Ingresos de Dinero')
        self.root.config(bg='#c9c9c9')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Ingresos de Dinero', font=('Times New Roman', 16), bg='#c9c9c9')
        
        frmDate = tk.Frame(self.root, bg='#c9c9c9')
        lblFromDate = tk.Label(frmDate, text='Del dia', bg='#c9c9c9')
        lblUntilDate = tk.Label(frmDate, text='Al dia', bg='#c9c9c9')
        
        frmEarnings = tk.Frame(self.root, bg='#c9c9c9')
        lblCash = tk.Label(frmEarnings, text='Total de ingresos en efectivo', bg='#c9c9c9')
        lblCard = tk.Label(frmEarnings, text='Total de ingresos por tarjeta de credito', bg='#c9c9c9')
        lblTotal = tk.Label(frmEarnings, text='Total de ingresos', bg='#c9c9c9')
        lblEstimate = tk.Label(frmEarnings, text='Estimado de ingresos por recibir', bg='#c9c9c9')

        # Entries
        self.fromDate = tk.Entry(frmDate)
        self.untilDate = tk.Entry(frmDate)

        # Labels
        self.cashEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx', bg='#c9c9c9')
        self.cardEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx', bg='#c9c9c9')
        self.totalEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx', bg='#c9c9c9')
        self.estimateEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx', bg='#c9c9c9')

        # Boton
        self.btnOk = tk.Button(self.root, text='Ok', width=8, anchor='center')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)

        frmDate.place(anchor='w', relx=0.03, rely=0.25)
        lblFromDate.grid(row=0, column=0, padx=(0, 20), sticky='w')
        self.fromDate.grid(row=0, column=1)

        lblUntilDate.grid(row=1, column=0, padx=(0, 20), sticky='w')
        self.untilDate.grid(row=1, column=1)


        frmEarnings.place(anchor='w', relx=0.03, rely=0.575)
        lblCash.grid(row=0, column=0, padx=(0, 50), sticky='w')
        self.cashEarnings.grid(row=0, column=1)

        lblCard.grid(row=1, column=0, padx=(0, 50), sticky='w')
        self.cardEarnings.grid(row=1, column=1)

        lblTotal.grid(row=2, column=0, padx=(0, 50), pady=(0, 15), sticky='w')
        self.totalEarnings.grid(row=2, column=1, pady=(0, 15))

        lblEstimate.grid(row=3, column=0, padx=(0, 50), sticky='w')
        self.estimateEarnings.grid(row=3, column=1)

        self.btnOk.place(anchor='s', relx=0.75, rely=0.925)

        # Comandos
        self.initCommands()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de Earnings
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
        self.fromDate.bind('<Return>', lambda e: self.searchLog())
        self.untilDate.bind('<Return>', lambda e: self.searchLog())

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de Earnings
    # O: 
    def btnOkCommand(self):
        self.root.destroy()

    # F:
    # I:
    # O:
    def searchLog(self):
        fromDate = validateDateString(self.fromDate.get())
        untilDate = validateDateString(self.untilDate.get())
        if fromDate == None or untilDate == None:
            errorBox(self.root, 'Parqueo', 'Ingrese fechas validas')
            return
        self.displayEarnings(fromDate, untilDate)

    # F:
    # I:
    # O:
    def displayEarnings(self, fromDate: float, untilDate: float):
        pendingVehicles = self.refParking.getPendingVehicles()
        self.totalEarnings.config(text=self.refParking.getTotalEarnings(fromDate, untilDate))
        self.estimateEarnings.config(text=self.refRegister.getEstimatedEarnings(pendingVehicles, getTimeFloat(), self.refParking.getHourlyRate(), self.refParking.getMinRate()))

################
# main program #
################

