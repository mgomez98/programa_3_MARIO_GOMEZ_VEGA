##################
#Parking.py
#Date of creation: 31/5/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

from vehicle import Vehicle

###########
# classes #
###########

class ParkingLot():
    # Atributos
    max_lots = None      # int
    hourly_rate = None   # float
    min_rate = None      # float
    manager_mail = None  # str
    max_minutes = None   # int
    lots = None          # dict (llave: int, valor: Vehicle)

    # Metodo constructor
    def __init__(self):
        self.max_lots = 1
        self.hourly_rate = 0.00
        self.min_rate = 0.00
        self.manager_mail = ""
        self.max_minutes = 1
        self.lots = dict()

#############
#  methods  #
#############

# F: Obtiene int de max_lots
    # I: Self - Instancia de ParkingLot
    # O: Int de max_lots
    def getMaxLots(self) -> int:
        return self.max_lots

    # F: Asigna valor de max_lots
    # I: Self - Instancia de ParkingLot, max_lots - int
    # O: N/a
    def setMaxLots(self, max_lots: int):
        self.max_lots = max_lots

    # F: Obtiene float de hourly_rate
    # I: Self - Instancia de ParkingLot
    # O: Float de hourly_rate
    def getHourlyRate(self) -> float:
        return self.hourly_rate

    # F: Asigna valor de hourly_rate
    # I: Self - Instancia de ParkingLot, hourly_rate - float
    # O: N/a
    def setHourlyRate(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    # F: Obtiene float de min_rate
    # I: Self - Instancia de ParkingLot
    # O: Float de min_rate
    def getMinRate(self) -> float:
        return self.min_rate

    # F: Asigna valor de min_rate
    # I: Self - Instancia de ParkingLot, min_rate - float
    # O: N/a
    def setMinRate(self, min_rate: float):
        self.min_rate = min_rate

    # F: Obtiene str de manager_mail
    # I: Self - Instancia de ParkingLot
    # O: Str de manager_mail
    def getManagerMail(self) -> str:
        return self.manager_mail

    # F: Asigna valor de manager_mail
    # I: Self - Instancia de ParkingLot, manager_mail - str
    # O: N/a
    def setManagerMail(self, manager_mail: str):
        self.manager_mail = manager_mail

    # F: Obtiene int de max_minutes
    # I: Self - Instancia de ParkingLot
    # O: Int de max_minutes
    def getMaxMinutes(self)  -> int:
        return self.max_minutes

    # F: Asigna valor de max_minutes
    # I: Self - Instancia de ParkingLot, max_minutes - int
    # O: N/a
    def setMaxMinutes(self, max_minutes: int):
        self.max_minutes = max_minutes

    # F: Obtiene diccionario de lots
    # I: Self - Instancia de ParkingLot
    # O: Dict de lots
    def getLots(self) -> dict:
        return self.lots

    # F: Verifica si el parqueo se encuentra lleno
    # I: Self - Instancia de ParkingLot
    # O: Retorna el bool relevante
    def isFull(self) -> bool:
        size = len(self.lots)
        if size >= self.max_lots:
            return True
        return False

    # F: Agrega una instancia de Vehicle al parqueo
    # I: Self - Instancia de ParkingLot, Vehicle - Instancia de Vehicle
    # O: N/a
    def addVehicle(self, vehicle: Vehicle):
        lotID = vehicle.getLotID()
        self.lots[lotID] = vehicle

    # F: Encuentra el primer espacio disponible en el parqueo
    # I: Self - Instancia de ParkingLot
    # O: Int de la llave correspondiente al espacio vacio
    def findLot(self) -> int:
        lotID = 1
        while lotID <= self.max_lots:
            if not lotID in self.lots.keys():
                break
            lotID += 1
        return lotID

    # F: Elimina una instancia de Vehicle del parqueo
    # I: Self - Instancia de ParkingLot, Vehicle - Instancia de Vehicle
    # O: N/a
    def removeVehicle(self, vehicle: Vehicle):
        lotID = vehicle.getLotID()
        del self.lots[lotID]

    # F: Encuentra una instancia de Vehicle en el parqueo
    # I: Self - Instancia de ParkingLot, Plate - str
    # O: Instancia de Vehicle buscada
    def findVehicle(self, plate: str) -> Vehicle:
        for key in self.lots.keys():
            vehicle = self.lots[key]
            if plate == vehicle.getPlate():
                return vehicle
        return None

    # F:
    # I:
    # O:
    def getEstimatedEarnings() -> float:
        pass # TO DO: Pasar funcion a cajero

################
# main program #
################

