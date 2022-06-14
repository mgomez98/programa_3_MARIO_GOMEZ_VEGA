##################
#EntryWindow.py
#Date of creation: 10/06/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from ParkingLot import ParkingLot
from Vehicle import Vehicle

from timeUtils import getTimeFloat, getTimeString
from msgUtils import *

###########
# classes #
###########

class EntryWindow():

    # Logica Parqueo
    refParking = None  # Instancia ParkingLot

    time = None        # Float de tiempo de entrada

    # Ventana y widgets
    root = None        # Tkinter toplevel

    freeSlots = None   # Label espacios disponibles
    plateNum = None    # Entry placa
    slotNum = None     # Label espacio asignado
    entryTime = None   # Label hora de entrada
    hourlyRate = None  # Label precio por hora

    # Botones
    btnOk = None       # Boton Ok
    btnCancel = None   # Boton Cancelar
    btnSearch = None   # Boton Buscar

    def __init__(self, parent, parking: ParkingLot):
        # Recibe logica de ventana principal
        self.refParking = parking

        # Ventana entrada de vehiculo
        self.root = tk.Toplevel(parent)
        self.root.geometry('400x250')
        self.root.title('Entrada de vehiculo')
        self.root.config(bg='#c9c9c9')
        self.root.focus_set()

        # Widgets
        lblTitle = tk.Label(self.root, text='Parqueo - Entrada de Vehiculo', font=('Times New Roman', 16), bg='#c9c9c9')

        lblSlots = tk.Label(self.root, text='Espacios disponibles', bg='#c9c9c9')
        self.freeSlots = tk.Label(self.root, bg='#c9c9c9')

        lblPlate = tk.Label(self.root, text='Su placa', bg='#c9c9c9')
        self.plateNum = tk.Entry(self.root)

        lblAsgnSlot = tk.Label(self.root, text='Campo asignado', bg='#c9c9c9')
        self.slotNum = tk.Label(self.root, bg='#c9c9c9')

        lblTime = tk.Label(self.root, text='Hora de entrada', bg='#c9c9c9')
        self.entryTime = tk.Label(self.root, bg='#c9c9c9')

        lblRate = tk.Label(self.root, text='Precio por hora', bg='#c9c9c9')
        self.hourlyRate = tk.Label(self.root, text=self.refParking.getHourlyRate(), bg='#c9c9c9')

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok', width=8, anchor='center')
        self.btnCancel = tk.Button(self.root, text='Cancelar', width=8, anchor='center')
        self.btnSearch = tk.Button(self.root, text='Buscar', width=8, anchor='center')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)

        lblSlots.place(anchor='w', relx=0.03, rely=0.2)
        self.freeSlots.place(anchor='w', relx=0.55, rely=0.2)

        lblPlate.place(anchor='w', relx=0.03, rely=0.32)
        self.plateNum.place(anchor='w', relx=0.55, rely=0.32)

        lblAsgnSlot.place(anchor='w', relx=0.03, rely=0.44)
        self.slotNum.place(anchor='w', relx=0.55, rely=0.44)

        lblTime.place(anchor='w', relx=0.03, rely=0.56)
        self.entryTime.place(anchor='w', relx=0.55, rely=0.56)

        lblRate.place(anchor='w', relx=0.03, rely=0.68)
        self.hourlyRate.place(anchor='w', relx=0.55, rely=0.68)

        self.btnOk.place(anchor='s', relx=0.40, rely=0.925)
        self.btnCancel.place(anchor='s', relx=0.60, rely=0.925)
        self.btnSearch.place(anchor='s', relx=0.80, rely=0.925)

        # Comandos
        self.initCommands()
        self.enableParkingEntry()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
        self.btnCancel.config(command=self.btnCancelCommand)
        self.btnSearch.config(command=self.btnSearchCommand)

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def btnOkCommand(self):
        self.parkVehicle()

    # F: Funcionalidad de btnCancel
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def btnCancelCommand(self):
        self.root.destroy()

    # F: Funcionalidad de btnSearch
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def btnSearchCommand(self):
        self.searchVehicle()

    # F: Agrega instancia vehiculo al parqueo
    # I: Self
    # O: N/a
    def parkVehicle(self):
        vehicle = Vehicle(self.plateNum.get(), self.time, self.refParking.findLot())
        self.refParking.addVehicle(vehicle)
        infoBox(self.root, 'Parqueo', 'Vehiculo agregado')
        self.enableParkingEntry()

    # F: Valida duplicado de vehiculo en parqueo
    # I: Self
    # O: N/a
    def searchVehicle(self):
        plate = self.plateNum.get()
        if plate == '' or plate.isspace():
            warningBox(self.root, 'Parqueo', 'Debe ingresar una placa valida')
            return
        vehicle = self.refParking.findVehicle(plate)
        if vehicle != None:
            warningBox(self.root, 'Parqueo', 'Este vehiculo ya se encuentra en el parqueo, no se puede agregar')
            return
        self.time = getTimeFloat()
        self.entryTime.config(text=getTimeString(self.time))
        self.btnOk.config(state='normal')
        
    # F: Monitorea disponibilidad de parqueo
    # I: Self
    # O: N/a
    def enableParkingEntry(self):
        self.plateNum.delete(0, len( self.plateNum.get() ))
        self.entryTime.config(text='-')
        self.btnOk.config(state='disabled')
        if self.refParking.isFull():
            self.freeSlots.config(text='No hay espacio', fg='#ff0000', font=('TkDefaultFont', 15, 'bold'))
            self.plateNum.config(state='disabled')
            self.slotNum.config(text='-')
            self.btnSearch.config(state='disabled')
        else:
            remainingLots = self.refParking.getMaxLots() - len(self.refParking.getLots())
            self.freeSlots.config(text=remainingLots)
            self.slotNum.config(text=self.refParking.findLot())

################
# main program #
################

