import csv

csv_datei = "amazon-order2.csv"

with open(csv_datei, mode="r", encoding="utf-8") as datei:
    amzreader = csv.DictReader(datei)
    for reihe in amzreader:
        print(reihe.get('Order ID',"0"))
