'''
Created on 28/1/2015

Autores: Carlos Martínez - 11-10584
         Christian Teixeira - 11-11016
'''

def marzullo(sourcestable):
    tuples = []
    for source in sourcestable:
        tuples.append([source[0], -1])
        tuples.append([source[1], 1])
    sortedtable = tuplesort(tuples)
    best = 0
    cnt = 0
    for i in range(len(sortedtable)):
        cnt = cnt - sortedtable[i][1]
        if cnt > best:
            best = cnt
            beststart = sortedtable[i][0]
            bestend = sortedtable[i+1][0]
    occupies = 0
    for source in sourcestable:
        if source[0] > beststart or source[1]:
            pass
        pass
    
def tuplesort(tuples):
    return sorted(tuples, key = getKey)

def getKey(item):
    return item[0]

if __name__ == '__main__':
    reservations = []
    reservations.append([8, 12])
    reservations.append([11,13])
    reservations.append([14, 15])
    bestinterval = marzullo(reservations)
    print("Best interval is [" + str(bestinterval[0]) + "," + str(bestinterval[1]) + "]")
    