from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from requests import Response
from config.colors import *


def formatMilion(tick_val, pos):
    if tick_val > 1000000:
        val = int(tick_val)/1000000
        return f"{val} M"
    elif tick_val > 1000:
        val = int(tick_val) / 1000
        return f"{val} k"
    else:
        return tick_val

class PopulationController:
    def largest(response: Response):
        json = response.json()

        plt.style.use('fivethirtyeight')
        plt.bar(json.keys(), json.values())
        plt.xticks(rotation = 45)
        plt.ylabel('Počet obyvatel')
        plt.xlabel('Země')
        plt.title('10 největších zemí podle populace')
        ax = plt.gca()
        ax.yaxis.set_major_formatter(FuncFormatter(formatMilion))

        plt.show()

    def process(response: Response):
        json = response.json()

        plt.style.use('grayscale')
        plt.plot(json.keys(), json.values())
        plt.xticks(rotation = 45)
        plt.ylabel('Světová populace')
        plt.title('Počet obyvatel')
        ax = plt.gca()
        ax.yaxis.set_major_formatter(FuncFormatter(formatMilion))

        plt.show()
