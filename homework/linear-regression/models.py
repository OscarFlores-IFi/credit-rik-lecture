import json
import jax.numpy as np
import pandas as pd


class LinearRegression:

    def __init__(self, data=None, target_column="", add_intercept="", weights=None):

        self.data = data
        self.target_column = target_column
        self.add_intercept = add_intercept
        self.weights = weights

    def train(self):

        if self.add_intercept:
            self.data[self.add_intercept] = np.ones(len(self.data))
        y = self.data[self.target_column]
        x = self.data.drop([self.target_column], axis=1)
        w = np.linalg.pinv(((x.T).dot(x)).values).dot(x.T).dot(y)
        return LinearRegression(self.data, self.target_column, self.add_intercept, w)

    def predict(self, data_predict):
        x = data_predict.drop([self.target_column], axis=1)
        predict = x.dot(self.weights)
        return predict

    def save(self, name):
        if self.add_intercept:
            data = {
                'target_column': self.target_column,
                'add_intercept': self.weights[-1].tolist(),
                'predictors': self.data.columns[:-1].tolist(),
                'weights': self.weights[:-1].tolist()
            }
        else:
            data = {
                'target_column': self.target_column,
                'add_intercept': 0,
                'predictors': [i for i in self.data.columns if i != self.target_column],
                'weights': self.weights.tolist()
            }
        print(data)
        with open(name, 'w') as file:
            json.dump(data, file)

    def load(self, name):
        with open(name, 'r') as file:
            model = json.loads(file.read())

        return model


def train(data_path, target_column, add_intercept='', save_path=''):
    """
    Debug:
    data_path = 'data/weather.csv' or 'data/weight-height.csv'
    target_column = 'max_temp' or 'weight'
    add_intercept = 'intercept'
    save_path = 'model-example.json'
    """
    data = pd.read_csv(data_path)
    if add_intercept:
        data[add_intercept] = np.ones(len(data))
    y = data[target_column].values
    x = data.drop([target_column], axis=1).values
    w = np.linalg.pinv(((x.T).dot(x))).dot(x.T).dot(y)  # calculo de pesos algebraicamente.

    if add_intercept:
        data = {
            'target_column': target_column,
            'add_intercept': w[-1].tolist(),
            'predictors': [i for i in data.columns if i != target_column],
            'weights': w[:-1].tolist()
        }
    else:
        data = {
            'target_column': target_column,
            'add_intercept': 0,
            'predictors': [i for i in data.columns if i != target_column],
            'weights': [i for i in w]
        }

    if save_path:
        with open(save_path, 'w') as file:
            json.dump(data, file)

    return data


def score(model_path, data_path=None, prediction='estimation', save_output=''):
    """
    Debug:
    model_path = 'model-example.json'
    data_path = 'data/weather.csv' or 'data/weight-height.csv'
    prediction = 'estimation'
    save_output = 'data/out.csv'
    """

    with open(model_path, "r") as file:
        model = json.loads(file.read())

    data = pd.read_csv(data_path)
    x = data.drop([model['target_column']], axis=1)
    y_hat = x.dot(np.array(model['weights']))

    if prediction:
        data[prediction] = y_hat

    if save_output:
        data.to_csv(save_output)

    return data
