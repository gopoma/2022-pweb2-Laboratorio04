from interpreter import draw
from chessPictures import *

firstLayerBlock = square.join(square.negative())
firstLayerComponent = firstLayerBlock.join(firstLayerBlock).join(firstLayerBlock).join(firstLayerBlock)

secondLayerBlock = square.negative().join(square)
secondLayerComponent = secondLayerBlock.join(secondLayerBlock).join(secondLayerBlock).join(secondLayerBlock)

battleField = firstLayerComponent.up(secondLayerComponent).up(firstLayerComponent).up(secondLayerComponent)

if __name__ == "__main__":
  draw(battleField)