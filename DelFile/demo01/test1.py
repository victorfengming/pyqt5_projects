from sys import argv
from os import system
path = "del /F /S /Q "+argv[1]+">nul\nRD /S /Q "+argv[1]+">nul"
system(path)

