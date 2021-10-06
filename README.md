# File System Manager Application

## Starting the Application
The application can be started in the main directory by running the following command: `python3 application.py`.

## Using the Application
### Setting the Capacity of the File System
Upon startup, the application will prompt for the capacity of the file system. This value is meant to be an integer value. If an invalid value is entered, the default value of 10 blocks will be used. After the capacity is set, the file system manager will prompt the user for commands.

### Commands
The following are the different commands for the file system:

- `help`: Lists all of the possible commands that can be entered upon prompt. The command has no other required arguments.
  - Example: `help`
- `save`: Returns a list of blocks that the OS can store the file to. 
  - Required arguments:
    - `fileId`: This is a `str` value that represents the id of the file to be stored.
    - `fileSize`: This is a `int` value that represents the size of the file to be stored in bytes.
  - Example: `save file1 2048`
- `read`: Returns the list of blocks where the file is being stored. The command required the following arguments:
  - Required Arguments:
    - `fileId`: This is a `str` value that represents the id of the file to be read.
  - Example: `read file1`
- `del`: Returns the list of blocks where a file was being stored. The file is removed from those blocks and the blocks are available to store other files.
  - Required Arguments:
    - `fileId`: This is a `str` value that represents the id of the file to be deleted.
  - Example: `del file1`
- `quit`: Quits the application. The command has no other required arguments.
  - Example: `quit`

## File Structure
The following are descriptions for each of the files:
- `application.py`: This file contains the high level
- `client.py`: This file contains all of the logic for interacting with the user through the command line.
- `fileSystemManager.py`: This file contains all of the logic to determine and perform the actions to manipulate the blocks of storage dependent on the user's command.
