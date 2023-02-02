def beker(szamok):

    print("Adj meg öt számot [0,120] intervallumon belül")
    i = 1
    while i < 6:
        x = int(input(f"{i}. szám: "))
        while x > 120 or x < 0:
            x = int(input(f"{i}. szám: "))
        szamok.append(x)
        i += 1
    return szamok


def kiir(korok):

    kiiras = ""
    i = 0
    while i < len(korok) - 1:
        kiiras += str(korok[i]) + " : "
        i += 1
    kiiras += str(korok[i])

    return kiiras


def elso_idos(lista):
    idosebb = -1
    i = 0
    while i < len(lista):
        if lista[i] > 70 and idosebb == -1:
            idosebb = i
        i += 1

    return idosebb


def konzol_ir(szamok):
    x = elso_idos(szamok)
    return x


def fajl_ir(lista):
    fajl = open("oreg.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\n\tElső idős ember korának helye a listában: {elso_idos(lista)}")
    fajl.close()
    