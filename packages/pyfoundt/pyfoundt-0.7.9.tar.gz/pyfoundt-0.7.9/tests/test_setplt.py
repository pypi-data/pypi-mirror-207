import unittest
from pyfoundt import setplt

te = 1
setplt.newfile("c:/ll.txt")
setplt.new_ile("c:/l.txt")
pip = setplt.PipOperation()
pip.uninstall("numpy", "c:/")
pip.install("numpy", "c:/")
pip.upgrademodular("c:/pip")
pip.piplist("c:/")


class TestSetPltFoundent(unittest.TestCase):
    def test_newfile(self):
        try:
            with open("c:/ll.txt", "r") as f:
                f.close()
        except Exception:
            self.assertEqual(te, 2)
        else:
            self.assertEqual(te, 1)
            f.close()

    def test_returnfileinfo(self):
        l = setplt.return_file_info("c:/ll.txt")
        with open("c:/ll.txt", "r") as f:
            lv = f.read()
            self.assertEqual(l, lv)
            f.close()

    def test_delete(self):
        setplt.delete("c:/l.txt")
        try:
            with open("c:/l.txt") as f:
                f.close()
        except Exception:
            self.assertEqual(te, 1)
        else:
            self.assertEqual(te, 2)
            f.close()

    def test_returnrlnfo(self):
        import requests
        l = setplt.return_url_info("https://baidu.com")
        lv = requests.get("https://baidu.com").text
        self.assertEqual(l, lv)

    def test_geturlInfile(self):
        import requests
        setplt.get_url_Infile("https://baidu.com")
        r = requests.get("https://baidu.com")
        r.encoding = "utf-8"
        with open("c:/n.html", "wb") as f:
            f.write(r.content)
        try:
            with open("c:/.html", "r", encoding="utf-8") as f:
                rv = f.read()
                f.close()
            with open("c:/n.html", "r") as f:
                rvv = f.read()
                f.close()
        except UnicodeDecodeError:
            self.assertEqual(te, 1)
        else:
            self.assertEqual(rv, rvv)


class TestClassPipOperation(unittest.TestCase):
    def test_install(self):
        try:
            with open("c:/install -numpy.bat", "r"):
                print()
        except FileNotFoundError:
            self.assertEqual(te, 2)
        else:
            self.assertEqual(te, 1)

    def test_uninstall(self):
        try:
            with open("c:/uninstall -numpy.bat", "r"):
                print()
        except FileNotFoundError:
            self.assertEqual(te, 2)
        else:
            self.assertEqual(te, 1)

    def test_upgrademodular(self):
        try:
            with open("c:/upgrade pip.bat", "r"):
                print()
        except FileNotFoundError:
            self.assertEqual(te, 2)
        else:
            self.assertEqual(te, 1)

    def test_pip_list(self):
        try:
            with open("c:/pip_list.bat", "r"):
                print()
        except FileNotFoundError:
            self.assertEqual(te, 2)
        else:
            self.assertEqual(te, 1)


class TestClassTime(unittest.TestCase):
    def test_now(self):
        from datetime import datetime
        time = setplt.Time
        n = time.now(detailed=True)
        nv = datetime.now()
        self.assertEqual(n, nv)


if __name__ == "__main__":
    unittest.main()
