from interpreter import draw
from chessPictures import *

component = square.join(square.negative())
templateLineWhiteFirst = component.join(component).join(component).join(component)

if __name__ == "__main__":
  draw(templateLineWhiteFirst)