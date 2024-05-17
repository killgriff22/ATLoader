import os
from sys import argv

if argv[1] == "reload":
    import onopen
    exit()
elif argv[1] == "themviewer":
    import themeloader
    for theme in os.listdir("@themes"):
        print(theme)
        print(themeloader.themeloader.gettheme(theme).logo)
