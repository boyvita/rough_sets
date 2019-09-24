# Algorithm that calculate importance of attribute in rough set builded on equivalent relation
# https://yadi.sk/i/4KdO6MfEDEQBqQ

import numpy as np

class RoughSet:
    def __init__(self, arr):
        self.arr = arr
        self.universum = [i for i in range(0, len(arr))]
        self.attributes = [i for i in range(0, len(arr[0]))]

    # D = {a1, a2}
    # U/Div(D)
    # разбить строчки на группы так, чтобы в каждой группе элементы из множества были равны поэлементно
    def div(self, attribute_group):
        groups = []
        for lineNum in range(0, len(self.arr)):
            for group in groups:
                for attributeNum in attribute_group:
                    if self.arr[lineNum][attributeNum] != self.arr[group[0]][attributeNum]:
                        break
                else:
                    group.append(lineNum)
                    break
            else:
                groups.append([lineNum])
        return groups

    def pos(self, what, by):
        divWhat = self.div(what)
        divBy = self.div(by)
        result = []
        for group in divWhat:
            if group in divBy:
                result.extend(group)
        return result

    def gamma(self, what, by):
        return len(self.pos(what, by)) / len(self.universum)


    def importance(self, subset, by):
        res = [0] * len(self.arr[0])
        divBy = self.div(by)
        print("by: " + str(by))
        print("divBy: " + str(divBy))

        divSubset = self.div(subset)
        print("subset: " + str(subset))
        print("divSubset: " + str(divSubset))

        print("POS_Subset(By): " + str(self.pos(by, subset)))
        print("gamma_Subset(By) = " + str(self.gamma(by, subset)))
        print()
        for i in subset:
            newSubset = subset.copy()
            newSubset.remove(i)
            print("delete item a" + str(i))
            nameOfNewSubset = ("(Subset-a" + str(i) + ")")
            print(nameOfNewSubset + ": " + str(newSubset))
            print("div" + nameOfNewSubset + ": " + str(self.div(newSubset)))
            print("pos_" + nameOfNewSubset + "(By) = " + str(self.pos(by, newSubset)))
            print("gamma_" + nameOfNewSubset + "(By) = " + str(self.gamma(by, newSubset)))
            print("gamma_(Subset)(By) - gamma_" + nameOfNewSubset + "(By) = " + str(self.gamma(by, subset) - self.gamma(by, newSubset)))
            res[i] = self.gamma(by, subset) - self.gamma(by, newSubset)
            print()
        print()
        return res

