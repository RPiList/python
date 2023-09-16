dateiname = 'malware.txt'

counter = 0
MySet = set()
MyListe = []

with open(dateiname, "r", encoding='UTF-8') as datei: # "r" steht für Read-Only Zugriff
    # Datei wird zeilenweise eingelesen
    for zeile in datei:
        counter = counter + 1
        MyListe.append(zeile.strip())

for eintrag in MyListe:
    tlddot = eintrag.rfind('.')
    MySet.add(eintrag[tlddot:])

counter = 0
for seteintrag in MySet:
    for listeneintrag in MyListe:
        if str(listeneintrag).endswith(seteintrag):
            counter = counter + 1
    print(str(seteintrag) + ": " + str(counter))
    counter = 0
    
print("TLDs insg.: " + str(len(MySet)))
print("Domains insg.: " + str(len(MyListe)))

