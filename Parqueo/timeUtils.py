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

# F: Obtiene str de tiempo
# I: segundos en formato float
# O: str de tiempo
def getTimeBill(timeFloat: float) -> str:
    return f"{getHours(timeFloat)}h    {getMinutes(timeFloat)}m    {getDays(timeFloat)}d"

# F: Obtiene str de tiempo sobre el limite
# I: timeFloat - segundos en formato float
# O: Str de tiempo
def getTimeTaken(timeFloat: float) -> str:
    return f"{getRawMinutes(timeFloat)} minutos"

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

# F: Obtiene dias
# I: segundos como float
# O: int de dias
def getDays(timeFloat: float) -> int:
    return int(timeFloat // 86400)

# F: Obtiene horas
# I: segundos como float
# O: int de horas
def getHours(timeFloat: float) -> int:
    return int(( timeFloat % 86400 ) // 3600)

# F: Obtiene minutos
# I: segundos como float
# O: int de minutos
def getMinutes(timeFloat: float) -> int:
    return int(( ( timeFloat % 86400 ) % 3600 ) // 60)

# F: Obtiene total de tiempo como minutos
# I: segundos como float
# O: int de minutos
def getRawMinutes(timeFloat: float) -> int:
    return int(timeFloat // 60)