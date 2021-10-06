from client import Client

if __name__ == '__main__':
  capacity = input('Please insert a capacity value in bytes to be allocated as the total storage (default is 10240 bytes or 10 blocks): ')
  client = None
  
  try:
    capacity = int(capacity)
    client = Client(int(capacity))
  except ValueError as err:
    print('Value is not a valid interger. Using default value for capacity.')
    client = Client()

  while client.active:
    client.prompt()