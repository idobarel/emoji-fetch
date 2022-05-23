#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import sys


def getName():
    return sys.argv[1] if len(sys.argv) == 2 else -1


class Fetcher():
    def __init__(self) -> None:
        self.data = requests.get(
            "https://unicode.org/emoji/charts/full-emoji-list.html").text
        self.trs = []
        self.makeData()

    def makeData(self):
        soup = BeautifulSoup(self.data, "lxml")
        self.data = soup.find_all("td")
        self.trs = soup.find_all("tr")

    def search(self, name: str):
        data = []
        for td in self.data:
            if td.attrs['class'][0] == "name":
                if name in str(td):
                    td = str(td)
                    data.append(td)
        return data

    def getEmojies(self, name: str):
        l = []
        data = self.search(name)
        if len(data) == 0:
            return False
        for tr in self.trs:
            tr = str(tr)
            for td in data:
                if td in tr:
                    l.append(tr.splitlines()[2][18])
                    continue
        return l


def main():
    name = getName()
    if name == -1:
        print(colored("Error, Use -h or --help", "red", attrs=['bold']))
        exit(1)
    elif name == '-h' or name == '--help':
        print(colored("Takes One Argument, The emoji you want!",
                      "white", attrs=['bold', 'dark']))
        exit(0)
    f = Fetcher()
    x = f.getEmojies(name)
    if x == False:
        print(colored("Found None...", 'red', attrs=['bold']))
        exit(1)
    print(colored(f"Found {len(x)} Emojies!", "green", attrs=['bold']))
    for i in x:
        print(i)


if __name__ == '__main__':
    main()

    
