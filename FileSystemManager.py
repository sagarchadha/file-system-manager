from math import ceil, floor

class FileSystemManager:
  blockSize = 1024
  freeBlocks = []
  usedBlocks = {}

  def __init__(self, capacity: int=10240):
    super().__init__()
    numBlocks = self.calculateBlocks(capacity, True)
    self.freeBlocks = [i for i in range(numBlocks)]

  def calculateBlocks(self, fileSize: int, intial: bool=False) -> int:
    return floor(fileSize/self.blockSize) if intial else ceil(fileSize/self.blockSize)
  
  def allocateBlocks(self, fileSize: int) -> int:
    numBlocks = self.calculateBlocks(fileSize)

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
    
    
    numBlocks = self.allocateBlocks(self.convertToInt(fileSize))

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
