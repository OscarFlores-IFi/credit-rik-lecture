import pandas as pd
import numpy as np
import json

def train_linear_regression(data_path, target_column, add_intercept = '', save_path = ''):
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
    y = data[target_column]
    x = data.drop([target_column], axis=1)
    w = np.linalg.pinv(((x.T).dot(x)).values).dot(x.T).dot(y) #calculo de pesos algebraicamente.

    if add_intercept:
        data = {
            'target_column' : target_column,
            'add_intercept' : w[-1],
            'predictors' : [i for i in x.columns[:-1]],
            'weights' : [i for i in w[:-1]]
            }
    else:
        data = {
            'target_column' : target_column,
            'add_intercept' : 0,
            'predictors' : [i for i in x.columns],
            'weights' : [i for i in w]
            }
    print(data)
    if save_path:
        with open(save_path, 'w') as file:
            json.dump(data, file)

    return data

def score_linear_regression(model_path, data_path = None, prediction = 'estimation', save_output = ''):
    """
    Debug:
    model_path = 'model-example.json'
    data_path = 'data/weather.csv' or 'data/weight-height.csv'
    target_column = 'max_temp' or 'weight'
    prediction = 'estimation'
    save_output = 'data/out.csv'
    """

    with open(model_path, "r") as file:
        model = json.loads(file.read())

    data = pd.read_csv(data_path)
    x = data.drop([model['target_column']],axis=1)
    y_hat = x.dot(np.array(model['weights']))
    print(data)

    if prediction:
        data[prediction] = y_hat

    if save_output:
        data.to_csv(save_output)

    pass



