import random
imena = [
    "Vedran", "Andrea", "Ana", "Marta", "Martina", "Iva", "Mirko", "Jakov", "Marko", "Mihaela",
    "Petar", "David", "Ivan", "Ivan", "Ana", "Dinko", "Petar", "Sanja", "Nikola", "Vinko", "Mihael",
    "Zdravko", "Patrik", "Kristijan", "Marin", "Kristijan", "Petar", "Mateo", "Bože", "Ivan-Kajo",
    "Matej", "Karlo", "Ana", "Lucija", "Bože", "Emanuel", "Ante-Roko", "Blaž", "Marijanela",
    "Leonarda", "Antonio", "Ana-Maria", "Petra", "Leo", "Mario", "Marijana", "Jelena", "Stjepan",
    "Dario", "Matej"]

rjecnik={}
ocjene={}

for ime in imena:
        rjecnik[ime]=random.randint(1, 5)
print(rjecnik)

brojac=0
for student in rjecnik:
    ocjena=rjecnik[student]
    if ocjena in ocjene:
        ocjene[ocjena]+=1
    else:
        ocjene[ocjena]=1
    if ocjena>1:
        brojac+=1

print(ocjene)
print("Postotak prolaznosti:", int(brojac/len(imena)*100))
