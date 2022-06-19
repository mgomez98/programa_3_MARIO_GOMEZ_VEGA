##################
#Title
#Date of creation: 
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import fpdf as fp
from Vehicle import Vehicle

###########
# classes #
###########



#############
#  methods  #
#############



################
# main program #
################
plt = 123456
testlist = [Vehicle('1234', 50.0, 1), Vehicle('5678', 60.0, 2)]

pdf = fp.FPDF()
for car in testlist:
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.cell(40, 10, f'placa: {car.getPlate()}  tiempo: {car.getEntryTime()}    espacio: {car.getLotID()}', 1, 2)
pdf.output('test1.pdf', 'F')