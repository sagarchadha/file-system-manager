from FileSystemManager import FileSystemManager

class Client(FileSystemManager):
  commands = {'read': 'read', 'save': 'save', 'del': 'delete', 'quit': 'quit'}
  active = True

  def checkArgs(self, args: list) -> bool:
    if args[0] not in client.commands:
      print('Unsupported command')
      return False
    return True
  
  def action(self, user_input: list) -> None:
    try:
      user_command, args = user_input[0], user_input[1:]
      command = self.__getattribute__(self.commands[user_command])
      command(*args)
    except TypeError or ValueError as err:
      print(err)
  
  def save(self, fileId: str, fileSize: str) -> None:
    result = FileSystemManager.save(self, fileId, fileSize)
    print(f'{fileId} was saved to the following blocks: {result}')

  def read(self, fileId: str) -> None:
    result = FileSystemManager.read(self, fileId)
    print(f'{fileId} returned the following blocks: {result}')
  
  def delete(self, fileId: str) -> None:
    result = FileSystemManager.delete(self, fileId)
    print(f'{fileId} was deleted and freed the following blocks: {result}')
  
  def quit(self):
    self.active = False
    print('Thank you for using this application.')

if __name__ == '__main__':
  client = Client()

  while client.active:
    values = input('Please enter your command:')
    args = values.split()
    if client.checkArgs(args):
      client.action(args)
