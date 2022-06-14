##################
#TimeUtils.py
#Date of creation: 13/6/22
#Author: Mario Gomez Vega
##################

import time
import datetime

# F: Obtiene float de segundos desde epoch
# I: N/a
# O: float de segundos
def getTimeFloat() -> float:
    return time.time()

# F: Obtiene str de tiempo
# I: timeFloat - segundos en formato float
# O: Str de tiempo
def getTimeString(timeFloat: float) -> str:
    timeStruct = time.localtime(timeFloat)
    return time.strftime("%H:%M - %d/%m/%Y", timeStruct)

# F: Obtiene str de tiempo sobre el limite
# I: timeFloat - segundos en formato float
# O: Str de tiempo
def getTimeTaken(timeFloat: float) -> str:
    timeStruct = time.localtime(timeFloat)
    return time.strftime("%M minutos", timeStruct)

# F: Valida conversion de fecha str a float de segundos
# I: str de fecha
# O: float de segundos, None si la fecha es invalida
def validateDateString(date: str) -> float:
    stringList = date.split('/')
    if len(stringList) != 3:
        return None
    if not stringList[0].isnumeric():
        return None
    if not stringList[1].isnumeric():
        return None
    if not stringList[2].isnumeric():
        return None

    try:
        date = datetime.date(int(stringList[2]), int(stringList[1]), int(stringList[0]))
        date = datetime.date.timetuple(date)
        date = time.mktime(date)
        return date
    except ValueError:
        return None