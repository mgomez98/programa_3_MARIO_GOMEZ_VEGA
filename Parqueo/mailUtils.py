##################
#TimeUtils.py
#Date of creation: 21/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#############
# functions #
#############

# F:
# I:
# O:
def nullPayment(plate: str, receiver: str):
    content = f'''Cajero sin fondos suficientes para dar cambio al vehiculo placa {plate}.
    Pago anulado; por favor presentarse a cargar cajero'''
    
    sender = 'parqueo2022029053@gmail.com'
    senderPass = '2022029053'
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Pago anulado'

    message.attach(MIMEText(content))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, senderPass)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    #session.quit()
    session.close()

# F:
# I:
# O:
def lowBalance(lowMoneyList: list, receiver: str):
    content = 'Cajero esta bajo en fondos; quedan menos de 5 de las siguientes denominaciones:'
    body = '{}, '
    for denomination in lowMoneyList:
        content = content + body.format(denomination)
    
    sender = 'parqueo2022029053@gmail.com'
    senderPass = '2022029053'
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Cajero tiene pocos fondos'

    message.attach(MIMEText(content))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, senderPass)
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()

################
# main program #
################

nullPayment('123456', 'mario.gomez.vega@gmail.com')