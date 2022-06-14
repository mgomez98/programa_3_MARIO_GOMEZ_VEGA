##################
#ExitWindow.py
#Date of creation: 13/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from ParkingLot import ParkingLot
from Vehicle import Vehicle

from timeUtils import getTimeFloat, getTimeTaken
from msgUtils import *

###########
# classes #
###########

class ExitWindow():

    # Logica Parqueo
    refParking = None
    
    # Ventana y widgets
    root = None
    entPlate = None

    # Botones
    btnOk = None

    def __init__(self, parent, parking: ParkingLot):
        # Recibe logica de ventana principal
        self.refParking = parking

        # Ventana salida de vehiculo
        self.root = tk.Toplevel(parent)
        self.root.geometry('325x120')
        self.root.title('Salida de vehiculo')
        self.root.config(bg='#c9c9c9')
        self.root.focus_set()

        # Widgets
        lblTitle = tk.Label(self.root, text='Parqueo - Salida de Vehiculo', font=('Times New Roman', 16), bg='#c9c9c9')

        lblPlate = tk.Label(self.root, text='Su placa', bg='#c9c9c9')
        self.entPlate = tk.Entry(self.root)

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok', width=8, anchor='center')

        # Posicionamiento
        lblTitle.place(anchor='nw', relx=0.03, rely=0.025)

        lblPlate.place(anchor='w', relx=0.03, rely=0.45)
        self.entPlate.place(anchor='w', relx=0.3, rely=0.45)

        self.btnOk.place(anchor='s', relx=0.5, rely=0.925)

        # Comandos
        self.initCommands()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def btnOkCommand(self):
        if self.validateSearch():
            self.exitParking()

    # F: Valida busqueda de vehiculo
    # I: Self
    # O: Bool
    def validateSearch(self) -> bool:
        plate = self.entPlate.get()
        if plate == '' or plate.isspace():
            warningBox(self.root, 'Parqueo', 'Debe ingresar una placa valida')
            return False

        vehicle = self.refParking.findVehicle(plate)
        if vehicle == None:
            warningBox(self.root, 'Parqueo', 'Este vehiculo no se encuentra en el parqueo, no se puede retirar')
            return False

        if not vehicle.hasPaid():
            warningBox(self.root, 'Parqueo', 'Este vehiculo no ha pagado aun')
            return False
        return True

    # F: Retira vehiculo de parqueo
    # I: Self
    # O: N/a
    def exitParking(self):
        plate = self.entPlate.get()
        vehicle = self.refParking.findVehicle(plate)
        vehicle.setExitTime( getTimeFloat() )
        self.refParking.removeVehicle(vehicle)

        if self.refParking.isTimeUp(vehicle):
            self.vehicleTimeout(vehicle)

        else:
            infoBox(self.root, 'Parqueo', 'Vehiculo retirado exitosamente')

    # F: Reingresa vehiculo sobre el limite de tiempo
    # I: Self, instancia de Vehicle
    # O: N/a
    def vehicleTimeout(self, vehicle: Vehicle):
        maxMinutes = self.refParking.getMaxMinutes()
        timeTaken = getTimeTaken( vehicle.getTimeDelta() )
        vehicle = Vehicle(
                vehicle.getPlate(),
                vehicle.getExitTime(),
                vehicle.getLotID()
        )
        self.refParking.addVehicle(vehicle)
        infoBox(self.root, 'Parqueo',\
            f'No puede salir porque excedió el tiempo permitido para ello.\
            \nTiempo máximo para salir luego del pago {maxMinutes}\
            \nTiempo que usted ha tardado {timeTaken}\
            \nDebe regresar al cajero a pagar la diferencia.')
