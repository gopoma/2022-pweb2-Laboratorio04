from interpreter import draw
from chessPictures import *

"""
Requirements:
* join()
* negative()
* up()
* verticalMirror()
"""

component = knight.join(knight.negative())
draw(component.up(component.verticalMirror()))