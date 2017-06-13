import numpy as np
import matplotlib.pyplot as plt

# 导入数据成为矩阵
data = np.loadtxt("section1.txt")

# 创建画布
plt.figure()

# 绘图：x轴数据为第二列，y轴数据为第一列，标记和线型
plt.plot(data[:, 1], data[:, 0],"ro--")

# 设置坐标轴标题
plt.xlabel("curvature")
plt.ylabel("moment")

# 设置图题
plt.title("moment-curvature")

# 坐标轴刻度
# plt.xticks([0, 0.0005, 0.002])
# plt.yticks([0, 500, 3000])

# 显示，而不是保存
plt.show()
