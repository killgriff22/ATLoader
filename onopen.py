import subprocess
import platform
import os
from sys import argv, stdout
from termcolor import colored
import themeloader
colors = ['red', 'red']

my_system = platform
logo = """
        ...          
    .uW8***88e.      
   d8*"     `"8N.    
 .@8F   .ucu.. %8L   
 @8E  .@8""988  8N   
'88>  @8~  98F  98   
~88  X8E   98~  8E   
'88> 98&  d88  X8    
 %8N '88W@"%8ed*`    
  %8b. `"   ``       
   `*8bu.. ..u@      
      ^"***%"`       
"""
topline = ""
logosplt = logo.splitlines()
counter = 0
maxlinelen = 0
infopanetmp = f"""
CPU : {platform.processor()}
OS Release : {my_system.release()}
Arch : {my_system.machine()}
Node Name: {my_system.node()}
"""
infosplt = infopanetmp.splitlines()
for line in infosplt:
    if len(line) <= maxlinelen:
        pass
    elif len(line) > maxlinelen:
        maxlinelen = len(line)
    newtopline = ""
    for i in range(maxlinelen+2):
        newtopline += "_"
    topline = newtopline
    bottomline = topline.replace("_", "¯")


def center(txt):
    center = ""
    for x in range(int(((int(len(topline))-2)-int(len(txt)))/2)):
        center += " "
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


infopane = f"""
{vcenter()}
{topline}
|{center("@Loader")}|
|{center("Version 1.0.0")}|
|{center(f"CPU : {platform.processor()}")} |
|{center(f"OS Release : {my_system.release()}")}|
|{center(f"Arch : {my_system.machine()}")}|
|{center(f"System : {my_system.system()}")}|
|{center(f"Node Name: {my_system.node()}")}|
|{filler()}|
{bottomline}
{vcenter()}
"""
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
