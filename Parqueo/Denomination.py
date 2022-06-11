##################
#Denomination.py
#Date of creation: 11/6/22
#Author: Mario Gomez Vega
##################

###########
# modules #
###########



###########
# classes #
###########

class Denomination():
    # Atributos
    value = None          # int
    amountInputs = None   # int
    amountOutputs = None  # int

    # Metodo constructor
    def __init__(self, value: int) -> None:
        self.value = value
        self.amountInputs = 0
        self.amountOutputs = 0

#############
#  methods  #
#############

    # F: Getter de value
    # I: N/a
    # O: Retorna int
    def getValue(self) -> int:
        return self.value

    # F: Getter de cantidad total de dinero
    # I: N/a
    # O: Retorna int
    def getTotalAmount(self) -> int:
        return (self.amountInputs - self.amountOutputs)

    # F: Getter de valor total de dinero
    # I: N/a
    # O: Retorna int
    def getTotalValue(self) -> int:
        return self.calculateTotalValue(self.getTotalAmount())

    # F: Getter de amountInputs
    # I: N/a
    # O: Retorna int
    def getAmountInputs(self) -> int:
        return self.amountInputs

    # F: Getter de valor de ingresos
    # I: N/a
    # O: Retorna int
    def getInputValue(self) -> int:
        return self.calculateTotalValue(self.amountInputs)

    # F: Getter de amountOutputs
    # I: N/a
    # O: Retorna int
    def getAmountOutputs(self) -> int:
        return self.amountOutputs

    # F: Getter de valor de retiros
    # I: N/a
    # O: Retorna int
    def getOutputValue(self) -> int:
        return self.calculateTotalValue(self.amountOutputs)

    # F: Incrementa amountInputs
    # I: quantity: cantidad incrementada
    # O: N/a
    def increaseAmount(self, quantity: int):
        self.amountInputs += quantity

    # F: Incrementa amountOutputs
    # I: quantity: cantidad incrementada
    # O: N/a
    def decreaseAmount(self, quantity: int):
        self.amountOutputs += quantity

    # F: Setter de valores predeterminados
    # I: N/a
    # O: N/a
    def emptyAmount(self):
        self.amountInputs = 0
        self.amountOutputs = 0

    # F: Calcula valor total
    # I: amount: cantidad de denominacion
    # O: Retorna int
    def calculateTotalValue(self, amount: int) -> int:
        return (amount * self.value)

################
# main program #
################

