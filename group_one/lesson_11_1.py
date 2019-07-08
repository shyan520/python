# 11--11.2.2 一个要测试的类#############################################################################################
from group_one.lesson_11_survey import AnonymousSurvey

"建立一个问题"
question = "你喜欢吃什么食物？"
my_surey = AnonymousSurvey(question)

#显示问题，并储存答案
my_surey.show_question()
print("按Q终止")
sign = True
while sign:
    response = input("请出入您的答案：")
    if response.lower() == 'q':
        sign = False
    else:
        my_surey.store_respone(response)

print("谢谢您的参与！\n")
my_surey.show_results()

# 11--11.2.3 测试 AnonymousSurvey 类####################################################################################
import unittest
from group_one.lesson_11_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试"""

    def test_store_single_respone(self):
        """测试单个答案会被妥善地存储"""
        question = "你喜欢吃什么食物？"
        my_surey = AnonymousSurvey(question)
        my_surey.store_respone("蛋糕")

        "核实-蛋糕在AnonymousSurvey类的responses列表内"
        self.assertIn("蛋糕", my_surey.responses)

    def test_store_three_respone(self):
        """测试三个答案会被妥善地存储"""
        question = "你喜欢吃什么食物？"
        my_surey = AnonymousSurvey(question)
        responses = ["蛋糕", "草莓", "巧克力"]
        for response in responses:
            my_surey.store_respone(response)

        "核实-蛋糕、草莓、巧克力在AnonymousSurvey类的responses列表内"
        for response in responses:
            self.assertIn(response, my_surey.responses)

#        self.assertIn("番茄", my_surey.responses)


if __name__ == "__main__":
    unittest.main()


