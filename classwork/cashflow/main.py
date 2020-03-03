import logging
import fire

from models import CashFlow
from utils import pretty_print

logger = logging.getLogger(__name__)

class Main(object):

    @pretty_print(logger)
    def future_value(self, amount, rate, t):
        return CashFlow(amount, 0).shift(rate, t).to_dict()

    @pretty_print(logger)
    def present_value(self, amount, rate, t):
        return CashFlow(amount, t).present_value(rate)


if __name__ == "__main__":
    logging.basicConfig()
    fire.Fire(Main)