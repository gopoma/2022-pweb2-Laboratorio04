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
  mainEscortBlack = mainEscortBlack.join(mainEscort[i].negative())
  pawnEscortWhite = pawnEscortWhite.join(pawn)
  pawnEscortBlack = pawnEscortBlack.join(pawn.negative())

firstLayer = templateLineWhiteFirst.under(mainEscortBlack)
lastLayer = templateLineBlackFirst.under(mainEscortWhite)
pawnLayerBlack = templateLineBlackFirst.under(pawnEscortBlack)
pawnLayerWhite = templateLineWhiteFirst.under(pawnEscortWhite)

completedBoard = firstLayer.up(pawnLayerBlack).up(battleField).up(pawnLayerWhite).up(lastLayer)
draw(completedBoard)