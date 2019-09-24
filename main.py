

import csv
import numpy as np
import io

from ReaderPlus import ReaderPlus
from RoughSet import RoughSet

def incAll(p):
    return list(map((lambda l: [i + 1 for i in l]), p))

with io.open("test.csv", "r", encoding='utf_8_sig') as fp:
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
        if columnName == "*":
            flag ^= True
        else:
            if flag:
                methods.append(columnName)
            else:
                persons.append(columnName)

    for lineName in preData[:, 0]:
        if lineName == "*":
            flag ^= True
        else:
            if flag:
                features.append(lineName)
            else:
                ways.append(lineName)

    personsLen = len(persons)
    featuresLen = len(features)
    methodsLen = len(methods)
    waysLen = len(ways)


    featuresMethods = np.array(preData[1:1 + len(features), 1:1 + len(methods)])
    featuresPersons = np.array(preData[1:1 + len(features), 2 + len(methods):2 + len(methods) + len(persons)])
    waysMethods = np.array(preData[2 + len(features): 2 + len(features) + len(ways), 1:1 + len(methods)])
    print("\npersons: " + str(persons))
    print("\nfeatures: " + str(features))
    print("\nmethods: " + str(methods))
    print("\npersons: " + str(persons))
    print("\nfeaturesMethods: \n" + str(featuresMethods))
    print("\nfeaturesPersons: \n" + str(featuresPersons))
    print("\nwaysMethods: \n" + str(waysMethods))

    for i in range(len(ways)):
        for j in range(len(methods)):
            waysMethods[i][j] = "1" if int(waysMethods[i][j]) <= 2 else "2"

    # situations = []
    # featuresSituations = np.empty((8, 25), dtype=object)
    # for methodNum in range(len(methods)):
    #     for personNum in range(len(persons)):
    #         situations.append(methods[methodNum] + " - " + persons[personNum])
    #         for featureNum in range(len(features)):
    #             print(str(featuresMethods[featureNum][methodNum]) + str(featuresPersons[featureNum][personNum]))
    #             featuresSituations[featureNum][methodNum * len(persons) + personNum] = str(featuresMethods[featureNum][methodNum]) + str(featuresPersons[featureNum][personNum])
    # print(situations)
    # print(featuresSituations)

    situations = []
    situationsMethods = np.empty((8, 5), dtype=object)
    num = 0
    for i in range(0, 2):
        for j in range(2, 4):
            for k in range(4, 6):
                situations.append(ways[i] + "/" + ways[j] + "/" + ways[k])
                for methodNum in range(len(methods)):
                    situationsMethods[num][methodNum] = waysMethods[i][methodNum] + waysMethods[j][methodNum] + waysMethods[k][methodNum]
                num += 1

    print(situations)
    print(situationsMethods)


    attributes = []
    featuresAttributes = np.empty((len(features), len(situations) + len(persons)), dtype=object)
    methodNum = 4
    for situationNum in range(len(situations)):
        attributes.append(str(methods[methodNum]) + " - " + str(situations[situationNum]))
        for featureNum in range(len(features)):
            featuresAttributes[featureNum][situationNum] = featuresMethods[featureNum][methodNum] + situationsMethods[situationNum][methodNum]
    for personNum in range(len(persons)):
        attributes.append(persons[personNum])
        for featureNum in range(len(features)):
            featuresAttributes[featureNum][len(situations) + personNum] = featuresPersons[featureNum][personNum]
    print(attributes)
    print(featuresAttributes)



    rs = RoughSet(featuresAttributes)
    #
    # print([i for i in range(8)])
    # imp = rs.importance([i for i in range(len(situations), len(situations) + len(persons))], [i for i in range(0, len(situations))])
    # for i in range(8):
    #     print(str(i) + " - " + attributes[i] + ': ' + str(imp[i]))

    for i in range(8):
        imp = rs.importance([i], [i for i in range(len(situations), len(situations) + len(persons))])
        # for i in range(8):
        #     print(str(i) + " - " + attributes[i] + ': ' + str(imp[i]))

    # objects = []
    # objectsFeatures = np.empty((40, 8), dtype="int")
    # objectNum = 0
    # for methodNum in range(len(methods)):
    #     for situationNum in range(len(situations)):
    #         objects.append(methods[methodNum] + " - " + situations[situationNum])
    #         for featureNum in range(len(features)):
    #             objectsFeatures[objectNum][featureNum] = (situationsMethods[situationNum][methodNum]) * 4 + featuresMethods[featureNum][methodNum] - 1
    #         objectNum += 1
    # print(objectsFeatures)
    #
    # roughSetObjectsFeatures = RoughSet(objectsFeatures)
    #
    # roughSetObjectsFeatures.importance([i for i in range(8)], [i for i in range(8)])



    # inp = ReaderPlus("test.txt")
    #
    # arr = [
    #     [1, 2, 0, 1, 1],
    #     [1, 2, 0, 1, 1],
    #     [2, 0, 0, 1, 0],
    #     [0, 0, 1, 2, 1],
    #     [2, 1, 0, 2, 0],
    #     [0, 0, 1, 2, 2],
    #     [2, 0, 0, 1, 0],
    #     [0, 1, 2, 2, 1],
    #     [2, 1, 0, 2, 2],
    #     [2, 0, 0, 1, 0]
    # ]

    # print("\n" + str(np.array(arr)))
    # roughSet = RoughSet(arr)
    #
    # print()
    #
    # print("U/IND(a0): " + str(roughSet.div([0])))
    # print("U/IND(a0, a1): " + str(roughSet.div([0, 1])))
    # print("U/IND(a0, a1, a2): " + str(roughSet.div([0, 1, 2])))
    # print("U/IND(a0, a1, a2, a3): " + str(roughSet.div([0, 1, 2, 3])))
    # print("U/IND(a0, a1, a2, a3, a4): " + str(roughSet.div([0, 1, 2, 3, 4])))
    #
    # print("**************************************")
    # roughSet.importance([0, 1, 2], [3, 4])
    #
    # print("**************************************")
    # roughSet.importance([3, 4], [0, 1, 2])
    #
    # print("**************************************")
    # roughSet.importance([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])