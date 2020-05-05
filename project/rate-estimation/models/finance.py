from typing import Callable, List, Optional

import jax.numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount, rate, n):
        pass

    def get_table(self):
        pass

    def get_enriched_table(self, prob_of_default: float, loss_given_default: float) -> pd.DataFrame:
        pass

    def expected_irr(self, prob_of_default: float, loss_given_default: float) -> float:
        pass
