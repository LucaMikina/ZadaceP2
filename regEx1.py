import re

unos = input("Unesite string: ")
reg = r'^L.*[0-5].* .*M$'

if re.match(reg, unos):
    print("Ispravan unos")

else:
    print("Neispravan unos")
