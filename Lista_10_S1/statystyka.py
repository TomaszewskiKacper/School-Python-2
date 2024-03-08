import numpy as np
import sys


def get_input():
    if len(sys.argv) > 1 and sys.argv[1].endswith(".csv"):  #csv file
        #wczytaj
    elif len(sys.argv) > 1:
        data = sys.argv[1]

    return data

print(get_input())
print("test")
