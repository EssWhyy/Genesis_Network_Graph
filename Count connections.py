#totals up character connections within verses

import xlwings
from itertools import combinations #counts number of tiems a pair of characters is mentioned in a  verse.

wb = xlwings.Book("bsb.xlsx")
verses = wb.sheets['Sheet1'] #the rows of namelists are placed on a seperate sheet
edges = wb.sheets['Edges']
j=2
allconnections = {}

for i in range(1,350):
    readcell = 'A' + str(i)
    string = verses.range(readcell).value
    characterlist = string.split(",")
    relationslist = list(combinations(characterlist, 2))
    print(relationslist)
    for i in relationslist:
        if i in allconnections:
            allconnections[i] += 1
        else:
            allconnections[i] = 1

for key, value in allconnections.items():
    sourcecell = 'A' + str(j)
    targetcell = 'B' + str(j)
    weightcell = 'C' + str(j)

    edges.range(sourcecell).value = key[0]
    edges.range(targetcell).value = key[1]
    edges.range(weightcell).value = value

    j += 1
