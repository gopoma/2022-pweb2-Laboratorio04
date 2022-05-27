from interpreter import draw
from chessPictures import *

component = square.join(square.negative())
draw(component.join(component).join(component).join(component))