from interpreter import draw
from chessPictures import *

firstLayerBlock = square.join(square.negative())
firstLayerComponent = firstLayerBlock.join(firstLayerBlock).join(firstLayerBlock).join(firstLayerBlock)

secondLayerBlock = square.negative().join(square)
secondLayerComponent = secondLayerBlock.join(secondLayerBlock).join(secondLayerBlock).join(secondLayerBlock)

draw(secondLayerComponent.under(firstLayerComponent).under(secondLayerComponent).under(firstLayerComponent))