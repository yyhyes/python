#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
求一个向量在一个新的基底下的坐标
主要是用求解线性方程组的方法求解
"""
import numpy as np
from scipy.linalg import solve

def baseCoordinate(alpha, theta):
    alpha = alpha.T
    theta = theta.T
    if len(theta) != len(theta.T):
        print("基底组成的矩阵应该是方阵！！！")
    elif len(alpha) != len(theta):
        print("向量的维数应该等于基底的个数！！！")
    else:
        # solve
        coordinate = solve(theta, alpha) #坐标
        return coordinate.T

# 例子：
alpha = np.array([3, 7, 1])
theta = np.array([[1, 3, 5], [6, 3, 2], [3, 1, 0]])
coordinate = baseCoordinate(alpha, theta)
print(coordinate)
