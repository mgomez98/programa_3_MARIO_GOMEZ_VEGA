##################
#msgUtils.py
#Date of creation: 13/6/22
#Author: Mario Gomez Vega
##################

from tkinter import messagebox

# F: Crea messagebox de informacion
# I: parent, titulo de ventana, mensaje
# O: N/a
def infoBox(parent, title: str, msg: str):
    messagebox.showinfo(parent=parent, title=title, message=msg)

# F: Crea messagebox de alerta
# I: parent, titulo de ventana, mensaje
# O: N/a
def warningBox(parent, title: str, msg: str):
    messagebox.showwarning(parent=parent, title=title, message=msg)

# F: Crea messagebox de error
# I: parent, titulo de ventana, mensaje
# O: N/a
def errorBox(parent, title: str, msg: str):
    messagebox.showerror(parent=parent, title=title, message=msg)