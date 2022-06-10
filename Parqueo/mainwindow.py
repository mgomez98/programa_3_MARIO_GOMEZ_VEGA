##################
#Mainwindow.py
#Date of creation: 2/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class MainWindow():

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

    def __init__(self):
        
        # Ventana principal
        self.root = tk.Tk()
        self.root.geometry('280x420')
        self.root.title('Parqueo')
        self.root.config(bg='#a0a0a0')

        # Frame botones
        self.frame = tk.Frame(self.root)

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo', font=('Times New Roman', 26))

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

    # F: Funcionalidad de btnConfig
    # I: Self - Instancia de MainWindow
    # O: 
    def btnConfigCommand(self):
        print('configuracion')

    # F: Funcionalidad de btnLoad
    # I: Self - Instancia de MainWindow
    # O:
    def btnLoadCommand(self):
        print('cargar cajero')

    # F: Funcionalidad de btnBalance
    # I: Self - Instancia de MainWindow
    # O:
    def btnBalanceCommand(self):
        print('saldo del cajero')

    # F: Funcionalidad de btnEarnings
    # I: Self - Instancia de MainWindow
    # O:
    def btnEarningsCommand(self):
        print('ingresos de dinero')

    # F: Funcionalidad de btnEntry
    # I: Self - Instancia de MainWindow
    # O:
    def btnEntryCommand(self):
        print('entrada de vehiculo')

    # F: Funcionalidad de btnRegister
    # I: Self - Instancia de MainWindow
    # O:
    def btnRegisterCommand(self):
        print('cajero del parqueo')

    # F: Funcionalidad de btnExit
    # I: Self - Instancia de MainWindow
    # O:
    def btnExitCommand(self):
        print('salida de vehiculo')

    # F: Funcionalidad de btnHelp
    # I: Self - Instancia de MainWindow
    # O:
    def btnHelpCommand(self):
        print('ayuda')

################
# main program #
################

window = MainWindow()