from models import *

data_path = 'data/weather.csv'
target_column = 'max_temp'
train_linear_regression(data_path,target_column,add_intercept='intercept', save_path='model-example.json')

model_path = 'model-example.json'
score_linear_regression(model_path,
                        data_path = 'data/weather.csv',
                        prediction = 'estimation',
                        save_output = 'data/out.csv')


