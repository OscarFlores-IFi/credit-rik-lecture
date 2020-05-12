from typing import Callable, List, Optional

# import jax.numpy as np
import pandas as pd
import numpy as np

class Amortization:

    def __init__(self, amount, rate, n):
        self.amount = amount
        self.rate = rate
        self.n = n

    def get_table(self):
        annuity = self.amount * self.rate / (1 - (1 + self.rate) ** (-self.n))
        table = np.zeros((self.n+1, 5))
        table[0, 1] = self.amount
        B = self.amount
        for t in range(1, self.n+1):
            I = B * self.rate
            P = annuity - I
            B -= P
            table[t, :] = [t, B, P, I, annuity]
        table_df = pd.DataFrame(table, columns=['time', 'Balance', 'Payment', 'Interest', 'Annuity']).set_index('time')

        return table_df

    def get_enriched_table(self, prob_of_default: float, loss_given_default: float) -> pd.DataFrame:
        def IRR(cashflows):
            # Get polynomial roots
            res = np.roots(cashflows[::-1])
            # Filter out imaginary component.
            mask = (res.imag == 0) & (res.real > 0)
            if not mask.any:
                return np.nan
            res = res[mask].real
            # Return the solution closest to zero.
            rate = 1 / res - 1
            return rate[np.argmin(np.abs(rate))]

        annuity = self.amount * self.rate / (1 - (1 + self.rate) ** (-self.n))
        table = np.zeros((self.n+1, 7))
        table[0, 1] = self.amount
        B = self.amount
        for t in range(0, self.n+1):
            I = 0
            P = 0
            irr = 0
            if t > 0:
                I = B * self.rate
                P = annuity - I
                B -= P
                irr = IRR([-self.amount] + [annuity for _ in range(t)])
            print(B,t)
            EL = B * loss_given_default * prob_of_default
            table[t, :] = [t, B, P, I, annuity, irr, EL]
        table_df = pd.DataFrame(table, columns=['time', 'Balance', 'Payment', 'Interest', 'Annuity', 'IRR', 'Expected Loss']).set_index('time')

        return table_df

    def expected_irr(self, prob_of_default: float, loss_given_default: float) -> float:
        df = Amortization.get_enriched_table(self, prob_of_default, loss_given_default)
        irr = df['IRR']
        return np.sum([irr[i]*prob_of_default*(1-prob_of_default)**i for i in range(len(irr))])


a = Amortization(amount = 18000, rate = 0.01, n = 6)
simple_df = a.get_table()
enriched_df = a.get_enriched_table(prob_of_default=0.20, loss_given_default=0.50)
expected_irr = a.expected_irr(prob_of_default=0.20, loss_given_default=0.50)

print(expected_irr)