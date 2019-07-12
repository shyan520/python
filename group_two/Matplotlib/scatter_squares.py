# 15--15.2.3 使用 scatter() 绘制散点图并设置其样式======================================================================
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置多个坐标点
# x_values = [1, 2, 3, 4, 5]
x_values = list(range(1, 1001))
#y_values = [1, 4, 9, 16, 25]
y_values = [x**2 for x in x_values]

# 设置散点的尺寸：s=2；颜色：c='r'；去除原点边框：edgecolor='none'
# plt.scatter(x_values, y_values, s=2, c='r', edgecolor='none')
# 15.2.8 使用渐变颜色===================================================================================================
"""
我们将参数 c 设置成了一个 y 值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。
这些代码将 y 值较小的点显示为浅蓝色，并将 y 值较大的点显示为深蓝色
所有的颜色映射:https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
"""
plt.scatter(x_values, y_values, s=2, c=y_values, edgecolor='none', cmap=plt.cm.Blues)
plt.title('散点图', fontsize=24)
plt.xlabel('值', fontsize=14)
plt.ylabel('平方值', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', color='r', labelsize=14)

# 设置每个坐标轴的取值范围
# 设置x轴的范围：0~1100；y轴的范围：0~1100000
plt.axis([0, 1100, 0, 1100000])

# plt.show()

# 15.2.9 自动保存图表===================================================================================================
plt.savefig(r'scatter.png', bbox_inches='tight')
