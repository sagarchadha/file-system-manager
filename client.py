from FileSystemManager import FileSystemManager

class Client:
  commands = {'read': 'read', 'save': 'save', 'del': 'delete'}

  def checkArgs(self, args: list) -> bool:
    if args[0] not in client.commands:
      print('Unsupported command')
      return False
    return True
  
  def action(self, args: list) -> None:
    try:
      command = getattr(fileSystemManager, self.commands[args[0]])
      print(command(*args[1:]))
    except ValueError as err:
      print(err)

if __name__ == '__main__':
  fileSystemManager = FileSystemManager()
  client = Client()

  while True:
    values = input('Please enter your command:')
    args = values.split()
    if client.checkArgs(args):
      client.action(args)
