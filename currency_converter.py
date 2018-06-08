# Currency Converter #

#imports#

#classes#

class Money:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def converter(self, target_symbol):

        if self.symbol == 'jpy':
            self.amount = (self.amount * .0091)
        if self.symbol == 'eur':
            self.amount = (self.amount * 1.18)
        if self.symbol == 'btc':
            self.symbol = (self.amount * 7633.70)

        self.symbol = target_symbol

        if target_symbol == 'usd':
            return self.amount
        elif target_symbol == 'jpy':
            self.amount = (self.amount * 109.43)
            return self.amount
        elif target_symbol == 'eur':
            self.amount = (self.amount * .85)
            return self.amount
        elif target_symbol == 'btc':
            self.amount = (self.amount * .00013)
            return self.amount

###### variable = classes ########
money = Money('usd', 1)

########### Bosdy #################
print("USD to JPY conversion")
money.converter('jpy')
print(money.amount)
input()

print("USD to EUR conversion")
money.converter('eur')
print(money.amount)
input()

print("USD to BTC conversion")
money.converter('btc')
print(money.amount)
