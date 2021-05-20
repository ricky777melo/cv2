import numpy
from numpy import linalg as la
import random
import pandas as pd
def reduceDim(Xmatrix, exRate=0.99):
    '''
    :param Xmatrix: 解释变量矩阵：第k行为第k个样本的dim个变量
    :param dim: 变量原始维度
    :param exRate:降维后变量应该能解释exRate的降维前变量，通常为0.99，0.95,
    :return:降维后的Xmatrix', 与Xmatrix格式相同
    '''
    dim = Xmatrix[0].__len__()
    X = Xmatrix
    Xt = X.transpose()
    cov = numpy.matmul(Xt,X) / dim
    matrix = cov
    U, sigma, V = la.svd(matrix)
    sigmaSum = 0
    k = dim
    print("降维前的解释变量个数k:", k)
    for i in range(dim):
        sigmaSum += sigma[i]
    for i in range(1, dim + 1):
        subSum = 0
        for j in range(i):
            subSum += sigma[j]
        rate = subSum / sigmaSum
        if rate >= exRate:
            k = i
            break
    print("降维后的解释变量个数k:", k)
    answer = Xmatrix
    if k != dim:
        print("success to reduce dimensionality!\n\n")
        Ureduce = U[:, :k]
        Z =numpy.matmul( X , Ureduce)
    else:
        print("fail to reduce dimensionality!")
        print("the exRate is to large\n\n")
    return Z
def normalize(data,start=0,end=0,infinitesimal=0.001):
    '''
    数据归一化
    :param data:
    :return: 包含日期、日收盘价、日成交量
    '''
    try:
        data=data.tolist()
    except:
        pass
    if end==0:
        end=data[0].__len__()
    small=[]
    big=[]
    all=[]
    for i in range(start,end):
        small.append(float(data[0][i]))
        big.append(float(data[0][i]))
        all.append(0)
    n=data.__len__()
    for i in data:
        for j in range(start,end):
            i[j]=float(i[j])
        for j in range(start,end):
            if i[j]<small[j-start]:
                small[j-start]=i[j]
            if i[j]>big[j-start]:
                big[j-start]=i[j]
            all[j-start]+=i[j]
    for i in range(end-start):
        all[i]=all[i]/n
        big[i]=big[i]-small[i]

    answer=[]
    for i in range(data.__len__()):
        line=[]
        for j in range(start,end):
            line.append((data[i][j]-all[j-start])/(big[j-start]+infinitesimal))
        answer.append(line+data[i][end:])
    return numpy.array(answer)
def massUp(array):
    answer=[]
    tempArray=array.tolist()
    tempLen=tempArray.__len__()
    while True:
        if tempLen==0:
            break
        else:
            answer.append(tempArray.pop(random.randint(0,tempLen-1)))
            tempLen-=1
    return numpy.array(answer)
def randomArea(x1,x2,y1,y2,sampleSize):
    answer=[]
    for i in range(sampleSize):
        answer.append([random.uniform(x1,x2),random.uniform(y1,y2)])
    return numpy.array(answer)
def randomRandom(x1,x2,shape):
    answer=[]
    for i in range(shape[0]):
        line=[]
        for j in range(shape[1]):
            line.append(random.uniform(x1,x2))
        answer.append(line)
    return numpy.array(answer)
def infinitesimal():
    return 0.00001
def sigmoid(x):
    return 1/(numpy.exp(-x)+1)
def dsigmoid(y):
    return y*(1-y)
def relu(x):
    return numpy.where(x > 0, x, 0)
def drelu(x):
    return numpy.where(x > 0, 1, 0)
def dtanh(x):
    return 1-numpy.square(x)
def darctan(x):
    return 1/(1+numpy.square(x))
def rand_arr(a, b, *args):
    numpy.random.seed(0)
    return numpy.random.rand(*args) * (b - a) + a


def normalization(data):
    _range = numpy.max(data) - numpy.min(data)
    return (data - numpy.min(data)) / _range



def standardization(data):
    mu = numpy.mean(data, axis=0)
    sigma = numpy.std(data, axis=0)
    return (data - mu) / sigma

def get_date_list(start='2019-06-01',end='2020-11-30',freq='D'):
    date_list=pd.date_range(start=start,end=end,freq=freq).tolist()
    for i in range(date_list.__len__()):
        date_list[i]=str(date_list[i]).split(' ')[0]
    return date_list
def standardization(data):
    mu = numpy.mean(data, axis=0)
    sigma = numpy.std(data, axis=0)
    return (data - mu) / sigma
def z_score_normalize(data):
    ave=[0 for i in range(data[0].__len__())]
    sigma=[0 for i in range(ave.__len__())]
    len=data.__len__()
    for i in range(len):
        ave+=data[i]
    ave=ave/len
    for i in range(len):
        sigma+=(data[i]-ave)*(data[i]-ave)
    sigma=numpy.sqrt(sigma/len)
    return ave,sigma
if __name__ == '__main__':
    A=numpy.array([[1,2],[3,4],[5,6]])
    ave,sigma=z_score_normalize(A)
    print(ave,sigma)