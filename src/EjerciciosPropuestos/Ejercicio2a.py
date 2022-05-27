from interpreter import draw
from chessPictures import *

"""
Requirements:
* join()
* negative()
* up()
"""

component = knight.join(knight.negative())
draw(component.up(component.negative()))