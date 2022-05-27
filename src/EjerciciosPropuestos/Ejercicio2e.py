from interpreter import draw
from chessPictures import *

component = square.negative().join(square)
draw(component.join(component).join(component).join(component))