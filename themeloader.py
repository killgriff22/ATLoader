import os


class themeloader:
    def gettheme(theme):
        class theme:
            logo = open(
                f"{os.environ['ZSH']}/@themes/{theme}/{theme}.logo").read()
            colorset = open(
                f"{os.environ['ZSH']}/@themes/{theme}/{theme}.colorset").readlines()
            for line in colorset:
                colorset[colorset.index(line)] = line.strip("\n")
        return theme
