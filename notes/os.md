# os.listdir() 
- a function that returns a list containing the names of the entries (files and directories) in the directory given by the path parameter.

import os

#### List all files and directories in the current directory
entries = os.listdir('.')
print(entries)

#### List all files and directories in a specific path
entries = os.listdir('/path/to/directory')
print(entries)

Key characteristics of os.listdir():

It returns both files and directories as **strings**
It doesn't include the special entries '.' and '..' (current and parent directories)
The returned names are in arbitrary order (not sorted)
It doesn't provide additional information about the entries (like whether they're files or directories)
It doesn't include the path in the returned names, just the filenames themselves
It can raise an OSError if the directory doesn't exist or can't be accessed

If you need more information about the entries or want to walk through directory trees, you might want to use os.walk() or the newer os.scandir() function, which provides more details and is more efficient for large directories.