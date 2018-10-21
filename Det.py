#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
求矩阵对应的行列式的值
"""
import numpy as np
from numpy.linalg import  *
# 例子：
alpha = np.array([[2, 1, -1, 1], [0, 3, 1, 0], [5, 3, 2, 1], [6, 6, 1, 3]]) #矩阵
myDet = det(alpha) #计算行列式
print(myDet)
