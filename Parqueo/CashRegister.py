##################
#CashRegister.py
#Date of creation: 11/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

from Denomination import Denomination, INPUT, OUTPUT, TOTAL
from Vehicle import Vehicle
from timeUtils import getRawHours

###########
# classes #
###########

class CashRegister():
    # Atributos
    coins = None # list <denominaciones>
    bills = None # list <denominaciones>

    # Metodo constructor
    def __init__(self):
        self.initCoins([0, 0, 0])
        self.initBills([0, 0, 0, 0, 0])

    # Metodo serializador (json)
    def to_dict(self):
        if isinstance(self, CashRegister):
            self.list_to_dict()
            dict = {
                "coins": self.coins,
                "bills": self.bills
            }
            return dict
        else:
            return None

    # Metodo list <denomination> -> list <dictionary>
    def list_to_dict(self):
        for i, coin in enumerate(self.coins):
            self.coins[i] = coin.to_dict()
        for i, bill in enumerate(self.bills):
            self.bills[i] = bill.to_dict()

    # Metodo list <dictionary> -> list <denomination>
    def dict_to_list(self):
        for i, coin in enumerate(self.coins):
            self.coins[i] = Denomination.from_dict(coin)
        for i, bill in enumerate(self.bills):
            self.bills[i] = Denomination.from_dict(bill)

    # Metodo deserializador (json)
    @classmethod
    def from_dict(cls, dict):
        register = CashRegister()
        register.coins = dict["coins"]
        register.bills = dict["bills"]
        register.dict_to_list()
        return register

#############
#  methods  #
#############

    # F: Inicializa lista coins
    # I: values: lista de ints
    # O: N/a
    def initCoins(self, values: list):
        self.coins = []
        for value in values:
            coin = Denomination(value)
            self.coins.append(coin)

    # F: Inicializa lista bills
    # I: values: lista de int
    # O: N/a
    def initBills(self, values: list):
        self.bills = []
        for value in values:
            bill = Denomination(value)
            self.bills.append(bill)

    # F: Getter de coins
    # I: N/a
    # O: Retorna lista de ints
    def getCoins(self) -> list:
        return self.coins

    # F: Getter de bills
    # I: N/a
    # O: Retorna lista de ints
    def getBills(self) -> list:
        return self.bills

    # F: Valida si el cajero esta vacio
    # I: N/a
    # O: Retorna bool True/False
    def isEmpty(self) -> bool:
        for coin in self.coins:
            if coin.getAmountInputs() != 0:
                return False
        for bill in self.bills:
            if bill.getAmountInputs() != 0:
                return False
        return True

    # F: Vacia el cajero
    # I: N/a
    # O: N/a
    def emptyAll(self):
        for coin in self.coins:
            coin.emptyAmount()
        for bill in self.bills:
            bill.emptyAmount()

    # F: Realiza conteo de denominaciones
    # I: Self, lista de denominaciones, type - constante consultada
    # O: conteo - int
    def __countAmount(self, denominations: list, type: int) -> int:
        count = 0
        for denomination in denominations:
            count += denomination.getAmount(type)
        return count

    # F: Realiza conteo de valor de denominaciones
    # I: Self, lista de denominaciones, type - constante consultada
    # O: sumatoria de valores - int
    def __countValue(self, denominations: list, type: int) -> int:
        value = 0
        for denomination in denominations:
            value += denomination.getValueByType(type)
        return value

    # F: Obtiene conteo de monedas
    # I: Self, constante consultada
    # O: Retorna conteo de monedas
    def getCoinsAmount(self, type: int) -> int:
        return self.__countAmount(self.coins, type)

    # F: Obtiene conteo de billetes
    # I: Self, constante consultada
    # O: Retorna conteo de billetes
    def getBillsAmount(self, type: int) -> int:
        return self.__countAmount(self.bills, type)

    # F: Obtiene valor de monedas
    # I: Self, constante consultada
    # O: Retorna valor de monedas
    def getTotalCoinValue(self, type: int) -> int:
        return self.__countValue(self.coins, type)

    # F: Obtiene valor de billetes
    # I: Self, constante consultada
    # O: Retorna valor de billetes
    def getTotalBillValue(self, type: int) -> int:
        return self.__countValue(self.bills, type)

    # F: Calcula cobro tentativo
    # I: self, instancia vehicle, float tiempo cobrado, float costo por hora, float costo minimo
    # O: cobro tentativo
    def calculateBill(self, vehicle: Vehicle, payTime: float, hourlyRate: float, minRate: float) -> int:
        timeDelta = payTime - vehicle.getEntryTime()
        hours = getRawHours(timeDelta)
        if hours < 1:
            return minRate
        return hours * hourlyRate

    # F:
    # I:
    # O:
    def calculatePayment(self, coinInputs: list, billInputs: list) -> int:
        total = 0
        for index, quantity in enumerate(coinInputs):
            total += self.coins[index].calculateTotalValue(quantity)
        for index, quantity in enumerate(billInputs):
            total += self.bills[index].calculateTotalValue(quantity)
        return total

    # F:
    # I:
    # O:
    def calculateChange(self, payment: int) -> tuple:
        coinOutputs = []
        billOutputs = []
        for bill in self.bills[::-1]:
            if bill.getValue() == 0:
                continue
            quantity = int(payment // bill.getValue())
            if quantity <= bill.getAmount(INPUT):
                payment -= bill.calculateTotalValue(quantity)
                billOutputs.insert(0, quantity)

        for coin in self.coins[::-1]:
            if coin.getValue() == 0:
                continue
            quantity = int(payment // coin.getValue())
            if quantity <= coin.getAmount(INPUT):
                payment -= coin.calculateTotalValue(quantity)
                coinOutputs.insert(0, quantity)
        return coinOutputs, billOutputs

    # F:
    # I:
    # O:
    def commitInputs(self, coinInputs: list, billInputs: list):
        for index, quantity in enumerate(coinInputs):
            self.coins[index].increaseAmount(quantity)

        for index, quantity in enumerate(billInputs):
            self.bills[index].increaseAmount(quantity)

    # F:
    # I:
    # O:
    def commitOutputs(self, coinOutputs: list, billOutputs: list):
        for index, quantity in enumerate(coinOutputs):
            self.coins[index].decreaseAmount(quantity)

        for index, quantity in enumerate(billOutputs):
            self.bills[index].decreaseAmount(quantity)

    # F:
    # I:
    # O:
    def isChangePossible(self, change: int):
        return change <= ( self.getTotalCoinValue(TOTAL) + self.getTotalBillValue(TOTAL) )

    # F:
    # I:    vehicleList (Vehiculos que no han pagado)
    #       estimatedTime (float de tiempo a calcular)
    # O:
    def getEstimatedEarnings(self, vehicles: list, estimatedTime: float, hourlyRate: float, minRate: float) -> float:
        total = 0
        for vehicle in vehicles:
            total += self.calculateBill(vehicle, estimatedTime, hourlyRate, minRate)
        return total

################
# main program #
################

