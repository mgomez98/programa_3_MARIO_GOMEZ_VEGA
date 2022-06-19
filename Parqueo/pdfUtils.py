##################
#FPDF.py
#Date of creation: 19/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import fpdf as fp
from timeUtils import getTimeString, getTimeBill, getTimeFloat, getFileTime
from Vehicle import Vehicle

#############
# functions #
#############

# F: Genera factura en formato pdf
# I: Recibe vehiculo a facturar
# O: N/a
def generateLog(vehicle: Vehicle):
    pdf = fp.FPDF('P', 'mm', (90.0, 120.0))
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Factura', 0, 2)
    pdf.set_font('Arial', '', 10)
    pdf.cell(40, 10, f'Placa: {vehicle.getPlate()}', 0, 2)
    pdf.cell(40, 10, f'Hora de entrada: {getTimeString(vehicle.getEntryTime())}', 0, 2)
    pdf.cell(40, 10, f'Hora de salida: {getTimeString(vehicle.getPayTime())}', 0, 2)
    pdf.cell(40, 10, f'Tiempo cobrado: {getTimeBill(vehicle.getPayTime() - vehicle.getEntryTime())}', 0, 2)
    pdf.cell(40, 10, f'Monto: {int(vehicle.getBilling())}')
    filename = f'factura_{getFileTime(vehicle.getPayTime())}.pdf'
    pdf.output(filename, 'F')

################
# main program #
################

