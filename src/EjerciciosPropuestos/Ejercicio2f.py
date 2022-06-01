from interpreter import draw
from chessPictures import *

# We would import cWF and cWB from Ejercicio2d and Ejercicio2e
componentWhiteFirst = square.join(square.negative()).horizontalRepeat(3);
componentBlackFirst = square.negative().join(square).horizontalRepeat(3);
componentWhiteBlack = componentWhiteFirst.up(componentBlackFirst)
battleField = componentWhiteBlack.up(componentWhiteBlack)

draw(battleField)