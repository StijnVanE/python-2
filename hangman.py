import random
from woorden import woorden_lijst
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("type \"?\" in om een woord te raden")
def speel():
    woord = random.choice(woorden_lijst)
    print("het woord heeft " + str(len(woord)) + " letters.")
    geraden =  False
    geradenletters = ""
    fout = 0
    geradenwoord = ""
    while not geraden and fout < 5:
        letter = input("raad een letter: ").lower()
        if letter == "?":
            geradenwoord = input("raad een woord: ").lower()
            if geradenwoord == woord:
                geraden = True
                print("je hebt het woord goed geraden, het woord is: "+str(woord))
            else:
                fout += 1
                print("het woord dat je geraden hebt is niet goed")
        elif letter in geradenletters or letter not in alfabet or len(letter) != 1:
            print("het letter dat je geraden hebt heb je al gebruikt of is geen letter")
        elif letter not in woord:
            fout += 1
            print("de letter: "+str(letter) + " is niet in het woord je hebt nu " + str(fout) + " foute letters geraden")
            geradenletters += letter+" "
            print("de letters die je tot nu toe geraden hebt: " + str(geradenletters))
        else:
            print("je hebt een letter goed geraden")
            geradenletters += letter+" "
            print("de letters die je tot nu toe geraden hebt: " + str(geradenletters))
        geraden1 = ""
        for x in woord:
            if x in geradenletters:
                geraden1 += x
            else:          
                geraden1 += "_"
        if not geraden:
            print(str(geraden1))
        if "_" not in geraden1:
            geraden = True
            print("je hebt het woord goed geraden, het woord is: "+str(woord))
        elif fout == 5:
            print("je hebt het woord niet geraden, het woord is: "+str(woord))
        
    nogeenkeerspelen()

    
def nogeenkeerspelen():
    nogeenkeer = input("wil je nog een keer spelen? ")
    if nogeenkeer == "ja":
        speel()
        
speel()
