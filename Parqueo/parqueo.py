##################
#Mainwindow.py
#Date of creation: 2/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

from jsonUtils import *
import os

from ConfigWindow import ConfigWindow
from LoadWindow import LoadWindow
from BalanceWindow import BalanceWindow
from EarningsWindow import EarningsWindow
from EntryWindow import EntryWindow
from RegisterWindow import RegisterWindow
from ExitWindow import ExitWindow
from About import About

###########
# classes #
###########

class MainWindow():

    # Logica Parqueo
    parking = None   # Instancia ParkingLot
    register = None  # Instancia CashRegister

    # Ventana y widgets
    root = None   # Tkinter root
    frame = None  # Frame botones

    # Botones
    btnConfig = None    # Boton configuracion
    btnLoad = None      # Boton cargar cajero
    btnBalance = None   # Boton saldo cajero
    btnEarnings = None  # Boton ingresos
    btnEntry = None     # Boton entrada vehiculo
    btnRegister = None  # Boton cajero
    btnExit = None      # Boton salida vehiculo
    btnHelp = None      # Boton ayuda
    btnAbout = None     # Boton acerca de
    btnClose = None     # Boton salir

    # Toplevel
    toplevel = None  # Toplevel activo

    def __init__(self):

        # Carga de datos guardados
        self.parking = loadParkingLot()
        self.register = loadCashRegister()
        
        # Ventana principal
        self.root = tk.Tk()
        self.root.geometry('280x480')
        self.root.title('Parqueo')
        self.root.config(bg='#c9c9c9')
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)

        # Frame botones
        self.frame = tk.Frame(self.root)

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo', font=('Times New Roman', 26), bg='#c9c9c9')

        # Botones
        self.btnConfig = tk.Button(self.frame, text='Configuracion',\
                                    anchor='center', width=16, height=2)

        self.btnLoad = tk.Button(self.frame, text='Cargar cajero',\
                                    anchor='center', width=16, height=2)

        self.btnBalance = tk.Button(self.frame, text='Saldo del cajero',\
                                    anchor='center', width=16, height=2)

        self.btnEarnings = tk.Button(self.frame, text='Ingresos de dinero',\
                                    anchor='center', width=16, height=2)

        self.btnEntry = tk.Button(self.frame, text='Entrada de vehiculo',\
                                    anchor='center', width=16, height=2)

        self.btnRegister = tk.Button(self.frame, text='Cajero del parqueo',\
                                    anchor='center', width=16, height=2)

        self.btnExit = tk.Button(self.frame, text='Salida de vehiculo',\
                                    anchor='center', width=16, height=2)

        self.btnHelp = tk.Button(self.frame, text='Ayuda',\
                                    anchor='center', width=16, height=2)

        self.btnAbout = tk.Button(self.frame, text='Acerca De',\
                                    anchor='center', width=16, height=2)

        self.btnClose = tk.Button(self.frame, text='Salir',\
                                    anchor='center', width=16, height=2)

        # Posicionamiento
        lblTitle.place(anchor='n', relx=0.5, rely=0.005)

        self.frame.place(anchor='center', relx=0.5, rely=0.55)
        
        self.btnConfig.grid(row=0, column=1)
        self.btnLoad.grid(row=1, column=1)
        self.btnBalance.grid(row=2, column=1)
        self.btnEarnings.grid(row=3, column=1)
        self.btnEntry.grid(row=4, column=1)
        self.btnRegister.grid(row=5, column=1)
        self.btnExit.grid(row=6, column=1)
        self.btnHelp.grid(row=7, column=1)
        self.btnAbout.grid(row=8, column=1)
        self.btnClose.grid(row=9, column=1)

        # Comandos
        self.initCommands()

        # Mainloop
        self.root.mainloop()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de MainWindow
    # O: N/a
    def initCommands(self):
        self.btnConfig.config(command=self.btnConfigCommand)
        self.btnLoad.config(command=self.btnLoadCommand)
        self.btnBalance.config(command=self.btnBalanceCommand)
        self.btnEarnings.config(command=self.btnEarningsCommand)
        self.btnEntry.config(command=self.btnEntryCommand)
        self.btnRegister.config(command=self.btnRegisterCommand)
        self.btnExit.config(command=self.btnExitCommand)
        self.btnHelp.config(command=self.btnHelpCommand)
        self.btnAbout.config(command=self.btnAboutCommand)
        self.btnClose.config(command=self.btnCloseCommand)

    # F: Cierra ventana y guarda cambios
    # I: Self - Instancia de MainWindow
    # O: N/a
    def closeWindow(self):
        self.root.destroy()
        writeParkingLot(self.parking)
        writeCashRegister(self.register)

    # F: Funcionalidad de btnConfig
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnConfigCommand(self):
        self.toplevel = ConfigWindow(self.root, self.parking, self.register)

    # F: Funcionalidad de btnLoad
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnLoadCommand(self):
        self.toplevel = LoadWindow(self.root, self.register)

    # F: Funcionalidad de btnBalance
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnBalanceCommand(self):
        self.toplevel = BalanceWindow(self.root, self.register)

    # F: Funcionalidad de btnEarnings
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnEarningsCommand(self):
        self.toplevel = EarningsWindow(self.root, self.register, self.parking)

    # F: Funcionalidad de btnEntry
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnEntryCommand(self):
        self.toplevel = EntryWindow(self.root, self.parking)

    # F: Funcionalidad de btnRegister
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnRegisterCommand(self):
        self.toplevel = RegisterWindow(self.root, self.register, self.parking)

    # F: Funcionalidad de btnExit
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnExitCommand(self):
        self.toplevel = ExitWindow(self.root, self.parking)

    # F: Funcionalidad de btnHelp
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnHelpCommand(self):
        os.system('manual_de_usuario_parqueo.pdf')

    # F: Funcionalidad de btnAbout
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnAboutCommand(self):
        self.toplevel = About(self.root)

    # F: Funcionalidad de btnClose
    # I: Self - Instancia de MainWindow
    # O: N/a
    def btnCloseCommand(self):
        self.closeWindow()

################
# main program #
################

window = MainWindow()