# Anti-Duplicator

This script allows to find duplicate files in folder and it's subfolders.
You need to specify folder path as a parameter. 

# Quickstart

The script needs Python 3.5 interpreter.

Example of script launch on Linux, Python 3.5:

```bash
$ python duplicates.py <path to folder>
```

Example of script output:

```bash
Found duplicate files:
--
test.py of size 109 bytes in folders:
c:\p
c:\p\dir 2
--
3.txt of size 0 bytes in folders:
c:\p\dir 1
c:\p\dir 1\subdir 1

Process finished with exit code 0
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
