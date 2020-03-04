import json

class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children



    @staticmethod
    def load(filename):
        def from_dict(**kwargs):
            return Node(
                value=kwargs.get("value", []),
                children=[
                    from_dict(**k)
                    for k in kwargs.get("children", [])
                ]
            )

        with open(filename, "r") as file:
            data = json.loads(file.read())
        return from_dict(**data)


    def to_dict(self):
        return {
            "value" : self.value,
            "children" : [Node.to_dict(child) for child in self.children ]
        }
