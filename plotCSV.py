import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
# - [Global params] -

PREDIR = "Pre/"
POSTDIR = "Post/"
CSVFORMATER = ','
SKIPLINES = 2
NROWS = 601
NCOLS = 30
INDEXES = [0, 1, 2, 4, 5,7,8]
DATETIMEFORMAT = '%d/%m/%Y %H:%M:%S'
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
        for i in range(nCols):
            if(i in indexes):
                temp.append(line[i])
        retorno.append(temp)
    return retorno

def processDates(input, index):
    first = True
    for row in input:
        if(first):
            initial = datetime.strptime(row[index],DATETIMEFORMAT)
            first = False
        #This gives elapsed time in minutes
        row[index] = (datetime.strptime(row[index],DATETIMEFORMAT) - initial).total_seconds()/60.0

def list2Array(input):
    retorno = np.zeros(shape = (NROWS, len(INDEXES)))
    for i in range(NROWS):
        retorno[i] = input[i]
    return retorno

def plotInfo(plt, input, index,vo, unit):
    maxes = np.max(input, axis=0)
    avg = np.average(input, axis=0)
    median = np.median(input, axis=0)
    plt.axhline(y = maxes[index], color = 'r', linestyle = '--')
    plt.axhline(y = avg[index], color = 'purple', linestyle = '--')
    #Texto
    plt.text(median[0], maxes[index]-vo, "Max: " + str(round(maxes[index],2)) + unit, color = 'r')
    plt.text(median[0], avg[index]-vo, "AVG: " + str(round(avg[index],2)) + unit, color = 'purple')
    return maxes[index]

def fullPlot(input,name):
    #plt.figure()
    plt.figure(figsize=(10.8,7.2), dpi=100)
    # Core #1 - Carga %
    plt.subplot(321)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Load [%]')
    plt.title('Porcentaje de carga: Core#1')
    plt.plot(input[:,0], input[:,1])
    max = plotInfo(plt, input, 1, 5, " [%]")
    plt.yticks(np.arange(0, max, 10))
    # Core #2 - Carga %
    plt.subplot(322)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Load [%]')
    plt.title('Porcentaje de carga: Core#2')
    plt.plot(input[:,0], input[:,2])
    plotInfo(plt, input, 2, 5, " [%]")
    plt.yticks(np.arange(0, max, 10))

    # Core#1 - Temp
    plt.subplot(323)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Temperatura [°C]')
    plt.title('Temperatura: Core#1')
    plt.plot(input[:,0], input[:,3])
    max = plotInfo(plt, input, 3, 1, " [°C]")
    # Core#2 - Temp
    plt.subplot(324)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Temperatura [°C]')
    plt.title('Temperatura: Core#2')
    plt.plot(input[:,0], input[:,4])
    max = plotInfo(plt, input, 4, 1, " [°C]")

    # Core#1 - Freq
    plt.subplot(325)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Frecuencia [MHz]')
    plt.title('Frecuencia: Core#1')
    plt.plot(input[:,0], input[:,5])
    max = plotInfo(plt, input, 5, 0, " [MHz]")
    # Core#2 - Freq
    # Core#1 - Freq
    plt.subplot(326)
    plt.xlabel('Tiempo [min]')
    plt.ylabel('Frecuencia [MHz]')
    plt.title('Frecuencia: Core#2')
    plt.plot(input[:,0], input[:,6])
    max = plotInfo(plt, input, 6, 0, " [MHz]")
    plt.tight_layout()
    plt.savefig(name,dpi=100)
    #plt.show()

# Baseline
baseReaded = readCSV(PREDIR+"baseline_pre",2,30,INDEXES)
processDates(baseReaded, 0)
baseProcessed = list2Array(baseReaded)
fullPlot(baseProcessed,"pre_Baseline")

# 1

# Pre#1
pre1Readed = readCSV(PREDIR+"Psingle_1",2,30,INDEXES)
processDates(pre1Readed,0)
pre1Processed = list2Array(pre1Readed)
fullPlot(pre1Processed, "pre_single1")


# Post#1
post1Readed = readCSV(POSTDIR+"single_post_1",2,30,INDEXES)
processDates(post1Readed,0)
post1Processed = list2Array(post1Readed)
fullPlot(post1Processed, "post_single1")

# 2

# Pre#2
pre2Readed = readCSV(PREDIR+"Psingle_2",2,30,INDEXES)
processDates(pre2Readed,0)
pre2Processed = list2Array(pre2Readed)
fullPlot(pre2Processed, "pre_single2")


# Post#2
post2Readed = readCSV(POSTDIR+"single_post_2",2,30,INDEXES)
processDates(post2Readed,0)
post2Processed = list2Array(post2Readed)
fullPlot(post2Processed, "post_single2")

# 3

# Pre#3
pre3Readed = readCSV(PREDIR+"Psingle_3",2,30,INDEXES)
processDates(pre3Readed,0)
pre3Processed = list2Array(pre3Readed)
fullPlot(pre3Processed, "pre_single3")


# Post#3
post3Readed = readCSV(POSTDIR+"single_post_3",2,30,INDEXES)
processDates(post3Readed,0)
post3Processed = list2Array(post3Readed)
fullPlot(post3Processed, "post_single3")
