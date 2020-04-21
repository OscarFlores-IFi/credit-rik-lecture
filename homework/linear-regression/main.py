import logging
import fire
import os

from models import *

logger = logging.getLogger(__name__)

class Main(object):

    def train_linear_regression(data_path,target_column,add_intercept='intercept', save_path='model-example.json'):
        return train(data_path,target_column,add_intercept, save_path)

    def score_linear_regression(model_path,
                            data_path = 'data/weather.csv',
                            prediction = 'estimation',
                            save_output = 'data/out.csv'):
        return score(model_path, data_path, prediction, save_output)

if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("APP_LOG_LEVEL",default="INFO"))
    fire.Fire(Main)
