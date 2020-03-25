import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class amortization(object):

    def __init__(self, amount, interest, n):
        self.amount = amount
        self.interest = interest
        self.n = n

    @property
    def annuity(self):
        return self.amount*self.interest/(1-(1+self.interest)**(-self.n))

    def get_table(self, show = 0, save:str = None):
        table = np.zeros((self.n, 5))
        table[0,1] = self.amount
        B = self.amount
        for t in range(1,self.n):
            I = B*self.interest
            P = self.annuity-I
            B -= P
            table[t,:] = [t, B, P, I, self.annuity]
        table_df = pd.DataFrame(table,columns=['t','B','P','I','A']).set_index('t')
        if show:
            print(table_df.head(show))

        if save:
            table_df.to_csv(save)

        return table_df

    def plot(self, show = False, save:str = None):
        P = self.get_table().P
        I = self.get_table().I

        if show:
            plt.bar(np.arange(self.n), P, )
            plt.bar(np.arange(self.n), I, bottom=P)
            plt.show()

        if save:
            plt.bar(np.arange(self.n), P, )
            plt.bar(np.arange(self.n), I, bottom=P)
            plt.savefig(save)



























