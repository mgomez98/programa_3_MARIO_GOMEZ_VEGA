##################
#CashRegister.py
#Date of creation: 11/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########

from Denomination import Denomination

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

    # F:
    # I:
    # O:
    def __countAmount(self, denominations: list, type: int) -> int:
        count = 0
        for denomination in denominations:
            count += self.__getAmount(denomination, type)
        return count

    # F:
    # I:
    # O:
    def __getAmount(self, denomination: Denomination, type: int) -> int:
        if type == 0: # cantidad de inputs
            return denomination.getAmountInputs()
        elif type == 1: # cantidad de outputs
            return denomination.getAmountOutputs()
        elif type == 2: # cantidad total
            return denomination.getTotalAmount()

    # F:
    # I:
    # O:
    def __countValue(self, denominations: list, type: int) -> int:
        value = 0
        for denomination in denominations:
            value += self.__getValue(denomination, type)
        return value

    # F:
    # I:
    # O:
    def __getValue(self, denomination: Denomination, type: int) -> int:
        if type == 0: # valor de inputs
            return denomination.getInputValue()
        elif type == 1: # valor de outputs
            return denomination.getOutputValue()
        elif type == 2: # valor total
            return denomination.getTotalValue()

    # F:
    # I:
    # O:
    def getCoinsAmount(self, type: int) -> int:
        return self.__countAmount(self.coins, type)

    # F:
    # I:
    # O:
    def getBillsAmount(self, type: int) -> int:
        return self.__countAmount(self.bills, type)

    # F:
    # I:
    # O:
    def getTotalCoinValue(self, type: int) -> int:
        return self.__countValue(self.coins, type)

    # F:
    # I:
    # O:
    def getTotalBillValue(self, type: int) -> int:
        return self.__countValue(self.bills, type)

################
# main program #
################
