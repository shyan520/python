# 11--11.2.4 方法 setUp()###############################################################################################
import unittest
from lesson_11_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self) -> None:
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "你喜欢吃什么食物？"
        """创建一个调查对象"""
        self.my_survey = AnonymousSurvey(question)
        """创建一个答案列表"""
        self.responses = ["蛋糕", "草莓", "巧克力"]

    def test_store_single_response(self):
        """测试一个答案会被妥善地存储"""
        self.my_survey.store_respone(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        #        self.assertIn("西瓜", self.my_survey.responses)

    def test_store_three_response(self):
        """测试多个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_respone(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
