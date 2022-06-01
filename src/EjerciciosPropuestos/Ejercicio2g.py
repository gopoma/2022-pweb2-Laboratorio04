from interpreter import draw
from chessPictures import *

"""
Requirements:
  * join()
  * negative()
  * horizontalRepeat()
  * up()
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
mainEscortBlack = mainEscortWhite.negative()
pawnEscortBlack = pawnEscortWhite.negative()

firstLayer = componentWhiteFirst.under(mainEscortBlack)
pawnLayerBlack = componentBlackFirst.under(pawnEscortBlack)
pawnLayerWhite = componentWhiteFirst.under(pawnEscortWhite)
lastLayer = componentBlackFirst.under(mainEscortWhite)

completedBoard = firstLayer.up(pawnLayerBlack).up(battleField).up(pawnLayerWhite).up(lastLayer)
draw(completedBoard)