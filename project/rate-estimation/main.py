import fire
import logging

from settings import EXPECTED_RATE_LOG_LEVEL
from models.drive import (
    ConfigTable,
    RateValue,
    RequestValue,
    ResultTable
)
from models.finance import Amortization
from utils import setup, search

import pandas as pd

logger = logging.getLogger(__name__)

"""###############################################
a = Amortization(amount=18000, rate=0.3015, n=6)
simple_df = a.get_table()
print(simple_df)
enriched_df = a.get_enriched_table(prob_of_default=0.20, loss_given_default=0.50)
print(enriched_df)
expected_irr = a.expected_irr(prob_of_default=0.20, loss_given_default=0.50)
print(expected_irr)
###############################################
irr_minimal = search(amount=18000, n=6, prob_of_default=0.20, loss_given_default=0.50, desired_rate=0)
print(irr_minimal)
###############################################"""

class Main:

    @staticmethod
    def setup():
        setup()

    @staticmethod
    def loan_request_local(loan_amount : float, loan_marr : float, loan_terms : int,
                           probability_of_default : float, loss_given_default : float,
                           client_min_rate : float, client_max_rate : float, search_samples : int,
                           save : str = '', show = False):
        rate = search(loan_amount, loan_terms, probability_of_default, loss_given_default, desired_rate=loan_marr, sample_size=search_samples)
        df = Amortization(loan_amount, rate, loan_terms).get_enriched_table(probability_of_default, loss_given_default)
        annuity = df['Annuity'][loan_terms]

        if (client_min_rate<rate<client_max_rate) and (loan_marr<rate):
            print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Accepted'
                            .format(loan_amount, loan_terms, annuity, rate*100))
        else:
            print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Rejected'
                  .format(loan_amount, loan_terms, annuity, rate * 100))

        if save[-4:] == '.csv':
            df.to_csv(save)

        if show:
            print(df)


if __name__ == "__main__":
    logging.basicConfig(level=EXPECTED_RATE_LOG_LEVEL)
    pd.options.display.float_format = '{:,.2f}'.format
    fire.Fire(Main)
