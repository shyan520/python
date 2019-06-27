# 10--10.4 存储数据################################################################################################
# 10--10.4.1 使用json.dump()和json.load()##########################################################################
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = r'test\numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

with open(filename, 'r') as f_object:
    numbers = json.load(f_object)
print(numbers)
print('10--10.4.1\n ')

# 10--10.4.2 保存和读取用户生成的数据##############################################################################
import json
class RmemberMe():
    def __init__(self, filename):
        self.filename = filename

    def writer_name(self):
        with open(self.filename, 'w', encoding='utf-8') as file_object:
            username = input('请输入您的姓名：')
            json.dump(username, file_object)
            print('你回来的时候我们会记得你的，' + username + '!\n')

    def read_name(self):
        with open(self.filename, 'r', encoding='utf-8') as file_object:
            print('欢迎回来！' + json.load(file_object))

filename = r'test\username.json'
rmemberme = RmemberMe(filename)
rmemberme.writer_name()
rmemberme.read_name()
print('10--10.4.2\n ')

# 10--10.4.3 重构##################################################################################################
import json
class GreetUser():
    def __init__(self, filename):
        self.filename = filename

    def read_user(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f_obj:
                username = json.load(f_obj)
        except FileNotFoundError:
            return None
        else:
            return username

    def writer_user(self):
        username = self.read_user()
        if username:
            print('欢迎回来！' + username)
        else:
            with open(self.filename, 'w', encoding='utf-8') as f_obj:
                username = input('请输入您的姓名：')
                json.dump(username, f_obj)
                print('你回来的时候我们会记得你的，' + username + '!\n')

filename = r'test\greetuser.json'
greetuser = GreetUser(filename)
greetuser.writer_user()
print('重构1\n ')

import json
class GreetUser1():
    def __init__(self, filename):
        self.filename = filename

    def read_user(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f_obj:
                username = json.load(f_obj)
        except FileNotFoundError:
            return None
        else:
            return username

    def writer_user(self):
        with open(self.filename, 'w', encoding='utf-8') as f_object:
            username = input('请输入您的姓名：')
            json.dump(username, f_object)
        print('你回来的时候我们会记得你的，' + username + '!\n')

    def greet_user(self):
        username = self.read_user()
        if username:
            print('欢迎回来！' + username)
        else:
            self.writer_user()

filename = r'test\greetuser1.json'
greetuser1 = GreetUser1(filename)
greetuser1.greet_user()
print('重构2\n ')