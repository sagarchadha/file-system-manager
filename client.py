from fileSystemManager import FileSystemManager

class Client(FileSystemManager):
  commands = {'read': 'read', 'save': 'save', 'del': 'delete', 'quit': 'quit', 'help': 'listCommands'}
  active = True

  def __init__(self, capacity=10):
    super().__init__(capacity=capacity)
    print(f'File system manager has started with a capacity of {capacity} blocks.')

  def checkArgs(self, args: list) -> bool:
    if len(args) == 0:
      print('Error: No command was given')
      return False
    elif args[0] not in self.commands:
      print('Error: Unsupported command')
      return False
    return True
  
  def prompt(self) -> None:
    values = input('Please enter your command (type "help" to see list of commands):')
    args = values.split()
    if self.checkArgs(args):
      self.action(args)
  
  def listCommands(self) -> None:
    print(f'The following commands can be used: {", ".join(self.commands.keys())}')
  
  def action(self, user_input: list) -> None:
    try:
      user_command, args = user_input[0], user_input[1:]
      command = self.__getattribute__(self.commands[user_command])
      command(*args)
    except ValueError as err:
      print(err)
    except TypeError as err:
      print('There was a mismatch between the number of arguments required and given for the command.')
  
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
