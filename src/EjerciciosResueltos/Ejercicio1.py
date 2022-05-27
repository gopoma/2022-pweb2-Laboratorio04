"""Determine si una matriz es escalar"""

def esEscalar(mtx):
  d = mtx[0][0]

  for i in range(len(mtx)):
    for j in range(len(mtx)):
      if i != j:
        if mtx[i][j] != 0:
          return False
      elif mtx[i][j] != d:
        return False

  return True


if __name__ == "__main__":
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

  print(esEscalar(mtx))
  print(esEscalar(mtx2))
  print(esEscalar(mtx3))