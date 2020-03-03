# Simple Financial Calculator

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

## Problem definition

Calculate the present and future value of a cashflow!

## Instructions

**a)** Open up the `cashflow` project with PyCharm or your favorite IDE. Create the virtualenv and install dependencies. Configure the file structure: 
* `main.py`: create the `Main` object and initialize with the `fire` library. 
* `models.py`: create a `CashFlow` object. 

**b)** Create the cashflow object named `CashFlow` that contains the following: 

**Attributes**
* `amount`: represents an arbitrary monetary value. 
* `t`: represent the position in arbitrary time units. 

**Methods**
* `present_value`: given an `interest_rate`, return the another `CashFlow` at `t=0` where the `amount` attribute is the present value of the current cashflow. 
* `shift`: given `t` and `interest_rate`, return another cashflow located at `t`. 
* `to_dict`: return a dictionary representing the cashflow. 

```python
from models import CashFlow

cf = CashFlow(112.68, 12)

example_1 = cf.present_value(0.01)
print(example_1.to_dict())  # {'amount': 100.0, 't': 0}

example_2 = cf.shift(24, 0.01)
print(example_2.to_dict())  # {'amount': 126.97, 't': 24}

example_3 = cf.shift(6, 0.01)
print(example_3.to_dict())  # {'amount': 106.15, 't': 6}
```

**c)** Add the following commands on the main.py file!

* `future-value --amount 100 --rate 0.01 --t 12` when using the `future-value` assume the `amount` is originally on `t=0`. 
* `present-value --amount 112.68 --rate 0.01 --t 12` when using the `present-value` assume the `amount` is originally in `t=t`. 

## Usage

Once `venv` in active, the usage is fairly simple.

* Get the future value: 

```commandline
$ python main.py future-value --amount 100 --rate 0.01 --t 12
{
    "amount": 112.68,
    "t": 12
}
```

* Get the present value: 

```commandline
python main.py present-value --amount 112.68 --rate 0.01 --t 12
{
    "amount": 100.0,
    "t": 0
}
```
