#! /usr/bin/env python
import sys
from os import system



def list_packages():
    system("pip freeze")


def create_model_pkl(model="bert_summarizer"):
    from app.models.package_creator import create_pkl
    create_pkl(model)


def execute(code):
    print(f"Executing: {code}")
    try:
        eval(code)()
    except Exception as e:
        print(e)
    print("Done")


if __name__ == "__main__":
    execute(sys.argv[1])

