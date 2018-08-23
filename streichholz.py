#!/usr/bin/env python3
# coding: utf-8

# anzahl an Streichhoelzern
from random import randint
streichhölzer = randint(5,25)
print()
print('Die Anzahl der Streichhölzer beträgt',streichhölzer)


#Wiederholung bis die anzahl der Streichhölzer 0 beträgt
while(streichhölzer>0):

    # Nutzer zieht 1-2 Streichhölzer
    print()
    anzahl_nutzer=input('Wie viele Streichhölzer ziehst du? ')
    
    if(anzahl_nutzer.isdigit()):
        number_nutzer = int(anzahl_nutzer)
    else:
        print('Eingabe nicht gültig, gebe die Zahl 1 oder 2 ein.')
        continue
    
    if(number_nutzer<0 or number_nutzer>2):
        print('Eingabe nicht gültig, gebe die Zahl 1 oder 2 ein.')
        continue

    print('Deine Eingabe war:', anzahl_nutzer)

    # abziehen
    streichhölzer= streichhölzer-number_nutzer
    
    if(streichhölzer<=0):
        print('Du hast gewonnen!')
        break
    else:
        print('Die Anzahl der Streichhölzer beträgt',streichhölzer) 

    # Computer zieht 1-2 Streichhölzer
    from random import randint
    anzahl_computer= randint(1,2)
    print()
    print('Die Eingabe des Computers war:',anzahl_computer)
    streichhölzer= streichhölzer-anzahl_computer
    
    if(streichhölzer<=0):
        print('Der Computer hat gewonnen!')
    else:
        print('Die Anzahl der Streichhölzer beträgt',streichhölzer)

