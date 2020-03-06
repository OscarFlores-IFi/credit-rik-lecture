# Flatten Json

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

Return the flat version of a "nested" json (dictionary). 

**EX-1**

This is a nested dictionary (i.e., a dictionary that potentially contains more dictionaries): 

```json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    }
}
```

Flat version: 

```json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6
}
```

**EX-2**

Assume that the dictionary can contain an arbitrary number of nested levels. 

```json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    },
    "f": {
        "g": 7,
        "h": {
            "i": {
                "j": 8
            }
        }
    }
}
```

Flatten version: 

```json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6,
    "f.g": 7,
    "f.h.i.j": 8
}
```
**EX-3**

If the dictionary contains a list with values, the flat version should use the "index" as a key: 

```json
{
    "a": 1,
    "b": 2,
    "c": [
        3,
        4,
        5
    ]
}
```

Flatten version: 

```json
{
    "a": 1,
    "b": 2,
    "c.0": 3,
    "c.1": 4,
    "c.2": 5
}
```

**EX-4**

Note that a list can contain more dictionaries and/or more lists. Everything should be flatten out in the final result. 

```json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": {
                "f": 4,
                "g": 5
            }
        }
    ]
}
```

Flatten version:

```json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.f": 4,
    "b.1.e.g": 5
}
```

## Instructions

**a)** Open up the project with PyCharm or your favorite IDE. Setup your virtualenv, install dependencies, and create the following scripts: 

* `main.py`:  create the `Main` object, define a logger and initialize with the fire library.
* `utils.py`: use this to store all your utility code.

**b)** Create a function on `utils` named `flatten_dict` with the following characteristics: 

* Receives a dictionary and returns the flat version of that dictionary. 
* The implementation is recursive. 

You can create as many other functions/classes as needed.

Hint: the `isinstance` functions returns a boolean indicating if an object is an instance of a type (e.g., `isinstance(obj, dict)`, `isinstance(obj, list)`).

**c)** Add the following commands on the `main.py` file! Use the `pretty_print` decorator on them.

* `show --filename file.json`: prints out the json file.
* `flatten --filename file.json`: prints out the flat version of the json file. 

## Usage

Show command on example 5:

```commandline
$ python main.py show --filename ex-5.json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": [
                4,
                5,
                {
                    "f": {
                        "g": 6
                    }
                }
            ]
        }
    ]
}
```

Flatten command on example 5: 

```commandline
$ python main.py flatten --filename ex-5.json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.0": 4,
    "b.1.e.1": 5,
    "b.1.e.2.f.g": 6
}
```
