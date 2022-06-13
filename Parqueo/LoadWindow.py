##################
#LoadWindow.py
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

class LoadWindow():

    # Ventana y widgets
    root = None         # Tkinter toplevel
    frame = None        # Frame principal

    frmDen = None       # Frame denominacion
    frmBalPrev = None   # Frame saldo anterior
    frmLoad = None      # Frame carga
    frmBal = None       # Frame saldo

    # Listas de widgets
    lstDen = None       # Lista denominacion (Labels)

    lstBalPrev1 = None  # Lista saldo anterior cantidad (Labels)
    lstBalPrev2 = None  # Lista saldo anterior total (Labels)

    lstLoad1 = None     # Lista carga cantidad (Entries)
    lstLoad2 = None     # Lista carga total (Labels)

    lstBal1 = None      # Lista saldo cantidad (Labels)
    lstBal2 = None      # Lista saldo total (Labels)

    # Botones
    btnOk = None        # Boton Ok
    btnCancel = None    # Boton Cancelar
    btnEmpty = None     # Boton Vaciar Cajero

    def __init__(self):
        # Ventana cargar cajero
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Cargar Cajero')

        # Frame principal
        self.frame = tk.Frame(self.root)

        # Frames por categoria
        self.frmDen = tk.Frame(self.frame)
        self.frmBalPrev = tk.Frame(self.frame)
        self.frmLoad = tk.Frame(self.frame)
        self.frmBal = tk.Frame(self.frame)

        # Widgets locales
        lblTitle = tk.Label(self.root, text='Parqueo - Cargar Cajero', font=('Times New Roman', 16))
        lblBalPrev = tk.Label(self.root, text='Saldo antes de la carga')
        lblLoad = tk.Label(self.root, text='Carga')
        lblBal = tk.Label(self.root, text='Saldo')

        # Listas de widgets
        # lstDen
        self.lstDen = []
        for a in range(15):
            self.lstDen.append(tk.Label(self.frmDen, text=a, anchor='w'))
        
        # lstBalPrev
        self.lstBalPrev1 = []
        for b in range(13):
            self.lstBalPrev1.append(tk.Label(self.frmBalPrev, text=b))
        self.lstBalPrev2 = []
        for c in range(13):
            self.lstBalPrev2.append(tk.Label(self.frmBalPrev, text=c))

        # lstLoad
        self.lstLoad1 = []
        for d in range(13):
            self.lstLoad1.append(tk.Entry(self.frmLoad))
        self.lstLoad2 = []
        for e in range(13):
            self.lstLoad2.append(tk.Label(self.frmLoad, text=e))

        # lstBal
        self.lstBal1 = []
        for f in range(13):
            self.lstBal1.append(tk.Label(self.frmBal, text=f))
        self.lstBal2 = []
        for g in range(15):
            self.lstBal2.append(tk.Label(self.frmBal, text=g))

        # Botones
        self.btnOk = tk.Button(self.root, text='Ok')
        self.btnCancel = tk.Button(self.root, text='Cancelar')
        self.btnEmpty = tk.Button(self.root, text='Vaciar cajero')

        # Posicionamiento
        lblTitle.grid(row=0, column=0)

        lblBalPrev.grid(row=1, column=1)
        lblLoad.grid(row=1, column=2)
        lblBal.grid(row=1, column=3)

        self.frmDen.grid(row=2, column=0)
        self.frmBalPrev.grid(row=2, column=1)
        self.frmLoad.grid(row=2, column=2)
        self.frmBal.grid(row=2, column=3)

        

        # Mainloop
        self.root.mainloop()

#############
#  methods  #
#############



################
# main program #
################

