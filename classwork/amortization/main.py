
import logging
import fire

from models import amortization

logger = logging.getLogger(__name__)


class Main(object):

    @staticmethod
    def annuity(amount, interest, n):
        return amortization(amount, interest, n).annuity

    @staticmethod
    def table(amount, interest, n, show:int = 0, save: str = None):
        return amortization(amount, interest, n).get_table(show = show, save = save)

    @staticmethod
    def plot(amount, interest, n, show = False, save: str = None):
        return amortization(amount, interest, n).plot(show = show, save = save)



if __name__ == "__main__":
    logging.basicConfig()
    fire.Fire(Main)






