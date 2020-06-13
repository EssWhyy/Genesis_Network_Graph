#finds characters in verses and writes to workbook

import re
import xlwings
from itertools import combinations

characters = ["Abel", "Abraham", "Adam", "Benjamin", "Cain", "Dinah", "Ephraim", "Esau",
"Eve", "Hagar", "Isaac", "Ishmael", "Jacob", "Joseph", "Judah", "Laban", "Leah", "Levi",
"Lot", "Manasseh", "Melchizedek", "Noah", "Potiphar", "Rachel", "Rebekah", "Reuben",
"Sarah", "Simeon", "Tamar", "God", "LORD"] #Main characters names.

wb = xlwings.Book("bsb.xlsx")
genesis = wb.sheets['Genesis']
edges = wb.sheets['Edges']
nodes = wb.sheets ['Nodes']

counts = {}

for character in characters:
    counts[character] = 0

#writing list of characters for each verse
for i in range(1,1534): 
    cell = 'B' + str(i)
    writecell = 'C' + str(i)
    characterlist=[]
    for character in characters:
        if character in genesis.range(cell).value:
            characterlist.append(character)
            counts[character] += 1

    if len(characterlist) > 0:
        genesis.range(writecell).value = (',').join(characterlist)


#counting total number of characters.
character_counts = counts.items()

index = 1
for item in character_counts:
    namecell = 'B' + str(index)
    countcell = 'D' + str(index)
    index += 1
    nodes.range(namecell).value = item[0]
    nodes.range(countcell).value = item[1]

wb.save()
wb.close()
