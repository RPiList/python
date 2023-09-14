# Nachfolgend wird eine Datei geöffnet und dann
# Zeilenweise gelesen. Das ist hier NICHT wichtig.
# Uns geht es nur um die For-Schleife am Ende.

dateiname = 'malware.txt'

counter = 0
counterDE = 0
counterFR = 0
counterCOM = 0
with open(dateiname, "r", encoding='UTF-8') as datei: # "r" steht für Read-Only Zugriff
    # Datei wird zeilenweise eingelesen
    for zeile in datei:
        counter = counter + 1
        domain = zeile.strip()
        if domain.endswith('.fr'):
            counterFR += 1 
        elif domain.endswith('.de'):
            counterDE = counterDE + 1
        elif domain.endswith('.com'):
            counterCOM = counterCOM + 1

print(str(counter))
print("FR-Domains: " + str(counterFR))
print("DE-Domains: " + str(counterDE))
print("COM-Domains: " + str(counterCOM))


