from FileSystemManager import FileSystemManager

class Client(FileSystemManager):
  commands = {'read': 'read', 'save': 'save', 'del': 'delete', 'quit': 'quit', 'help': 'listCommands'}
  active = True

  def __init__(self, capacity=10):
    super().__init__(capacity=capacity)
    print(f'Application has started with a capacity of {capacity} blocks.')

  def checkArgs(self, args: list) -> bool:
    if args[0] not in client.commands:
      print('Unsupported command')
      return False
    return True
  
  def prompt(self) -> None:
    values = input('Please enter your command (type "help" to see list of commands):')
    args = values.split()
    if client.checkArgs(args):
      client.action(args)
  
  def listCommands(self) -> None:
    print(f'The following commands can be used: {", ".join(self.commands.keys())}')
  
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
  
  def quit(self) -> None:
    self.active = False
    print('Thank you for using this application.')

if __name__ == '__main__':
  capacity = input('Please insert a value for the number of total blocks to be allocated (default is 10 blocks): ')
  client = None

  if capacity.isdigit():
    client = Client(int(capacity))
  else:
    print('Value is not a valid interger. Using default value for capacity.')
    client = Client()

  while client.active:
    client.prompt()
