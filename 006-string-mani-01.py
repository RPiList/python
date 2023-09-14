# Nachfolgend wird eine Datei geöffnet und dann
# Zeilenweise gelesen. Das ist hier NICHT wichtig.
# Uns geht es nur um die For-Schleife am Ende.

dateiname = 'malware.txt'
with open(dateiname, "r", encoding='UTF-8') as datei: # "r" steht für Read-Only Zugriff
    # Datei wird zeilenweise eingelesen
    for zeile in datei:
        ???
