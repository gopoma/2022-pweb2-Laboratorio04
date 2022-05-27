from interpreter import draw
from chessPictures import *

draw(square.negative().under(queen.under(king)).horizontalMirror().horizontalRepeat(4).rotate())