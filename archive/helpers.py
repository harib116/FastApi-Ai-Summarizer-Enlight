import json

def bprint(content, indent=2):
    print(json.dumps(content, indent=indent))

# bprint({"hari": "name", 29:"age"})


class Obj:
    def __init__(self) -> None:
        print("__init__")

    def __call__(self) -> None:
        print("__call__")

