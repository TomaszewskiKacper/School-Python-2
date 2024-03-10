import numpy as np
import sys
import csv

def get_input():
    if len(sys.argv)>1:  #command line args [1,2,3,4]
        data = [float(x) for x in sys.argv[1].split(",")]   #split into array and convert to float

    elif not sys.stdin.isatty(): #command line args [<file.txt]
        data = [float(x) for x in sys.stdin]    #add to array and convert to float

    else:   #no data provided
        return 0

    return data



data = get_input()  #get data
print("data: ", data)   #print data
print("srednia: ", np.mean(data))       #srednia
print("wariancja: ", np.var(data))      #wariancja
print("odchylenie standardowe: ", np.std(data))     #odchylenie standardowe

