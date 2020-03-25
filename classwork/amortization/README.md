# Amortization

## Setup 

Open this project on PyCharm and do the following:

1. Create and activate the virtualenv
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

Given the following values:

* `amount`: represents a loan's present value.
* `interest`: represents an interest rate.
* `n`: represents the number of periods.

Create an amortization table and a visualization of the results.

## Instructions

**a)** Open up the `amortization` project with PyCharm, create the virutalenv, install dependencies, and create the following scripts (if not exists):

* `main.py`: create the `Main` object and initialize with the `fire` library.
* `models.py`: create an `Amortization` class.

**b)** Create an `Amortization` class containing the following: 

**Attributes**
* `amount`: represents a loan's present value.
* `interest`: represents an interest rate (float).
* `n`: represents the number of periods.

**Methods**
* `def annuity(self)`: return the annuity value (use the `@propery` decorator to use this method as an attribute).
* `def get_table(self)`: return a pandas DataFrame with the following columns:
    * `t`: Time period.
    * `B`: Outstanding balance.
    * `P`: Principal payment.
    * `I`: Interest payment.
    * `A`: Annuity (constant payment).
* `def get_plot(self, show_figure: bool = False, save: str = "")`: Plots the principal/interest as a stacked bar plot. Show the plot if `show_figure` is true and save as an image if `save` contains a filename.

Example:

```python
from models import Amortization

amortization = Amortization(amount=18000, interest=0.0283, n=6)

# Get the annuity
a = amortization.annuity 

# Get the amortization table
df = amortization.get_table()

# Show or save the plot
amortization.get_plot(show_figure=True)
amortization.get_plot(save="example.png")

```

**c)** Add the following commands on the `main.py` file!
* `annuity --amount 18000 --interest 0.0283 --n 6`
* `table --amount 18000 --interest 0.0283 --n 6 --show 10 --save example.csv`
    * `show` is an integer with default value as 0 that represents the number of rows to print.
    * `save` is a string representing a filename. Ignore if string is empty (default).
* `plot --amount 18000 --interest 0.0283 --n 6 --show --save example.png`
    * `show` is a boolean to determine if `plt.show()` should be called. 
    * `save` is a string representing a filename. Ignore if string is empty (default). 

## Usage

Calculate the annuity:


```commandline
$ python main.py annuity --amount 18000 --interest 0.0283 --n 6
3304.06
```

Amortization table:

```commandline
$ python main.py table --amount 18000 --interest 0.0283 --n 6 --show 3 --save example.csv
   t         B        P      I        A
0  0 18,000.00      nan    nan      nan
1  1 15,205.34 2,794.66 509.40 3,304.06
2  2 12,331.60 2,873.75 430.31 3,304.06
```
* Should be a file named `example.csv` with the amortization table. 

Amortization plot:

```commandline
$ python main.py plot --amount 18000 --interest 0.0283 --n 6 --show --save example.png
```
* Should show the plot.
* Should be a png file named `example.png` with the plot.

## Exercise

Create and save the monthly amortization table for the following loan: 
* Amount: $371,000.00
* Interest rate: 18% annual
* Periods: 20 years
* Filename: `amortization-table-1.csv`

Create and save the monthly amortization table for the following loan: 
* Amount: $275,320.00
* Interest rate: 25% annual
* Periods: 5 years
* Filename: `amortization-table-2.csv`
