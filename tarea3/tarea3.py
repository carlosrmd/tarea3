'''
Created on 28/1/2015

Autores: Carlos Martínez - 11-10584
         Christian Teixeira - 11-11016
'''

def marzullo(sourcestable, intervbegin, intervend):
    tuples = []
    for source in sourcestable:
        if (source[1] > intervbegin) and (source[0] < intervend):
            tuples.append([source[0], -1])
            tuples.append([source[1], 1])
    sortedtable = tuplesort(tuples)
    
    best = 0
    cnt = 0
    beststart = 0
    bestend = 0
    for i in range(len(sortedtable)):
            cnt = cnt - sortedtable[i][1]
            if cnt > best:
                best = cnt
                beststart = sortedtable[i][0]
                bestend = sortedtable[i+1][0]
    
    bestinterval = [beststart, bestend, best]
    print("Best interval is [" + str(bestinterval[0]) + "," + str(bestinterval[1]) + "] and the number of reservations is: " + str(bestinterval[2]))
    if bestinterval[2] > 9:
        return False
    elif bestinterval[2] <= 9:
        return True
    
    
def tuplesort(tuples):
    return sorted(tuples, key = getKey)


def getKey(item):
    return item[0]


if __name__ == '__main__':
    reservations = []
    reservations.append([8, 9])
    reservations.append([8, 12])
    reservations.append([10, 12])
    if marzullo(reservations, 9, 10):
    	print("Thank you. Your reservation has been processed successfully.")
    else:
        print("Sorry. There's no parking lot available at this hour.")
    