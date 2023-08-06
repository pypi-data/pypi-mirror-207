# Like shutil.which, but for all file types, and multiple results (if desired)

## pip install shlexwhichplus

#### Tested against Windows 10 / Python 3.10 / Anaconda

```python

import shutil

from shlexwhichplus import which_plus

print('_________________shutil.which')
print(shutil.which('python.exe'))
print(shutil.which('Python.exe'))
print(shutil.which('output.avi'))
print(shutil.which('output.avi')),
print(shutil.which(b'teSt.txt'))
print(shutil.which(b'teSt.txt'))

print('_________________which_plus')
print(which_plus('python.exe', mode='one', path=None))
print(which_plus('Python.exe', mode='all', path=None))
print(which_plus('output.avi', mode='all', path=None))
print(which_plus('output.avi', mode='one', path=None))
print(which_plus('api-ms-win-crt-conio-l1-1-0.dll', mode='one', path=None))
print(which_plus('api-ms-win-crt-conio-l1-1-0.dll', mode='all', path=None))
print(which_plus('Python.exe', mode='BLALBLALA', path=None))  # one if mode not in [all,one]
print(which_plus('TeST.txt', mode='all', path=None))
print(which_plus('teSt.txt', mode='one', path=None))
print(which_plus(b'teSt.txt', mode='all', path=None))
print(which_plus(b'teSt.txt', mode='one', path=None))


# output 


_________________shutil.which
C:\ProgramData\anaconda3\envs\dfdir\python.exe
C:\ProgramData\anaconda3\envs\dfdir\Python.exe
None
None
None
None
_________________which_plus
C:\ProgramData\anaconda3\envs\dfdir\python.exe
['C:\\ProgramData\\anaconda3\\envs\\dfdir\\python.exe']
['C:\\cprojekt\\output.avi', 'C:\\ProgramData\\anaconda3\\envs\\dfdir\\output.avi']
C:\ProgramData\anaconda3\envs\dfdir\output.avi
C:\ProgramData\anaconda3\envs\dfdir\api-ms-win-crt-conio-l1-1-0.dll
['C:\\ProgramData\\anaconda3\\envs\\dfdir\\api-ms-win-crt-conio-l1-1-0.dll', 'C:\\Program Files\\Microsoft\\jdk-11.0.16.101-hotspot\\bin\\api-ms-win-crt-conio-l1-1-0.dll', 'C:\\ProgramData\\anaconda3\\envs\\dfdir\\Library\\bin\\api-ms-win-crt-conio-l1-1-0.dll', 'C:\\Program Files\\Eclipse Adoptium\\jdk-11.0.18.10-hotspot\\bin\\api-ms-win-crt-conio-l1-1-0.dll', 'C:\\Program Files\\Amazon Corretto\\jdk17.0.6_10\\bin\\api-ms-win-crt-conio-l1-1-0.dll']
C:\ProgramData\anaconda3\envs\dfdir\python.exe
['C:\\ProgramData\\anaconda3\\envs\\dfdir\\Library\\bin\\TeST.txt', 'C:\\ProgramData\\anaconda3\\envs\\dfdir\\TeST.txt', 'C:\\ProgramData\\anaconda3\\envs\\dfdir\\Scripts\\TeST.txt']
C:\ProgramData\anaconda3\envs\dfdir\TeST.txt
[b'C:\\ProgramData\\anaconda3\\envs\\dfdir\\Library\\bin\\TeST.txt', b'C:\\ProgramData\\anaconda3\\envs\\dfdir\\TeST.txt', b'C:\\ProgramData\\anaconda3\\envs\\dfdir\\Scripts\\TeST.txt']
b'C:\\ProgramData\\anaconda3\\envs\\dfdir\\TeST.txt'




    Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH,
    or None if there is no such file.

    :param cmd: A string specifying the command to be searched.
    :type cmd: str
    :param mode: A string indicating whether to return one or all matches on the PATH.
                 If 'one', return the first match found on the PATH.
                 If 'all', return a list of all matches found on the PATH.
                 If any other string, mode defaults to 'one'.
    :type mode: str
    :param path: A string representing the search path. If None, uses the current system PATH variable.
    :type path: str|None
    :return: If mode is 'one', returns the first path found to the given command, or None if not found.
             If mode is 'all', returns a list of all paths found to the given command, or an empty list if not found.
    :rtype: str or list of str





```