import os
import requests


def returnfileinfo(file, encoding="utf-8"):
    f = None
    try:
        f = open(f"{file}", "r", encoding=encoding)
        for fv in f:
            return fv
    finally:
        if f is not None:
            f.close()


def newfile(file, data="", encoding="utf-8"):
    f = None
    try:
        with open(f"{file}", "a", encoding=encoding) as f:
            f.write(data)
    finally:
        if f is not None:
            f.close()

        else:
            try:
                with open(f"{file}", "a", encoding=encoding) as f:
                    f.write(data)
            finally:
                if f is not None:
                    f.close()


def return_url_info(url, headers):
    r = requests.get(url, headers=headers)
    return r.text


def geturlInfile(url, file="c:/.html"):
    r = requests.get(url)
    with open(file, "wb") as f:
        f.write(r.content)


def delete(file):
        os.remove(f"{file}")


class PipOperation(object):
    @staticmethod
    def install(modular):
        with open(f"install -{modular}.bat", "a") as f:
            f.write(f"pip install {modular} -i https://mirror.baidu.com/pypi/simple")

    @staticmethod
    def uninstall(modular):
        with open(f"uninstall -{modular}.bat", "a") as f:
            f.write(f"pip uninstall {modular}")

    @staticmethod
    def upgrademodular(modular):
        with open(f"upgrade {modular}.bat", "a") as f:
            f.write("pip install --upgrade pip")

    @staticmethod
    def piplist(luj=None):
        with open("pip_list.bat", "a") as f:
            f.write("pip list\nping 127.1 -n 6 >nul")


class Time(object):
    def __init__(self, year=2012, month=1, day=1,
                 hour=0, minute=0, second=0):

        self.hour = hour
        self.minute = minute
        self.second = second
        self.day = day
        self.month = month
        self.year = year

        for i in range(99):
            if self.second >= 60:
                self.minute += 1
                self.second -= 60
            if self.minute >= 60:
                self.hour += 1
                self.minute -= 60
            if self.hour >= 24:
                self.hour -= 24
                self.day += 1
            if self.day >= 30:
                self.day -= 30
                self.month += 1
            if self.month == 12:
                if self.day >= 30:
                    self.year += 1
                    self.month = 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def __str__(self):
        return "%.4d-%.2d-%.2d %.2d:%.2d:%.2d" % (self.year,
                                                  self.month,
                                                  self.day,
                                                  self.hour,
                                                  self.minute,
                                                  self.second)

    def __add__(self, time1, time2):
        return time1 + time2

    @staticmethod
    def now(detailed=False):
        if detailed is False:
            import datetime
            now = datetime.datetime.now()
            return now.strftime("%Y-%m-%d %H:%M:%S")
        if detailed is True:
            import datetime
            now = datetime.datetime.now()
            return now
