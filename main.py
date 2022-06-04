#!/usr/bin/env python3
import plotext
import numpy as np
import pandas_datareader as pdr
from termcolor import colored
import requests
import os
import sys
import time


data = requests.get(
    "https://raw.githubusercontent.com/crypti/cryptocurrencies/master/cryptocurrencies.json").json()
data = data.keys()


def clearScreen():
    if sys.platform.lower() == 'win32':
        os.system("cls")
    else:
        os.system('clear')


def isCoin(s: str):
    s = s.upper()
    return s in data


class Stock():
    def __init__(self, name: str, history: np.ndarray) -> None:
        self.name = name
        self.price = history[-1]
        self.history = history


def getStock(s: str) -> Stock:
    s = s.upper()
    x = pdr.DataReader(f"{s}", "yahoo")
    history = np.array(x["Close"].values)
    return Stock(s, history)


class HandleStock():
    def __init__(self, s: Stock) -> None:
        self.stock = s

    def printName(self):
        s = colored(f"{self.stock.name} : {self.stock.price}",
                    "magenta", attrs=['bold'])
        print(s)

    def plot(self):
        x = np.array(data)
        plotext.plot(self.stock.history)
        plotext.canvas_color(240)
        plotext.ticks_color(35)
        plotext.axes_color(240)  # back-240 | fore-35
        plotext.title(f"{self.stock.name} - Close Price")
        plotext.limit_size(False)
        plotext.plot_size(50, 15)
        plotext.show()


def main():
    symbol = sys.argv[1] if len(sys.argv) == 2 else -1
    if symbol == -1:
        print(colored("Excepting stock symbol as an argument..."))
        exit(1)
    print(colored(f"Getting Data For {symbol} >> ",
                  "yellow", attrs=['bold', 'dark']))
    if isCoin(symbol):
        symbol += "-USD"
    time.sleep(1)
    s = getStock(symbol)
    obj = HandleStock(s)
    print(colored("Found!", "green", attrs=['bold']))
    time.sleep(1)
    clearScreen()
    obj.printName()
    obj.plot()


if __name__ == '__main__':
    main()
