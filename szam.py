import random


def general():
    vel = int(random.random()*51) + 1

    return vel


def oszthato(vel):

    kiiras = ""

    if vel % 3 == 0 and vel % 5 == 0:
        kiiras += "A szám öttel és hárommal is osztható!"
    elif vel % 5 == 0:
        kiiras += "A szám öttel osztható!"
    elif vel % 3 == 0:
        kiiras += "A szám hárommal osztható!"
    else:
        kiiras += "A szám nem osztható hárommal és öttel sem!"

    return kiiras
