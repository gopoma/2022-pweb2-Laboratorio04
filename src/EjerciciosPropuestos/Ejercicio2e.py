from interpreter import draw
from chessPictures import *

"""
Requirements:
  * negative()
  * join()
  * horizontalRepeat()
  ~With Python Modules~
  * verticalMirror() [Optional]
  * rotate() [Optional]
"""

componentBlackFirst = square.negative().join(square).horizontalRepeat(3)
draw(componentBlackFirst)