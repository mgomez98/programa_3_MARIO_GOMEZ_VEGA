##################
#FrameTotalLoad.py
#Date of creation: 15/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import tkinter as tk

###########
# classes #
###########

class FrameTotalLoad(tk.Frame):
    # FrameLoad hermanos
    refSiblingFrames = None # list

    # Widgets
    title = None # lbl

    countPrev = None # lbl
    valuePrev = None # lbl

    countLoad = None # lbl
    valueLoad = None # lbl

    countTotal = None # lbl
    valueTotal = None # lbl

    def __init__(self, master, siblings: list, name: str):
        super().__init__(master, bg='#c9c9c9')

        self.refSiblingFrames = siblings
        for frame in self.refSiblingFrames:
            frame.setSibling(self)

        # Frame
        self.config(width=610, height=20)
        self.title = tk.Label(self, text=f'TOTAL DE {name}', bg='#c9c9c9')

        self.countPrev = tk.Label(self, text=self.getStartAmount(), bg='#c9c9c9')
        self.valuePrev = tk.Label(self, text=self.getStartValue(), bg='#c9c9c9')

        self.countLoad = tk.Label(self, text='0', bg='#c9c9c9')
        self.valueLoad = tk.Label(self, text='0', bg='#c9c9c9')

        self.countTotal = tk.Label(self, text=self.getStartAmount(), bg='#c9c9c9')
        self.valueTotal = tk.Label(self, text=self.getStartValue(), bg='#c9c9c9')

        # Posicionamiento
        self.title.place(anchor='center', relx=0.105, rely=0.5)
        
        self.countPrev.place(anchor='center', relx=0.284, rely=0.5)
        self.valuePrev.place(anchor='center', relx=0.39, rely=0.5)

        self.countLoad.place(anchor='center', relx=0.570, rely=0.5)
        self.valueLoad.place(anchor='center', relx=0.681, rely=0.5)

        self.countTotal.place(anchor='center', relx=0.831, rely=0.5)
        self.valueTotal.place(anchor='center', relx=0.927, rely=0.5)

#############
#  methods  #
#############

    # F: Getter de cantidad total inicial
    # I: Self
    # O: int
    def getStartAmount(self) -> int:
        count = 0
        for frame in self.refSiblingFrames:
            count += frame.getSavedAmount()
        return count

    # F: Getter de valor total inicial
    # I: Self
    # O: int
    def getStartValue(self) -> int:
        value = 0
        for frame in self.refSiblingFrames:
            value += frame.getSavedValue()
        return value

    # F: Getter de total de entradas
    # I: Self
    # O: int
    def getInputSum(self):
        total = 0
        for frame in self.refSiblingFrames:
            if frame.validateInput():
                total += frame.getInput()
        return total

    # F: Getter de valor total de entradas
    # I: Self
    # O: int
    def getValueSum(self):
        total = 0
        for frame in self.refSiblingFrames:
            if frame.validateInput():
                total += frame.getInputValue()
        return total

    # F: Getter de estimado total
    # I: Self
    # O: int
    def getInputTotal(self):
        total = 0
        for frame in self.refSiblingFrames:
            if frame.validateInput():
                total += frame.getInputTotal(frame.getInput())
        return total

    # F: Getter de valor estimado total
    # I: Self
    # O: int
    def getValueTotal(self):
        total = 0
        for frame in self.refSiblingFrames:
            if frame.validateInput():
                total += frame.getValueTotal(frame.getInput())
        return total

    # F: Actualiza valores del frame
    # I: Self
    # O: N/a
    def updateDisplay(self):
        self.updateLoad()
        self.updateTotal()

    # F: Actualiza carga de dinero
    # I: Self
    # O: N/a
    def updateLoad(self):
        self.countLoad.config(text=self.getInputSum())
        self.valueLoad.config(text=self.getValueSum())

    # F: Actualiza total de dinero
    # I: Self
    # O: N/a
    def updateTotal(self):
        self.countTotal.config(text=self.getInputTotal())
        self.valueTotal.config(text=self.getValueTotal())

################
# main program #
################

