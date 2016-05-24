# -*- coding: utf-8 -*-
"""
对常微分方程组求数值解，计算洛伦茨吸引子的轨迹。
"""
from scipy.integrate import odeint 
import numpy as np 

def nuetron_dynamics(w, t, p, r, b): 
    # 给出位置矢量w，和三个参数p, r, b计算出
    # dx/dt, dy/dt, dz/dt的值
    n, c, tho = w.tolist()
    # 直接与lorenz的计算公式对应 
    return 0.078*c-103.7*n, 64.1*n-1.01*10**(-4)*c, 0

t = np.arange(0, 30, 0.01) # 创建时间点 
# 调用ode对lorenz进行求解, 用两个不同的初始值 
track1 = odeint(nuetron_dynamics, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0)) 
track2 = odeint(nuetron_dynamics, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0)) 

# 绘图
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:,0], track1[:,1], track1[:,2])
ax.plot(track2[:,0], track2[:,1], track2[:,2])
plt.show()
