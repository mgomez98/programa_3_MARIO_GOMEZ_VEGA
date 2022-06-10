##################
#Config.py
#Date of creation: 4/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class Config():

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

    def __init__(self):
        # Ventana configuracion
        self.root = tk.Tk()
        self.root.geometry('530x550')
        self.root.title('Configuracion')

        # Frame texto
        self.frmText = tk.Frame(self.root, height=600)

        # Frame entries
        self.frmEntry = tk.Frame(self.root, height=600)

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Configuracion', font=('Times New Roman', 16))

        # Labels
        self.lblLots = tk.Label(self.frmText, text='Cantidad de espacios en el parqueo (entero >= 1)', anchor='w')
        self.lblHourly = tk.Label(self.frmText, text='Precio por hora (flotante con máximo 2 decimales >=0)', anchor='w')
        self.lblMin = tk.Label(self.frmText, text='Pago mínimo (flotante con máximo 2 decimales >=0)', anchor='w')
        self.lblMail = tk.Label(self.frmText, text='Correo electrónico del supervisor', anchor='w')
        self.lblMinutes = tk.Label(self.frmText, text='Minutos máximos para salir después del pago (entero >=0)', anchor='w')

        self.lblCoinType = tk.Label(self.frmText, text='Tipos de moneda (máximo 3 tipos, enteros >= 0):', anchor='w')
        self.lblCoin1 = tk.Label(self.frmText, text='Moneda 1, la de menor denominación (ejemplo 50)', anchor='w')
        self.lblCoin2 = tk.Label(self.frmText, text='Moneda 2, denominación siguiente a la anterior (ejemplo 100)', anchor='w')
        self.lblCoin3 = tk.Label(self.frmText, text='Moneda 3, denominación siguiente a la anterior (ejemplo 500)', anchor='w')

        self.lblBillType = tk.Label(self.frmText, text='Tipos de billetes (máximo 5 tipos, enteros >= 0):', anchor='w')
        self.lblBill1 = tk.Label(self.frmText, text='Billete 1, el de menor denominación (ejemplo 1000)', anchor='w')
        self.lblBill2 = tk.Label(self.frmText, text='Billete 2, denominación siguiente a la anterior (ejemplo 2000)', anchor='w')
        self.lblBill3 = tk.Label(self.frmText, text='Billete 3, denominación siguiente a la anterior (ejemplo 5000)', anchor='w')
        self.lblBill4 = tk.Label(self.frmText, text='Billete 4, denominación siguiente a la anterior (ejemplo 10000)', anchor='w')
        self.lblBill5 = tk.Label(self.frmText, text='Billete 5, denominación siguiente a la anterior (ejemplo 20000)', anchor='w')

        # Entries
        self.entLots = tk.Entry(self.frmEntry)
        self.entHourly = tk.Entry(self.frmEntry)
        self.entMin = tk.Entry(self.frmEntry)
        self.entMail = tk.Entry(self.frmEntry)
        self.entMinutes = tk.Entry(self.frmEntry)

        self.entCoin1 = tk.Entry(self.frmEntry)
        self.entCoin2 = tk.Entry(self.frmEntry)
        self.entCoin3 = tk.Entry(self.frmEntry)

        self.entBill1 = tk.Entry(self.frmEntry)
        self.entBill2 = tk.Entry(self.frmEntry)
        self.entBill3 = tk.Entry(self.frmEntry)
        self.entBill4 = tk.Entry(self.frmEntry)
        self.entBill5 = tk.Entry(self.frmEntry)

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

        # Mainloop
        self.root.mainloop()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de Config
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)
        self.btnCancel.config(command=self.btnCancelCommand)

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de Config
    # O: 
    def btnOkCommand(self):
        print('Ok')

    # F: Funcionalidad de btnCancel
    # I: Self - Instancia de Config
    # O: 
    def btnCancelCommand(self):
        print('Cancelar')

################
# main program #
################

window = Config()