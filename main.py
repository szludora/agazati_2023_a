import szam
import korok
import gombak

szamok = []


x = szam.general()
print(f"I/A:\n\tA generált szám: {x}.\n")
print(f"I/B:\n\t {szam.oszthato(x)}.\n")

korok_lista = korok.beker(szamok)

print(f"IIA, B, C:\n\t{korok.kiir(korok_lista)}\n")
print(f"II/D, E:\n\tElső idős ember korának helye a listában: {korok.konzol_ir(szamok)}\n")
korok.fajl_ir(szamok)

gombak.beolvas()
print(f"III/A,B:\n\tA gombák száma: {gombak.gombak_szama()}.\n")
print(f"III/C:\n\tAz első papsapkagomba neve: {gombak.papsapka()}.\n")
print(f"III/D:\n\tA tinóru gombák száma: {gombak.tinoru()}.")
