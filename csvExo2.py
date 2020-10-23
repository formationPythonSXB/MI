import csv,operator

with open("/home/osboxes/python/toy_data.csv") as csvFic:
    
    csvContenu = csv.reader(csvFic, delimiter=';')
    colonnes = next(csvContenu)
    
    csvTrie = sorted(csvContenu,key=operator.itemgetter(2))
    
    with open("tri.csv", "w") as f:
          ficWriter = csv.writer(f, delimiter=';')
          ficWriter.writerow( (colonnes[0],colonnes[2]) )
          for ligne in csvTrie :
              ficWriter.writerow( (ligne[0],ligne[2]) )