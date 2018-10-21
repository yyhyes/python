#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
求从第一个基到第二个基的过渡矩阵
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
        return coordinate

# 例子：
alpha = np.array([[2, 1, -1, 1], [0, 3, 1, 0], [5, 3, 2, 1], [6, 6, 1, 3]]) #第二个基
theta = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) #第一个基
coordinate = baseCoordinate(alpha, theta)
print(coordinate)
