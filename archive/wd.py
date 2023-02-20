import os, sys
from pathlib import Path


# Using sys
# os.chdir(sys.path[0])

# Using path
file = Path(__file__)
parent = file.parent
os.chdir(parent)
# os.chdir(Path(__file__).parent)
print(os.getcwd())
