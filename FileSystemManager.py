from math import ceil

class FileSystemManager:
  capacity = 0
  blockSize = 1024
  freeBlocks = []
  usedBlocks = {}

  def __init__(self, capacity: int=10):
    super().__init__()
    self.capacity = capacity
    self.freeBlocks = [i for i in range(self.capacity)]

  def calculateNumBlocks(self, fileSize: int) -> int:
    numBlocks = ceil(fileSize/self.blockSize)

    if numBlocks > len(self.freeBlocks):
      raise ValueError(f'Error: Not enough space for file with size of {fileSize} bytes')
    
    return numBlocks

  def convertToInt(self, value: str) -> int:
    try: 
      return int(value)
    except ValueError as err:
      raise ValueError('Error: File size input is not an integer.')

  def save(self, fileId: str, fileSize: str) -> list:
    if fileId in self.usedBlocks:
      raise ValueError('Error: File already exists')
    
    
    numBlocks = self.calculateNumBlocks(self.convertToInt(fileSize))

    newBlocks = []
    for _ in range(numBlocks):
      newBlocks.append(self.freeBlocks.pop())
    self.usedBlocks[fileId] = newBlocks
    return newBlocks

  def read(self, fileId: str) -> list:
    if fileId not in self.usedBlocks:
      raise ValueError('Error: File does not exist')

    return self.usedBlocks[fileId]

  def delete(self, fileId: str) -> None:
    if fileId not in self.usedBlocks:
      raise ValueError('Error: File does not exist')
    
    deletedBlocks = self.usedBlocks[fileId]
    self.freeBlocks = self.freeBlocks + deletedBlocks
    del self.usedBlocks[fileId]
    return deletedBlocks
