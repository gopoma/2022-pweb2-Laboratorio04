"""Determine si una matriz es unitaria"""
from Ejercicio1 import esEscalar

def esUnitaria(mtx):
  return mtx[0][0] == 1 and esEscalar(mtx)

mtx = [
  [4, 0, 0],
  [0, 4, 0],
  [0, 0, 4]
]
mtx2 = [
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]
mtx3 = [
  [4, 0, 5],
  [0, 4, 0],
  [0, 0, 4]
]

print(esUnitaria(mtx))
print(esUnitaria(mtx2))
print(esUnitaria(mtx3))