# Linear Regression

Create and use a simple linear regression!

Objectives: 
* Implement a linear regression algorithm on python using the linear algebra method. 
* Use your algorithm on the commandline and other python scripts.
* Allow training and saving models!

## Setup

Open this project on PyCharm and do the following:

1. Create and activate a virtualenv
    * **Use PyCharm** or one of the following:
        * `virtualenv --python=python3 venv`
        * `python3 -m virtualenv --python=python3 venv`
        * Note: you might have to use the complete python path.
    * Activate your virtual environment:
        * Mac/Linux: `source venv/bin/activate`
        * Windows: `source venv/Scripts/activate`

1. Install requirements
    * `pip install -r requirements.txt`
    
## Usage

You should be able to use this model on the following scenarios: 
* As a commandline tool. 
* As a python library.

All use cases should be able to `train` or `load` a model to use it. 

You can define how to save your model as a JSON file. Feel free to use the structure that works best for your code. For example: 

```json
{
  "target_column": "...",
  "add_intercept": "...",
  "predictors": [
    ...
  ],
  "weights": [
    ...
  ] 
}
```

You should use the linear algebra definition for multivariate linear regression seen during class. 

Allowed dependencies (`requirements.txt`):
* `numpy`
* `pandas`
* `fire`

### Commandline Tool

**Training** a linear regression:

Your algorithm should be able to take the training data from a csv-file. 

```commandline
$ python main.py train_linear_regression \
    --data-path data/weather.csv  \
    --target-column max_temp \
    --add-intercept intercept \
    --save-path model-example.json
```

Options: 

```text
    --data-path     : Path to the training dataset. 
    --target-column : Name of the target column.
    --add-intercept : Name of the intercept column. 
                      This column is not added if an empty string is used.
                      * Default: ""
    --save-path     : Path used to save the model as json format.
                     * Default: ""
```

**Scoring** a linear regression:  

You algorithm should be able to get the model from a json file and output the predictions to into a csv file. 

```commandline
$ python main.py score_linear_regression \
    --model-path model-example.json \
    --data-path data/weather.csv  \
    --save-output data/out.csv
```

Options: 

```text
    --model-path    : Path with the json-file containing a previously trained model. 
    --data-path     : Path with the data to perform scoring. Empty path will use the training data. 
                     * Default: None
    --prediction    : Column name for prediction. 
                     * Default: estimation
    --save-output   : Save prediction csv-file. Empty strings ignored. 
                     * Default: "" 
```

### Library

Example of how to use this codebase as a library: 

```python
import pandas as pd

from models import LinearRegression

# Read your data 
data = pd.read_csv("data/weather.csv")

# Separate into training/testing 
train = data.sample(frac=0.7)
test = data.drop(train.index)

# Create and train the model
linear_model = LinearRegression(
    data=train, 
    target_column="max_temp", 
    add_intercept="intercept"
    ).train()

# Get predictions!
train_with_predictions = linear_model.predict(train)
test_with_predictions = linear_model.predict(train)

print(test_with_predictions)

# Save model
linear_model.save("model-example.json")
```

You should be able to load your trained model: 

```python
from models import LinearRegression

linear_model = LinearRegression.load("model-example.json")
```

## Grading!

- [ ] Training method is done using the linear algebra formulation seen in class. 
- [ ] You can train and save a linear regression via commandline.
- [ ] You can train and save a linear regression by importing with the python object.
- [ ] You can evaluate a previously saved linear regression via commandline.
- [ ] You can evaluate a previously saved linear regression via the python object.
- [ ] Model is saved using a JSON file.
- [ ] You can get results (evaluation) as a csv-file.

**Note**: If your implementation runs different than the examples on this file, create a `RUN.md` markdown file with the instructions on how to execute your program with the following sections: 
* `Commandline`: as if it were run with `python main.py ...`
* `Python object`: as if it were used by another python program. 

Show how to `train`/`save`/`evaluate`/`load` your model. 
