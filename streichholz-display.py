#!/usr/bin/env python3
# coding: utf-8

import math
import time
from random import randint

import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Gebe Hallo, es regnet! aus
#initialisierung vom Bild vom Stif und schriftart
image= Image.new('1', ( LCD.LCDWIDTH,LCD.LCDHEIGHT))
draw= ImageDraw.Draw(image)

draw.rectangle((0,0,84,48), outline=0, fill=1)


font= ImageFont.load_default()
draw.text((8,5), 'Hallo,', font=font)
draw.text((8,25), 'es regnet!', font=font)
disp.image(image)
disp.display()

# --- Streichholzspiel ---
# anzahl an Streichhoelzern
streichhölzer = randint(5,25)

draw.rectangle((0,0,84,48), outline=0, fill=1)
draw.text((8,5), 'Hölzer:', font=font)
draw.text((8,25), str(streichhölzer), font=font)
disp.image(image)
disp.display()

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
        draw.rectangle((0,0,84,48), outline=1, fill=1)
        draw.text((8,22), '    :)', font=font)
        disp.image(image)
        disp.display()
        break
    else:
        draw.rectangle((0,25,84,48), outline=1, fill=1)
        draw.text((8,25), str(streichhölzer), font=font)
        disp.image(image)
        disp.display()

    # Computer zieht 1-2 Streichhölzer
    from random import randint
    anzahl_computer= randint(1,2)
    print()
    print('Die Eingabe des Computers war:',anzahl_computer)
    streichhölzer= streichhölzer-anzahl_computer
    
    if(streichhölzer<=0):
        draw.rectangle((0,0,84,48), outline=1, fill=1)
        draw.text((8,22), '    :(', font=font)
        disp.image(image)
        disp.display()
    else:
        draw.rectangle((0,25,84,48), outline=1, fill=1)
        draw.text((8,25), str(streichhölzer), font=font)
        disp.image(image)
        disp.display()




