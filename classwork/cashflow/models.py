class CashFlow(object):
    def __init__(self, amount, t=0):
        self.amount = amount
        self.t = t

    def present_value(self, interest_rate):
        return CashFlow(self.amount/(1+interest_rate/100)**(self.t))

    def shift(self, interest_rate, t):
        return CashFlow(self.amount*(1+interest_rate/100)**(t-self.t), (t))

    def to_dict(self):
        return {
            'amount' : self.amount,
            't' : self.t
        }
    #cuando requiero datos del objeto necesito que no sea @staticmethod.
    #Cualquier metodo que no necesite los datos del objeto puede convertirse en @property






