from csv import reader
import csv

ocjene = {}
studenti = []

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    data=[tuple(line) for line in csv.reader(read_obj)]

print("ucenici koji su polozili: ")
for osoba in data:
    ime, prezime, bodovi, ocjena = osoba
    if int(bodovi) >= 50:
        print(osoba)
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1
    punoime = [ime, prezime]
    studenti.append(punoime)
    
print("Ocjene:\n", ocjene)

print("Po prezimenima")
sortirani= sorted(studenti, key=lambda x: x[1])
brojac = 0
for osoba in sortirani:
    print(sortirani[brojac])
    brojac += 1
