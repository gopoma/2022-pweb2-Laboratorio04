from interpreter import draw
from chessPictures import *
from Ejercicio2f import battleField
from colors import *

squareColors = {
  "white": "_",
  "black": "="
}

def paintBlank(p, color):
  if color not in squareColors.keys():
    return p
  return Picture([p.img[i].replace(" ", squareColors[color]) for i in range(len(p.img))])

mainEscort = [rock, knight, bishop, king, queen, bishop, knight, rock]

mainEscortBlack = paintBlank(mainEscort[0].negative(), "white")
pawnEscortBlack = paintBlank(pawn.negative(), "black")
pawnEscortWhite = paintBlank(pawn, "white")
mainEscortWhite = paintBlank(mainEscort[0], "black")
for i in range(1, len(mainEscort)):
  tmp = mainEscort[i].negative()
  tmp2 = mainEscort[i]
  if i % 2 != 0:
    mainEscortBlack = mainEscortBlack.join(paintBlank(tmp, "black"))
    pawnEscortBlack = pawnEscortBlack.join(paintBlank(pawn.negative(), "white"))
    pawnEscortWhite = pawnEscortWhite.join(paintBlank(pawn, "black"))
    mainEscortWhite = mainEscortWhite.join(paintBlank(tmp2, "white"))
    continue
  mainEscortBlack = mainEscortBlack.join(paintBlank(tmp, "white"))
  pawnEscortBlack = pawnEscortBlack.join(paintBlank(pawn.negative(), "black"))
  pawnEscortWhite = pawnEscortWhite.join(paintBlank(pawn, "white"))
  mainEscortWhite = mainEscortWhite.join(paintBlank(tmp2, "black"))

draw(mainEscortBlack.up(pawnEscortBlack).up(battleField).up(pawnEscortWhite).up(mainEscortWhite))
