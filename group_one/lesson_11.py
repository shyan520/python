# 11 测试代码################################################################################################
from group_one.lesson_11_name_function import get_formatted_name

print('打q退出输入')
while True:
    first = input('请输入您的姓：')
    if first.lower() == 'q':
        break
    last = input('请输入您的名：')
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('重新组合的姓名为：' + formatted_name)

# 11--11.1.2 可通过的测试################################################################################################
"""导入Python自带的测试模块unittest"""
import unittest
from group_one.lesson_11_name_function import get_formatted_name,get_formatted_middle_name_error,get_formatted_middle_name

"""创建了一个继承了unittest.TestCase，名为NameTestCase的测试类"""


class NameTestCase(unittest.TestCase):
    """创建了一个用于测试lesson_11_name_function模块的方法"""
    def test_get_formatted_name(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        """一个**断言**方法。断言方法用来核实得到的结果是否与期望的结果一致"""
        """“将`formatted_name`的值同字符串`'Janis Joplin'`进行比较，如果它们相等，就万事大吉，如果它们不相等，跟我说一声！”"""
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_get_formatted_middle_name_error(self):
        formatted_name = get_formatted_middle_name_error('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_get_formatter_middle_name(self):
        formatted_name = get_formatted_middle_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_get_formatter_middle_name1(self):
        formatted_name = get_formatted_middle_name('janis', 'joplin', 'a')
        self.assertEqual(formatted_name, 'Janis A Joplin')


"""我们运行lesson_11.py 时，所有以`test_`打头的方法都将自动运行"""
unittest.main()

