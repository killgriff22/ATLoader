import os
from sys import argv
help = """
|||||||CUSTOM ALIASES|||||||
loadGP :: loads globalprotect
unloadGP :: unloads globalprotect
reloadGP :: reloads/fixes (normally) globalprotect
py :: python3 (will be updated to allow for python2 as well as other python versions)
|||||||COMMANDS THAT REUIRE @ AS A PREFIX|||||||
help :: shows this menu
theme :: change theme usage :: theme <theme-name>

"""
try:
    argv[2]
except:
    print(help)
    exit()
