

import csv
import numpy as np
import io

from ReaderPlus import ReaderPlus
from RoughSet import RoughSet

def incAll(p):
    return list(map((lambda l: [i + 1 for i in l]), p))

with io.open("test2.csv", "r", encoding='utf_8_sig') as fp:
    reader = csv.reader(fp, delimiter=';', quotechar='"', lineterminator='\n')
    preData = []
    for row in reader:
        if row[0] != "":
           preData.append(row)
    preData = np.array(preData)

    # Персонал - Person
    # Характеристика - Feature
    # Метод/способ обучения - Method
    # Подход организации - Way

    persons = []
    features = []
    methods = []
    ways = []


    flag = False
    for columnName in preData[0, :]:
        if columnName != "" or columnName != "*":
            features.append(columnName)

    for lineName in preData[:, 0]:
        if lineName != "" or lineName != "*":
            methods.append(lineName)


    methodsFeatures = np.array(preData[1:6, 1:9])
    print("\nfeatures: " + str(features))
    print("\nmethods: " + str(methods))
    print("\nmethodsFeatures: \n" + str(methodsFeatures))

    rs = RoughSet(methodsFeatures)
    ans = []
    for i in range(1, 1 << 8):
        group = []
        for j in range(0, 8):
            if (i & 1 << j) != 0:
                group.append(j)
        ans.append([rs.div(group), group])
    ans.sort(key=lambda d: (max([len(g) for g in d[0]]) * 8 + len(d[1])), reverse=True)

    for d in ans:
        print(str([i + 1 for i in d[1]]), end="")
        print(": " + str([[j + 1 for j in i] for i in d[0]]), end="")
        for g in d[0]:
            if len(g) == max([len(g) for g in d[0]]):
                print(" group" + str([i + 1 for i in g]), end=":")
                avg = 0
                for j in range(len(d[1])):
                    print(rs.arr[g[0]][d[1][j]], end="")
                    avg += float(rs.arr[g[0]][d[1][j]]) / len(d[1])
                print(" avg=" + "{0:.2f}".format(avg), end="; ")
        print()