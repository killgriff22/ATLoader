import os
from sys import argv

if argv[1] == "reload":
    import onopen
    exit()
elif argv[1] == "themeviewer":
    import themeloader
    from termcolor import colored
    if len(argv) > 2 and argv[2] in os.listdir(os.environ['ZSH']+"/@themes"):
        theme = themeloader.themeloader.gettheme(argv[2])
        logosplit = theme.logo.splitlines()
        for i, line in enumerate(logosplit):
            print(colored(line, theme.colorset[i % len(theme.colorset)]))
        exit()
    for theme in os.listdir(os.environ['ZSH']+"/@themes"):
        print(theme)
        logosplit = themeloader.themeloader.gettheme(theme).logo.splitlines()
        for i,line in enumerate(logosplit):
            print(colored(line, themeloader.themeloader.gettheme(theme).colorset[i%len(themeloader.themeloader.gettheme(theme).colorset)]))
elif argv[1] == "settheme":
    if not len(argv) > 2:
        print("Usage: settheme <theme>")
        exit()
    if not argv[2] in os.listdir(os.environ['ZSH']+"/@themes"):
        print(f"Theme {argv[2]} not found.")
        exit()
    with open(os.environ['ZSH']+"/onopen.py", "w") as f:
        script = ("""import subprocess
import platform
import os
from sys import argv, stdout
from termcolor import colored
import themeloader

colors = theme.colorset
my_system = platform
logo = f\"""{theme.logo}\"""
logosplt = logo.splitlines()
counter = 0
maxlinelen = 0
NN = f"Node Name: {my_system.node()}"
AR = f"Arch : {my_system.machine()}"
OSR = f"OS Release : {my_system.release()}"
CPU = f"CPU : {platform.processor()}"
SYS = f"System : {my_system.system()}"
infopanetmp = f\"""
{CPU}
{OSR}
{AR}
{NN}
\"""
topline = "_______________________________________________"
bottomline = "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
infosplt = infopanetmp.splitlines()
for line in infosplt:
    if len(line) <= maxlinelen:
        pass
    elif len(line) > maxlinelen:
        maxlinelen = len(line)


def center(txt):
    center = ""
    for x in range(int(((int(len(topline))-2)-int(len(txt)))/2)):
        center += " "
    if len(txt) % 2 == 0:
        return center + txt + " " + center
    return center + txt + center


def filler():
    fill = ""
    for x in range(len(topline)-2):
        fill += " "
    return fill


def vcenter():
    center = ""
    if len(logosplt) > len(infosplt):
        buffer = int((len(logosplt)-len(infosplt))/2)
        for i in range(buffer):
            center += " "
    return center


infopane = f\"""
{vcenter()}
{topline}
|{center("@Loader")}|
|{center("Version 1.0.0")}|
|{center(f"{CPU}")}|
|{center(f"{OSR}")}|
|{center(f"{AR}")}|
|{center(F"{SYS}")}|
|{center(f"{NN}")}|
|{filler()}|
{bottomline}
{vcenter()}
\"""
infosplt = infopane.splitlines()
for index in range(len(logosplt)):
    if len(logosplt) > len(infosplt):
        buffer = int((len(logosplt)-len(infosplt)))
        for i in range(buffer):
            infosplt.append(" ")
    try:
        print(colored(logosplt[index], colors[counter]), end="")
        print(infosplt[index])
    except Exception as err:
        print(err)
    if counter == len(colors)-1:
        counter = 0
    counter += 1
""").split("\n")
        script[6] = f"theme = themeloader.themeloader.gettheme(\"{argv[2]}\")"
        script = "\n".join(script)
        f.write(script)
    import onopen
    exit()