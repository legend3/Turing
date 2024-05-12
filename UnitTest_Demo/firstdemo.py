import unittest


# 通过继承 unittest。TestCase 来实现用例
class forTest(unittest.TestCase):
    #类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print('class')
    #类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print('tclass')
    
    # 测试用例初始化
    def setUp(self) -> None: 
        print("setUp")#测试用例释放
    def tearDown(self)-> None:
        print("teadDown")
        
    # 测试用例
    def test_a(self): 
        print("a")#测试用例
    def test_b(self):
        print("b")#团数
    def add(self, a, b):
        return a + b#测试用例
    def test_c(self):
        c = self.add(1,3) 
        print('c =', c)


if __name__ == '__main__':
    unittest.main(verbosity=2) # 参数 verbosity=2的目的是为了让打印的信