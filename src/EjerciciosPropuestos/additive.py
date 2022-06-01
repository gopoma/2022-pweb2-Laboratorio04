from interpreter import draw
from chessPictures import *

"""
Requirements:
  * join()
  * negative()
  * horizontalRepeat()
  * up()
  * horizontalMirror()
  * rotate() [Optional]
  * under()
"""

# We would import cWF and cWB from Ejercicio2d and Ejercicio2e,
# also battleField from Ejercicio2f
componentWhiteFirst = square.join(square.negative()).horizontalRepeat(3)
componentBlackFirst = square.negative().join(square).horizontalRepeat(3)
componentWhiteBlack = componentWhiteFirst.up(componentBlackFirst)
battleField = componentWhiteBlack.up(componentWhiteBlack)

mainEscortWhite = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
pawnEscortWhite = pawn.horizontalRepeat(7)
mainEscortBlack = mainEscortWhite.negative().horizontalMirror()
pawnEscortBlack = pawnEscortWhite.negative().horizontalMirror()
# mainEscortBlack = mainEscortWhite.negative().rotate().rotate()
# pawnEscortBlack = pawnEscortWhite.negative().rotate().rotate()

firstLayer = componentWhiteFirst.under(mainEscortBlack)
secondLayer = componentBlackFirst.under(pawnEscortBlack)
seventhLayer = componentWhiteFirst.under(pawnEscortWhite)
lastLayer = componentBlackFirst.under(mainEscortWhite)

additiveBoard = firstLayer.up(secondLayer).up(battleField).up(seventhLayer).up(lastLayer)
draw(additiveBoard)