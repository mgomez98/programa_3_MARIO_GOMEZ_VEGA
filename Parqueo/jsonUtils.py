##################
#Funciones json
#Date of creation: 11/6/22
#Author: Mario Gomez Vega
##################

import json
from CashRegister import CashRegister
from ParkingLot import ParkingLot

# F: Guarda contenidos en un archivo
# I: Recibe: Nombre del archivo a guardar, archivo a guardar
# O: N/a
def writeCashRegister(contents):
    binFile=open('cajero.json', 'w')
    json.dump(contents, binFile, default=CashRegister.to_dict)
    binFile.close()
    return

# F: Carga contenidos de un archivo
# I: Recibe nombre del archivo a cargar
# O: Retorna los contenidos del archivo
def loadCashRegister():
    try:
        binFile=open('cajero.json', 'r')
        objDictionary=json.load(binFile)
        binFile.close()
        objData = CashRegister.from_dict(objDictionary)
        return objData
    except FileNotFoundError:
        return CashRegister()

# F: Guarda contenidos en un archivo
# I: Recibe: Nombre del archivo a guardar, archivo a guardar
# O: N/a
def writeParkingLot(contents):
    binFile=open('parqueo.json', 'w')
    json.dump(contents, binFile, default=ParkingLot.to_dict)
    binFile.close()
    return

# F: Carga contenidos de un archivo
# I: Recibe nombre del archivo a cargar
# O: Retorna los contenidos del archivo
def loadParkingLot():
    try:
        binFile=open('parqueo.json', 'r')
        objDictionary=json.load(binFile)
        binFile.close()
        objData = ParkingLot.from_dict(objDictionary)
        return objData
    except FileNotFoundError:
        return ParkingLot()