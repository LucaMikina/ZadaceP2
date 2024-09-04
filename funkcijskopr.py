def pozdrav(string):
    print("Pozdrav", string, "!")

dobrodosao= lambda ime: print("Dobrodošao " + ime + " !")

def obje(string):
    dobrodosao(string)

pozdrav("Jana")
dobrodosao("Marko")
obje("Ante")
    
