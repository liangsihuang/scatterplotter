import numpy as np
import matplotlib.pyplot as plt

# S1截面
# 导入数据成为矩阵
data = np.loadtxt("S1_load_disp.txt")

# 创建画布
plt.figure()

# 对数据进行无量纲处理，(由于数据为负数，改为正)
# 第一列为位移,原单位mm
l=500
disp=data[:, 0]*(-1)/l
# 第二列为力，需要乘以梁长变为弯矩，再除以塑性弯矩，单位N×mm
Mp=29079840
Mnon=data[:, 1]*(-1)*l/Mp

# 绘图：x轴数据为第一列，y轴数据为第二列，标记和线型
plt.plot(disp, Mnon,"ro--")

# 设置坐标轴标题
plt.xlabel("\delta/L")
plt.ylabel("M/Mp")

# 设置图题
plt.title("无量纲弯矩-相对位移曲线")

# 坐标轴刻度
# plt.xticks([0, 0.0005, 0.002])
# plt.yticks([0, 500, 3000])

# 显示，而不是保存
plt.show()

# # S2截面
# data2 = np.loadtxt("section2.txt")
# plt.figure()
# l=500
# disp=data[:, 0]*(-1)/l
# Mp=29079840
# Mnon=data[:, 1]*(-1)*l/Mp
# plt.plot(data[:, 0], data[:, 1],"ro--")
# plt.xlabel("\delta/L")
# plt.ylabel("M/Mp")
# plt.title("无量纲弯矩-相对位移曲线")

# # 坐标轴刻度
# # plt.xticks([0, 0.0005, 0.002])
# # plt.yticks([0, 500, 3000])

# # 显示，而不是保存
# plt.show()
