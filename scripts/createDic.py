#should create a Dic with all species data, where the species begins and ends
from Bio import SeqIO
import time
import json

path = "/Users/hannahmuelbaier/Desktop/Bachelorarbeit"
allProteins = open("/Users/hannahmuelbaier/Desktop/Bachelorarbeit/oma-seqs.fa", "r")
newFileSpecies = open("/Users/hannahmuelbaier/Desktop/Bachelorarbeit/oma-seqs-dic.fa", "w")
omaGroups = open("/Users/hannahmuelbaier/Desktop/Bachelorarbeit/oma-groups.txt", "r")
newFileOmaGroup = open("/Users/hannahmuelbaier/Desktop/Bachelorarbeit/oma-groups-tmp.txt", "w")
def createDicSpecies(proteins, file):
    start = time.time()
    sequenceDic = {}
    code = str(proteins.readline()[2:7])
    #print(code)
    startline = 0
    lineNr = 0

    for i in proteins:
        lineNr += 1
        if code != i[2:7] and i[0] == ">":
            #print(i[2:7])
            endline = lineNr - 1
            #print(code)
            sequenceDic[code] = (startline,endline)
            code = i[2:7]
            startline = lineNr

    sequenceDic[code] = (startline,lineNr)
    json.dump(sequenceDic, file)
    ende = time.time()
    print('{:5.3f}s'.format(ende - start), end='  ')


def createDicOmaGroup(omaGroups, file):
    start = time.time()

    print("test")

    groupDic = {}

    for i in omaGroups:
        if i[0] != "#":

            line = i.split("\t")
            speciesSet = set()
            groupId = line[0]

            for j in range(2, len(line)):
                species = str(line[j])[0:5]
                speciesSet.add(species)


            groupDic[groupId] = tuple(speciesSet)

    #json.dump(groupDic, file)

    for key in groupDic:
        speciesStr = str(groupDic[key]).replace("(", "")
        speciesStr = speciesStr.replace(")", "")
        speciesStr = speciesStr.replace("'", "")
        speciesStr = speciesStr.replace(" ", "")
        file.write(key + "\t" + speciesStr + "\n")

    ende = time.time()
    print('{:5.3f}s'.format(ende - start), end='  ')



createDicSpecies(allProteins, newFileSpecies)
createDicOmaGroup(omaGroups, newFileOmaGroup)
newFileSpecies.close()



