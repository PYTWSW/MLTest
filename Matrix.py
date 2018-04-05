'''
#矩阵的初始化

import numpy as np #导入NumPy包

#创建一个3*5的全0矩阵和全1矩阵
myZero = np.zeros([3, 5]) #3*5的全0矩阵
print(myZero)

myOnes = np.ones([3, 5])  #3*5的全1矩阵
print(myOnes)

#生成随记矩阵
myRand = np.random.rand(3, 4) #3行4列的0-1之间的随机数矩阵
print(myRand)

#单位阵
myEye = np.eye(3) #3*3的单位阵
print(myEye)
'''

#矩阵的元素运算
from numpy import * #导入NumPy包

#元素相加和相减
myOnes = ones([3, 3])
myEye = eye(3)
print(myOnes + myEye)
print(myOnes - myEye)

#矩阵数乘：一个数乘以一个矩阵
mymatrix = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = 10
print(a * mymatrix)

#矩阵所有元素求和
print(sum(mymatrix))

#矩阵各元素的积：矩阵的点乘同维对应元素的相乘
mymatrix1 = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mymatrix2 = 1.5 * ones([3, 3])
print(multiply(mymatrix1, mymatrix2))

#矩阵各元素的n次幂:n=2
mylist = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(power(mylist, 2))

#矩阵的乘法：矩阵乘矩阵

mymatrix3 = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mymatrix4 = mat([[1], [2], [3]])
print(mymatrix3 * mymatrix4)

#矩阵的转置
mymatrix5 = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mymatrix5.T)     #矩阵的转置
mymatrix5.transpose()  #矩阵的转置
print(mymatrix5)

#矩阵的其它操作：行列数、切片、复制、比较
mymatrix6 = mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[m, n] = shape(mymatrix6)   #矩阵的行列数
print("矩阵的行数和列数:", m, n)

mysc11 = mymatrix6[0]   #按行切片
print("按行切片：", mysc11)

mysc12 = mymatrix6.T[0] #按列切片
print("按列切片：", mysc12)

mycpmat = mymatrix6.copy() #矩阵的复制
print("矩阵的复制：\n", mycpmat)

#比较
print("矩阵元素的比较：\n",mymatrix6 < mymatrix6.T)
