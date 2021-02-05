import matplotlib.pyplot as plt

# - [Global params] -

PREDIR = "Pre/"
POSTDIR = "Post/"
CSVFORMATER = ','
SKIPLINES = 2

# - [Funciones] -

def readCSV(name, nSkip, nCols, indexes):
    file = open(name + ".csv")
    retorno = []
    # Skip lines
    for j in range(nSkip):
        next(file)
    for line in file:
        temp = []
        line = line.strip().split(CSVFORMATER)
        retorno.append(line)
    print(len(retorno))
readCSV(PREDIR+"baseline_pre",2,0,0)
