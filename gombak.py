from Gomba import Gomba

gomba_lista = []


def beolvas():
    fajl = open("gombak_jav.txt", "r", encoding="utf-8")
    fajl.readline()
    tartalom = fajl.readlines()
    fajl.close()
    peldanyositas(tartalom)


def peldanyositas(tart):
    i = 0
    while i < len(tart):
        sor = tart[i].strip().split("@")
        gomba = Gomba(sor[0], sor[1], sor[2])
        gomba_lista.append(gomba)
        i += 1


def gombak_szama():

    return len(gomba_lista)


def papsapka():
    i = 0
    while i < len(gomba_lista) and gomba_lista[i].nemzettseg != "papsapkagombák ":
        i += 1
    return gomba_lista[i].nev


def tinoru():
    db = 1
    i = 0
    while i < len(gomba_lista):
        if gomba_lista[i].nemzettseg == "tinóru":
            db += 1
        i += 1
    return db
