def parNep(n):
    for broj in range(n):
        if broj % 2==0:
            yield "parni:" + str(broj)
        else:
            yield "neparni:" + str(broj)

my_iter=iter(parNep(19))
while True:
    try:
        element=next(my_iter)
        print(element)
    except StopIteration:
        break
    
