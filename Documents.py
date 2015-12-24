import time
def init():
    """ initial state """
    if not exists("1450617504600.png"):
        exit()
    click("1450617512741.png")
    wait("1450617981095.png")
    click("1450617981095.png")

def backHome():
    """ back to city select activity """
    while not exists("1450618092142.png"):
         click("1450618178686.png")
         wait("1450619546749.png", 6)
    statusBar = find("1450621142544.png").getCenter().offset(0,-64)
    hover(statusBar)


def lottery(item):
    """ lottery """
    if exists(item):
        click(item)
        try:
            wait("1450618588432.png", 6)
        except:
            backHome()
            return
        for x in range(3):
            doubleClick("1450618588432.png")
            time.sleep(8)
            doubleClick("1450618588432.png")


def loopCity():
    while True:
        for item in items:
            lottery(item)
            backHome()
        if exists("1450619672356.png"):
            return
        else:
           # slide up
           #wheel(WHEEL_DOWN, 3)
            statusBar = find("1450621142544.png").getCenter().offset(0,-64)
            wheel(WHEEL_DOWN, 1)
            dragDrop(statusBar, statusBar.offset(Location(10,-100)))

def changeCity(item):
    if exists(Pattern("1450658612825.png").similar(0.80)):
        click(Pattern("1450657885056.png").similar(0.80))
        if exists(item):
            click(item)
            wait("1450618092142.png")

cityList = [
            Pattern("1450658042078.png").similar(0.80),
            Pattern("1450658049729.png").similar(0.80),
            Pattern("1450658055885.png").similar(0.80),
            Pattern("1450658060710.png").similar(0.80),
            Pattern("1450658065534.png").similar(0.80),
            Pattern("1450658070482.png").similar(0.80),
            Pattern("1450658101190.png").similar(0.80),
            Pattern("1450658108132.png").similar(0.80),
            Pattern("1450658114163.png").similar(0.80),
            Pattern("1450658119756.png").similar(0.80),
            Pattern("1450658125427.png").similar(0.80),
            Pattern("1450658130116.png").similar(0.80),
            Pattern("1450658136808.png").similar(0.80),
        ]
items = [Pattern("1450661458586.png").similar(0.91), Pattern("1450926366175.png").similar(0.91)]
if __name__ == "__main__":
    init()
    backHome()
    for city in cityList:
        changeCity(city)
        loopCity()
