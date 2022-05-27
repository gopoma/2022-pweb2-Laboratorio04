from interpreter import draw
from chessPictures import *
from Ejercicio2d import templateLineWhiteFirst
from Ejercicio2e import templateLineBlackFirst
from Ejercicio2f import battleField

mainEscort = [rock, knight, bishop, queen, king, bishop, knight, rock]

mainEscortWhite = mainEscort[0]
mainEscortBlack = mainEscort[0].negative()
pawnEscortWhite = pawn
pawnEscortBlack = pawn.negative()

for i in range(1, len(mainEscort)):
  mainEscortWhite = mainEscortWhite.join(mainEscort[i])
  mainEscortBlack = mainEscortBlack.join(mainEscort[len(mainEscort) - i - 1].negative().verticalMirror())
  pawnEscortWhite = pawnEscortWhite.join(pawn)
  pawnEscortBlack = pawnEscortBlack.join(pawn.negative())

firstLayer = templateLineBlackFirst.under(mainEscortBlack).rotate().rotate()
lastLayer = templateLineBlackFirst.under(mainEscortWhite)
pawnLayerBlack = templateLineWhiteFirst.under(pawnEscortBlack).rotate().rotate()
pawnLayerWhite = templateLineWhiteFirst.under(pawnEscortWhite)

completedBoard = firstLayer.up(pawnLayerBlack).up(battleField).up(pawnLayerWhite).up(lastLayer)
draw(completedBoard)