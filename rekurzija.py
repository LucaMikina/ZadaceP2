def obratno(n):
    if n == "":
        return n
    print(n)
    return obratno(n[1:]) + n[0]

print(obratno("jabuka"))
