import re


reg1 = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba'
reg2 = r'^[a-zA-Z]+\.[a-zA-Z]+@sum\.ba'

email=input("Unesite mail: ")
eduId=input("Unesite  eduId: ")


if re.match(reg1, email):
    print("Ispravan unos!")
else:
    print("Neispravan unos!")

if re.match(reg2, eduId):
    print("Ispravan unos!")
else:
    print("Neispravan unos!")
