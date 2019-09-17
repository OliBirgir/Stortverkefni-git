#1,3             2,3     3,3
#1,2             2,2 |    3,2
#1,1(byrjun)     |2,1|    3,1(sigur)

"""gera veggi i kringum. spilari getur ekki farið útfyrir. þá prentast út "Not a valid direction!"""
"""prenta út valid directions. You can Travel:"""
"""ef spilari fer N frá 1.1 á hann að fara á 1,2 o.s.frv."""
"""þegar spilari fer á 3,1 prentast út "Victory!" og leikurinn hættir"""

#búa til def move fyrir hverja hreyfingu
#búa til breytu sem að heitir position sem segir forritinu hvar við erum.
#hvert sem að það hreyfist uppfærist síðan positionið
#veggir!
#þurfum input sem að verður move. 
#while (spilarinn er staddur á 1,1. prentast út you can travel north)
"""def 1.1(movement):
    print("you can travel: (N)orth)
    if movement ="N":
        return North1,1
    else:
        print("Not a valid direction!")
        x =failure
        return x


if def1.1(movement) = North1,1:
    def1,2(movement)




def1.1
def1.2
def1.3
def2.1
def2.2
def2.3
def3.1
def3.2
def3.3

    
"""



def oneone (mayPrint):
    if mayPrint:
        print("You can travel (N)orth")
    movement = input ("Direction: ")
    if movement == "N" or movement == "n":
        onetwo(True)
    else:
        print("Not a valid direction!")
        oneone(False)

def onetwo (mayPrint):
    if mayPrint:
        print("You can travel (N)orth or (E)ast or (S)outh")
    movement = input ("Direction: ")
    if movement == "N" or movement == "n":
        onethree(True)
    elif movement == "E" or movement == "e":
        twotwo(True)
    elif movement == "S" or movement == "s":
        oneone(True)
    else:
        print("Not a valid direction!")
        onetwo(False)

def onethree(mayPrint):
    if mayPrint:
        print("You can travel (E)ast or (S)outh")
    movement = input ("Direction: ")
    if movement == "E" or movement == "e":
        twothree(True)
    elif movement =="S" or movement == "s":
        onetwo(True)
    else:
        print("Not a valid direction!")
        onethree(False)
def twoone(mayPrint):
    if mayPrint:
        print("You can travel (N)orth")
    movement = input ("Direction: ")
    if movement =="N" or movement == "n":
        twotwo(True)
    else:
        print("Not a valid direction!")
        twoone(False)
def twotwo(mayPrint):
    if mayPrint:
        print ("You can travel (S)outh or (W)est")
    movement = input ("Direction: ")
    if movement == "S" or movement == "s":
        twoone(True)
    elif movement == "W" or movement == "w":
        onetwo(True)
    else:
        print("Not a valid direction!")
        twotwo(False)
def twothree(mayPrint):
    if mayPrint:
        print("You can travel (E)ast or (W)est")
    movement = input ("Direction: ")
    if movement == "W" or movement == "w":
        onethree(True)
    elif movement == "E" or movement == "e":
        threethree(True)
    else:
        print("Not a valid direction!")
        twothree(False)
def threeone(mayPrint):
    print("Victory!")
def threetwo(mayPrint):
    if mayPrint:
        print("You can tavel (N)orth or (S)outh")
    movement = input ("Direction: ")
    if movement == "N" or movement == "n":
        threethree(True)
    elif movement == "S" or movement == "s":
        threeone(True)
    else:
        print("Not a valid direction!")
        threetwo(False)
def threethree(mayPrint):
    if mayPrint:
        print("You can travel (S)outh or (W)est")
    movement = input("Direction: ")
    if movement == "S" or movement == "s":
        threetwo(True)
    elif movement == "W" or movement == "w":
        twothree(True)
    else:
        print("Not a valid direction!")
        threethree(False)


oneone(True)
