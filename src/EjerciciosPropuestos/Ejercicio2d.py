from interpreter import draw
from chessPictures import *

"""
Requirements:
* join()
* negative()
* horizontalRepeat()
"""

componentWhiteFirst = square.join(square.negative()).horizontalRepeat(3);
draw(componentWhiteFirst)