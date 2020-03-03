# Tree Traversal

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

Given a tree-like structure like: 

```text
          3  
        / | \
       1  5 10   
      /  / \  \
     6  1   4  5  

```

Calculate the total sum per level: 

**EX-1**

```text
          3        => 3
        / | \
       1  5 10     => 16
      /  / \  \
     6  1   4  5   => 16
```

```python
from models import Node

Node(value=3, children=[
    Node(value=1, children=[
        Node(value=6, children=[])
    ]),
    Node(value=5, children=[
        Node(value=1, children=[]),
        Node(value=4, children=[])
    ]),
    Node(value=10, children=[
        Node(value=5, children=[])
    ])
])
```

**EX-2** 

```text
          1        => 1
        /   \
       6     7     => 13
      / \    |
    10   4   7     => 21
```

```python
from models import Node

Node(value=1, children=[
    Node(value=6, children=[
        Node(value=10, children=[]),
        Node(value=4, children=[])
    ]),
    Node(value=7, children=[
        Node(value=7, children=[])
    ])
])
```

**EX-3**

```text
         17        => 17
        /   \
       0     1     => 1
     / | \    
    2  3  1        => 6
```

```python
from models import Node

Node(value=17, children=[
    Node(value=0, children=[
        Node(value=2, children=[]),
        Node(value=3, children=[]),
        Node(value=1, children=[])
    ]),
    Node(value=1, children=[])
])
```

## Instructions

**a)** Open up the `tree-traversal` project with PyCharm, create the virutalenv, install dependencies, and create the following scripts (if not exists):

* `main.py`: create the `Main` object, define a `logger` and initialize with the `fire` library.
* `models.py`: create a `Node` class that represents an element on the tree (more on `b`). 
* `utils.py`: use this to store all your utility code (e.g., classes, functions).

**b)** Create a `Node` class containing the following: 

**Attributes**
* `value`: integer representing the node value.
* `children`: list of child nodes.

**Methods** 
* Create as many methods as needed. At least:
    * `load`: build the tree from a json file.
    * `to_dict`: create a dictionary from the tree data. 

**c)** Add the following commands on the `main.py` file! Use the `pretty_print` decorator on them. 
* `show --filename file.json`: prints out the dictionary structure of a tree.
* `sum-levels --filename file.json`: prints out the sum per level of a given tree. 

## Usage

Using the `show` command on example 2 (`ex-2.json`):

```commandline
$ python main.py show --filename ex-2.json
{
    "value": 1,
    "children": [
        {
            "value": 6,
            "children": [
                {
                    "value": 10,
                    "children": []
                },
                {
                    "value": 4,
                    "children": []
                }
            ]
        },
        {
            "value": 7,
            "children": [
                {
                    "value": 7,
                    "children": []
                }
            ]
        }
    ]
}
```

Using the `sum_levels` command on example 1 (`ex-1.json`):

```commandline
python main.py sum_levels --filename ex-1.json
{
    "0": 3,
    "1": 16,
    "2": 16
}
```

Using the `sum_levels` command on example 2 (`ex-2.json`):

```commandline
python main.py sum_levels --filename ex-2.json
{
    "0": 1,
    "1": 13,
    "2": 21
}
```
