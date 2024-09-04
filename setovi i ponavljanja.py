import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 
         'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 
             'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

lista=[]

for ime in imena:
    for i in range(15):
        radnik={
           "ime": random.choice(imena),
           "prezime": random.choice(prezimena),
           "satnica": float(random.randint(4, 6))
        }
    lista.append(radnik)
print(lista)
lista2=[]
brojac=0

for radnik in lista:
    radnik["tjedni_sati"]=random.randint(20, 31)
    isplata=radnik["satnica"]*radnik["tjedni_sati"]
    radnik["isplata"]=int(isplata)
    ntorka=radnik["ime"], radnik["prezime"], radnik["isplata"]
    lista2.append(ntorka)
    brojac+=isplata
    prosjecna_isplata=round(brojac/len(lista), 2)

print(lista2)
print("Prosjecna isplata iznosi:", prosjecna_isplata)

for ntorka in lista2:
    if ntorka[2]> prosjecna_isplata:
        print("Radnik", ntorka[0], "ima vecu prosjecnu placu od", ntorka[2])
        


    
