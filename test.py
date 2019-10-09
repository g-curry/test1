# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# np.random.seed(sum(map(ord,"aesthetics")))
#
#
#
# '''
# Seaborn有5种预定义的主题：
# darkgrid（灰色背景+白网格）
# whitegrid（白色背景+黑网格）
# dark（仅灰色背景）
# white（仅白色背景）
# ticks（坐标轴带刻度）
# 默认的主题是darkgrid，修改主题可以使用set_style函数
# '''
# sns.set_style("whitegrid")
# #首先定义一个函数用来画正弦函数，可帮助了解可以控制的不同风格参数
# def sinplot(flip=1):
#     x=np.linspace(0,14,100)
#     for i in range(1,7):
#         plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)
# sinplot()
#
# # 设置横坐标的文字说明
# plt.xlabel("Types of Students")
# # 设置纵坐标的文字说明
# plt.ylabel("Frequency")
# # 设置标题
# plt.title("Numbers of Books Students Read")
# plt.show()
#
#


import time
[(time.sleep(0.0009),  print("\033[91m"+i,end="",flush=True)) for i in ('\n'.join([''.join([(' I love U'[(x-y)%9]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))]