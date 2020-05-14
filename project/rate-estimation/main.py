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


class Main:

    @staticmethod
    def setup():
        setup()

    @staticmethod
    def loan_request_local(loan_amount: float, loan_marr: float, loan_terms: int,
                           probability_of_default: float, loss_given_default: float,
                           client_min_rate : float, client_max_rate : float, search_samples : int,
                           save: str = '', show=False):
        rate = search(loan_amount, loan_terms, probability_of_default, loss_given_default, desired_rate=loan_marr)
        df = Amortization(loan_amount, rate, loan_terms).get_enriched_table(probability_of_default, loss_given_default)
        annuity = df['Annuity'][loan_terms]

        if (client_min_rate < rate < client_max_rate) and (loan_marr < rate):
            print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Accepted'
                            .format(loan_amount, loan_terms, annuity, rate*100))
        else:
            print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Rejected'
                  .format(loan_amount, loan_terms, annuity, rate * 100))

        if save[-4:] == '.csv':
            df.to_csv(save)

        if show:
            print(df)

    @staticmethod
    def loan_request_cloud(sheet_id: str, save="", show=False):
        table = ConfigTable(sheet_id)
        rate = search(table.loan_amount, table.loan_terms, table.probability_of_default, table.loss_given_default, desired_rate=table.loan_marr)
        df = Amortization(table.loan_amount, rate, table.loan_terms).get_enriched_table(table.probability_of_default, table.loss_given_default)
        annuity = df['Annuity'][table.loan_terms]

        RateValue(sheet_id).update(rate)

        if (table.client_min_rate < rate < table.client_max_rate) and (table.loan_marr < rate):
            RequestValue(sheet_id).update("Accepted")
        else:
            RequestValue(sheet_id).update("Rejected")

        ResultTable(sheet_id).update(df.values.tolist())

        if save:
            df.to_csv(save)

        if show:
            if (table.client_min_rate < rate < table.client_max_rate) and (table.loan_marr < rate):
                print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Accepted'
                      .format(table.loan_amount, table.loan_terms, annuity, rate * 100))
            else:
                print('Loan request for {} due in {} terms of {} of fix payments at an interest rate of {}% : Rejected'
                      .format(table.loan_amount, table.loan_terms, annuity, rate * 100))
            print(df)


if __name__ == "__main__":
    logging.basicConfig(level=EXPECTED_RATE_LOG_LEVEL)
    pd.options.display.float_format = '{:,.2f}'.format
    fire.Fire(Main)
