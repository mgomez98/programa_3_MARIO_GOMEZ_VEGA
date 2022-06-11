##################
#AddVehicle.py
#Date of creation: 10/06/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class AddVehicle():
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

    def __init__(self):
        # Ventana entrada de vehiculo
        self.root = tk.Tk()
        self.root.geometry('400x250')
        self.root.title('Entrada de vehiculo')

        # Widgets
        lblTitle = tk.Label(self.root, text='Parqueo - Entrada de Vehiculo', font=('Times New Roman', 16))

        lblSlots = tk.Label(self.root, text='Espacios disponibles')
        self.freeSlots = tk.Label(self.root, text='xxxxxxxxxx')

        lblPlate = tk.Label(self.root, text='Su placa')
        self.plateNum = tk.Entry(self.root)

        lblAsgnSlot = tk.Label(self.root, text='Campo asignado')
        self.slotNum = tk.Label(self.root, text='XXXXXXXXXX')

        lblTime = tk.Label(self.root, text='Hora de entrada')
        self.entryTime = tk.Label(self.root, text='hh:mm dd/mm/aaaa')

        lblRate = tk.Label(self.root, text='Precio por hora')
        self.hourlyRate = tk.Label(self.root, text='xxxxxxxxxx')

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok', width=8, anchor='center')
        self.btnCancel = tk.Button(self.root, text='Cancelar', width=8, anchor='center')

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

        self.btnOk.place(anchor='s', relx=0.60, rely=0.925)
        self.btnCancel.place(anchor='s', relx=0.80, rely=0.925)

        # Comandos
        self.initCommands()

        # Mainloop
        self.root.mainloop()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de AddVehicle
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
        self.btnCancel.config(command=self.btnCancelCommand)

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de AddVehicle
    # O: 
    def btnOkCommand(self):
        print('Ok')

    # F: Funcionalidad de btnCancel
    # I: Self - Instancia de AddVehicle
    # O: 
    def btnCancelCommand(self):
        print('Cancelar')

################
# main program #
################

window = AddVehicle()