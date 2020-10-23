import csv

with open("/home/osboxes/python/toy_data.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=';')
    nbLigne = 0
    for ligne in csvReader:
        if nbLigne != 0 and 2020 - int(ligne[2]) < 24 :
            print(ligne[0])
        nbLigne+=1