from numpy import array
from numpy import concatenate
from numpy import zeros
from numpy.linalg import det
# from scipy.linalg import solve

def principalMinor(A):
    # 判断，矩阵A的各阶顺序主子式不为0返回1，否则返回0
    if len(A) != len(A[0]):
        print("错误，请提供方阵！！！")
        return 0
    for i in range(len(A)):
        temp = A[0:i+1, 0:i+1]
        if det(temp) == 0:
            return 0
    return 1

def gaussElimin(A,b):
    #顺序高斯消去法，参数系数矩阵A和常数项向量b，输出化简的过程并返回方程组的解
    if not(principalMinor(A)):
        print("不满足高斯消去法的条件：各阶顺序主子式都不等于0")
        return 0
    C = concatenate((A, b.T), axis=1) #增广矩阵
    # 进行顺序高斯消去法
    for i in range(1,len(A)):
        for j in range(i,len(A)):
            ratio = C[j,i-1] / C[i-1,i-1]
            C[j,:] = C[j,:] - ratio*C[i-1,:]
        print(C)
        print("---------------")
    # 回带求解
    x = zeros(len(A))
    # x = array([[1, 2, 3]])
    for i in range(len(A)):
        x[len(A)-i-1] = C[len(A)-i-1,len(A)] / C[len(A)-i-1,len(A)-i-1]
    return x

A = array([[2, -4, 2], 
        [1, 2, 3], 
        [-3, -2, 5]])
b = array([[2, 3, 1]])
result = gaussElimin(A,b)
print(result)
# print(gaussElimin(A,b))
