import unittest
from pyfoundt.pyfoundt import useragents

ie = useragents.IE()
aoyou = useragents.AoYou()
sougou = useragents.SouGou()
qq = useragents.QQ()


class TestUseragentsFoundent(unittest.TestCase):
    def test_chrome(self):
        u = useragents.chrome()
        ui = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) "
                            "Chrome/14.0.835.163 Safari/535.1"}
        self.assertEquals(u, ui)

    def test_firefox(self):
        u = useragents.firefox()
        ui = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
        self.assertEquals(u, ui)

    def test_safari(self):
        u = useragents.safari()
        ui = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "
                            "Safari/534.5"}
        self.assertEquals(u, ui)

    def test_opera(self):
        u = useragents.opera()
        ui = {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
        self.assertEquals(u, ui)

    def test_l360v30(self):
        u = useragents.l360v30()
        ui = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR "
                            "2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; "
                            ".NET4.0C; .NET4.0E)"}
        self.assertEqual(u, ui)

    def test_AYun130Beta111205(self):
        u = useragents.AYun130Beta111205()
        ui = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"}
        self.assertEquals(u, ui)


class TestUseragentsClassIE(unittest.TestCase):
    def test_Win7Ie9(self):
        u = ie.Win7Ie9()
        ui = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; "
                            ".NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media "
                            "Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        self.assertEqual(u, ui)

    def test_Win7Ie8(self):
        u = ie.Win7Ie8()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; "
                            ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC "
                            "6.0; .NET4.0C; InfoPath.3"}
        self.assertEqual(u, ui)

    def test_WinxpIe8(self):
        u = ie.WinxpIe8()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)"}
        self.assertEqual(u, ui)

    def test_WinxpIe7(self):
        u = ie.WinxpIe7()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
        self.assertEqual(u, ui)

    def test_WinxpIe6(self):
        u = ie.WinxpIe6()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"}
        self.assertEqual(u, ui)


class TestUseragentsClassAoYou(unittest.TestCase):
    def test_AoYou317Gs(self):
        u = aoyou.AoYou317Gs()
        ui = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, "
                            "like Gecko) Maxthon/3.0 Safari/534.12"}
        self.assertEqual(u, ui)

    def test_AoYou317ieXh(self):
        u = aoyou.AoYou317ieXh()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; "
                            ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC "
                            "6.0; InfoPath.3; .NET4.0C; .NET4.0E)"}
        self.assertEqual(u, ui)


class TestUseragentsClassSouGou(unittest.TestCase):
    def test_SouGou30IeXh(self):
        u = sougou.SouGou30IeXh()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; "
                            ".NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC "
                            "6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"}
        self.assertEqual(u, ui)

    def test_SouGou30Gs(self):
        u = sougou.SouGou30Gs()
        ui = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, "
                            "like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"}
        self.assertEqual(u, ui)


class TestUseragentsClassQQ(unittest.TestCase):
    def test_QQ69w11079IeXh(self):
        u = qq.QQ69w11079IeXh()
        ui = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) "
                            "Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"}
        self.assertEqual(u, ui)

    def test_QQ69w11079Gs(self):
        u = qq.QQ69w11079Gs()
        ui = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET "
                            "CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; "
                            "InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201"}
        self.assertEqual(u, ui)


if __name__ == "__main__":
    unittest.main()
