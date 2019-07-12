# 15--15.2 绘制简单的折线图=============================================================================================
import matplotlib.pyplot as plt

# 初始化折线图的y坐标点
squares = [1, 4, 9, 16, 25]
# 根据坐标点绘制出折线图
#plt.plot(squares)
# 打开 matplotlib 查看器，并显示绘制的图形
# plt.show()

# 15--15.2.1 修改标签文字和线条粗细=====================================================================================
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
#plt.plot(squares, linewidth=3)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

#plt.show()

# 15--15.2.2 校正图形===================================================================================================
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, LW=3, c='red')
plt.show()