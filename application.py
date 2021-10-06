from client import Client

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