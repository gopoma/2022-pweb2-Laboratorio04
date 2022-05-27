from interpreter import draw
from chessPictures import *

component = square.negative().join(square)
templateLineBlackFirst = component.join(component).join(component).join(component)

if __name__ == "__main__":
  draw(templateLineBlackFirst)