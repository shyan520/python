# 6--6.1 一个简单的字典#########################################################################
# 在Python中,字典是一系列【键—值】对。字典用放在花括号 {} 中的一系列【键—值】对表示
alien = {'color':'green','points':5}
print(alien['color'])
print(alien['points'])
print('6--6.1\n')

# 6--6.2.2 添加【键—值】对######################################################################
# 创建一个空字典
alien = {}
print(alien)
alien['color'] = 'green'
alien['points'] = 5
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)
print('6--6.2.2\n')

# 6--6.2.4 修改字典中的值#########################################################################
alien = {'color':'green'}
print(alien['color'])
alien['color'] = 'yellow'
print(alien['color'])

# 对一个能够以不同速度移动的外星人的位置进行跟踪。为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：
alien_0 = {'x_position':0,'y_position':25,}
# 初始化外星人的速度slow、medium、fast;默认为medium
alien_0['speed'] = 'medium'
print(alien_0)
# 外星人向右移动
# 根据外星人的速度状态，决定移动距离了
# 初始化移动距离
x_increment = 0
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])
print('6--6.2.4\n')

# 6--6.2.5 删除【键—值】对#########################################################################
alien = {'color':'green','points':5}
print(alien)
del alien['points']
print(alien)
print('6--6.2.5\n')

# 6--6.2.6 由类似对象组成的字典#####################################################################
favorite_languages = {
    'eric':'C++',
    'ella':'Python',
    'jack':'Java',
    'many':'ruby',
    }
print('Many favorite language is ' + favorite_languages['many'].title())
print('6--6.2.6\n')

# 6--6.3.1 遍历所有的【键—值】对####################################################################
favorite_languages = {
    'eric':'C++',
    'ella':'Python',
    'jack':'Java',
    'many':'ruby',
    }
# 方法items()返回一个【键—值】对列表
for key,value in favorite_languages.items():
    print('key: ' + key)
    print('value: ' + value)
print('6--6.3.1\n')

# 6--6.3.2 遍历字典中的所有键########################################################################
favorite_languages = {
    'eric':'C++',
    'ella':'Python',
    'jack':'Java',
    'many':'ruby',
    }
for key in favorite_languages.keys():
    print(key.title())
print('6--6.3.2\n')

# 6--6.3.4 遍历字典中的所有值########################################################################
favorite_languages = {
    'eric':'C++',
    'ella':'Python',
    'jack':'Java',
    'many':'ruby',
    'nina':'Python',
    }
for value in favorite_languages.values():
    print(value.title())
print('')
# 除去重复显示的'Python';注意‘值’的大小写，如果2个值大小写不一样，则不判定为重复值
for value in set(favorite_languages.values()):
    print(value.title())
print('6--6.3.4\n')

# 6--6.4 嵌套########################################################################################
# 6--6.4.1 字典列表##################################################################################
# 创建一队外星人信息
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# 自动创建30个绿色的外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed': 'slow'}
    aliens.append(new_alien)
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('......')
print('共创建了'+ str(len(aliens)) + '个外星人')
print('6--6.4.1\n')

# 6--6.4.2 在字典中存储列表############################################################################
# 在字典中存储列表
pizza = {
    '面皮':'厚',
    '材料':['番茄','起司','辣椒'],
}
print('你点的披萨面皮是'+ pizza['面皮'] +'的，使用的材料是：')
for p in pizza['材料']:
    print('\t' + p)
print('6--6.4.2\n')

# 6--6.4.3 在字典中存储字典############################################################################
# 创建3条用户信息
users = {
    'user_0':{
        'name':'ella',
        'age':4,
        'sex':'girl',
    },
    'user_1':{
        'name':'eric',
        'age':36,
        'sex':'man',
    },
    'user_2':{
        'name':'vanesse',
        'age':32,
        'sex':'woman',
    }
}
for user_number,user_info in users.items():
    print('user_number = ' + user_number)
    print('\t姓名：' + user_info['name'])
    print('\t年龄：' + str(user_info['age']))
    print('\t性别：' + user_info['sex'])
print('6--6.4.3\n')