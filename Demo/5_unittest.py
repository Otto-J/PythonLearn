import unittest

class TestBeginner(unittest.TestCase):
    # 在每个测试方法调用之前被执行
    def setUp(self):
        pirnt('setup before 测试用例')

    # 在测试方法调用之后执行
    def tearDown(self):
        print('tearDown after 测试用例')

    # 所有case运行前
    @classmethod
    def setUpClass(cls):
        print('setup before TestBeginner.')

    # 所有case运行后
    @classmethod
    def tearDownClass(cls):
        print('tear down after TestBeginner.')

    # 以上都是准备工作

    # 使用名称以 test 开头的方法定义三个单独的测试
    # 命名约定通知 测试运行器 哪些方法代表测试

    def test_case1(self):
        print('test case1')

    def test_case2(self):
        print('test case2')

    def test_case3(self):
        print('test case3')

    def test_stat_report_input_output_size_should_ok(self):
        stu_list = [
            ['alice',81],
            ['bob',73],
            ['cindy',66],
            ['david',96],
            ['ella',84],
            ['frank',56]
        ]
        ans = tool.start_report(stu_list)
        self.assertEqual(len(stu_list), len(ans))
        self.assertEqual(ans[0][1],'良好')
        
