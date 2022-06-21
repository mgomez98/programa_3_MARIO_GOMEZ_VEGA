##################
#Vehicle.py
#Date of creation: 31/5/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

import time

###########
# classes #
###########

class Vehicle():
    # Atributos
    plate = None      # str
    entryTime = None  # float - segundos desde epoch time.time()
    payTime = None    # float - segundos desde epoch time.time()
    exitTime = None   # float - segundos desde epoch time.time()
    billing = None    # float
    lotID = None      # int

    # Metodo constructor
    def __init__(self, plate: str, entryTime: float, lotID: int):
        self.plate = plate
        self.entryTime = entryTime
        self.lotID = lotID

    # Metodo serializador (json)
    def to_dict(self):
        if isinstance(self, Vehicle):
            dict = {
                "plate": self.plate,
                "entryTime": self.entryTime,
                "payTime": self.payTime,
                "exitTime": self.exitTime,
                "billing": self.billing,
                "lotID": self.lotID
            }
            return dict
        else:
            return None

    # Metodo deserializador
    @classmethod
    def from_dict(cls, dict):
        vehicle = Vehicle(dict["plate"], dict["entryTime"], dict["lotID"])
        vehicle.payTime = dict["payTime"]
        vehicle.exitTime = dict["exitTime"]
        vehicle.billing = dict["billing"]
        return vehicle

#############
#  methods  #
#############

    # F: Obtiene str de plate
    # I: Self - Instancia de Vehicle
    # O: Str de plate
    def getPlate(self) -> str:
        return self.plate
    
    # F: Obtiene entryTime
    # I: Self - Instancia de Vehicle
    # O: entryTime
    def getEntryTime(self) -> float:
        return self.entryTime

    # F: Asigna entryTime
    # I: Self, entryTime - float
    # O: N/a
    def setEntryTime(self, entryTime: float):
        self.entryTime = entryTime

    # F: Obtiene payTime
    # I: Self - Instancia de Vehicle
    # O: payTime
    def getPayTime(self) -> float:
        return self.payTime

    # F: Asigna payTime
    # I: Self, payTime - float
    # O: N/a
    def setPayTime(self, payTime: float):
        self.payTime = payTime

    # F: Obtiene exitTime
    # I: Self - Instancia de Vehicle
    # O: exitTime
    def getExitTime(self) -> float:
        return self.exitTime

    # F: Asigna exitTime
    # I: Self, exitTime - float
    # O: N/a
    def setExitTime(self, exitTime: float):
        self.exitTime = exitTime

    # F: Getter de billing
    # I: Self
    # O: billing
    def getBilling(self):
        return self.billing

    # F: Asigna valor de billing
    # I: Self - Instancia de Vehicle, billing - float
    # O: N/a
    def setBilling(self, billing: float):
        self.billing = billing
    
    # F: Obtiene int de lotID
    # I: Self - Instancia de Vehicle
    # O: Int de lotID
    def getLotID(self) -> int:
        return self.lotID

    # F: Verifica si el vehiculo ha pagado
    # I: Self
    # O: Bool
    def hasPaid(self) -> bool:
        return self.payTime != None

    # F: Obtiene tiempo entre pago y salida
    # I: Self
    # O: Tiempo transcurrido en segundos (float)
    def getTimeDelta(self) -> float:
        return self.getExitTime() - self.getPayTime()

################
# main program #
################

