##################
#EarningsWindow.py
#Date of creation: 7/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class EarningsWindow():
    # Ventana y widgets
    root = None              # Tkinter toplevel
    fromDate = None          # Entry inicio fecha
    untilDate = None         # Entry final fecha

    cashEarnings = None      # Label efectivo
    cardEarnings = None      # Label tarjeta
    totalEarnings = None     # Label total
    estimateEarnings = None  # Label estimado

    btnOk = None             # Boton OK

    def __init__(self):
        
        # Ventana Ingresos
        self.root = tk.Tk()
        self.root.geometry('400x250')
        self.root.title('Ingresos de Dinero')

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Ingresos de Dinero', font=('Times New Roman', 16))
        
        frmDate = tk.Frame(self.root)
        lblFromDate = tk.Label(frmDate, text='Del dia')
        lblUntilDate = tk.Label(frmDate, text='Al dia')
        
        frmEarnings = tk.Frame(self.root)
        lblCash = tk.Label(frmEarnings, text='Total de ingresos en efectivo')
        lblCard = tk.Label(frmEarnings, text='Total de ingresos por tarjeta de credito')
        lblTotal = tk.Label(frmEarnings, text='Total de ingresos')
        lblEstimate = tk.Label(frmEarnings, text='Estimado de ingresos por recibir')

        # Entries
        self.fromDate = tk.Entry(frmDate)
        self.untilDate = tk.Entry(frmDate)

        # Labels
        self.cashEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx')
        self.cardEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx')
        self.totalEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx')
        self.estimateEarnings = tk.Label(frmEarnings, text='xxx.xxx.xxx')

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

        # Mainloop
        self.root.mainloop()

#############
#  methods  #
#############

    # F: Asigna comandos a botones del menu
    # I: Self - Instancia de Earnings
    # O: N/a
    def initCommands(self):
        self.btnOk.config(command=self.btnOkCommand)

    # F: Funcionalidad de btnOk
    # I: Self - Instancia de Earnings
    # O: 
    def btnOkCommand(self):
        print('Ok')

################
# main program #
################

