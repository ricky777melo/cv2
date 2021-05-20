import os
import matplotlib.pyplot as plt
import numpy as np

cur_path =  os.path.abspath(os.path.dirname(__file__))
root_path = cur_path[:cur_path.find("pyHFT\\")+len("pyHFT\\")]

def printList(array,dim=2):
    if dim==2:
        for i in array:
            print(i)
    if dim==1:
        print(array)
def scatter(x1,y1,x2=[],y2=[],xmax=1,xmin=-1,ymax=1,ymin=-1):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(xmax=xmax, xmin=xmin)
    plt.ylim(ymax=ymax, ymin=ymin)

    colors1 = '#00CED1'  # 点的颜色
    colors2 = '#DC143C'
    area = np.pi * 4 ** 2  # 点面积
    # 画散点图
    plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')
    plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='类别B')
    plt.plot([0, 9.5], [9.5, 0], linewidth='0.5', color='#000000')
    plt.legend()
    plt.show()

def curve(title,x,y,label='first',x1=[],y1=[],label1='second',x2=[],y2=[],label2='third',x3=[],y3=[],label3='forth',prompt="曲线如图所示"):
    #网格
    ax = plt.gca()
    ax.set_xlim(0, x.__len__())
    miloc = plt.MultipleLocator(1)
    ax.xaxis.set_minor_locator(miloc)
    ax.grid(axis='x', which='minor')
    #网格
    ax.set_xticklabels(x, rotation=40, horizontalalignment='right')
    ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    plt.plot(x,y,label=label)
    plt.plot(x1,y1,label=label1)
    plt.plot(x2,y2,label=label2)
    plt.plot(x3,y3,label=label3)
    plt.title(title)
    plt.legend()

    plt.show()
    print()
    print(title,prompt)
def plot_decision_boundary(dim,pred_func,X,y):
    xxs=[]
    yys=[]
    lengths=[]
    explaining_variables =[]
    x_min, x_max = X.min(), X.max()
    y_min, y_max = X.min(), X.max()
    # 设定最大最小值，附加一点点边缘填充
    h = 0.01
    for i in range(dim//2):
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        xxs.append(xx)
        yys.append(yy)
        lengths.append(xx.ravel().__len__())
        explaining_variables.append(xx.ravel())
        explaining_variables.append(yy.ravel())
        #target_before=np.c_[xx.ravel(), yy.ravel()]
    explaining_variables=np.transpose(np.array(explaining_variables))
    # 用预测函数预测一下
    Z = pred_func(explaining_variables)

    Z = Z.reshape(xxs[0].shape)
    # 然后画出图
    plt.contourf(xxs[0], yys[0], Z, cmap=plt.cm.get_cmap('Spectral'))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.get_cmap('Spectral'))


def dynamiCurve():
    sampleSize=10000
    X = np.random.randint(0, 512, sampleSize).tolist()
    Y = np.random.randint(0, 512, sampleSize).tolist()

    fig = plt.figure()
    ax = plt.gca()
    # ax.spines['bottom'].set_color('none')
    # ax.spines['right'].set_color('none')
    # 设置坐标轴上的数字显示的位置，top:显示在顶部  bottom:显示在底部,默认是none
    # ax.xaxis.set_ticks_position('top')
    # ax.yaxis.set_ticks_position('left')

    ax.xaxis.set_ticks_position('top')
    ax.invert_yaxis()
    ax.set_xticks(np.linspace(0, 512, 10, endpoint=True))
    ax.set_yticks(np.linspace(512, 0, 10, endpoint=True))

    # plt.xlim(0,512)
    # plt.ylim(0,512)
    # plt.xticks(np.linspace(0,512,10,endpoint=True))
    # plt.yticks(np.linspace(0,512,10,endpoint=True))

    for i in range(0, sampleSize):
        ax.scatter(X[i], Y[i], c='b', marker='o',)
        plt.pause(0.001)
    plt.show()
def threeD(xd,yd,zd,xd2=[],yd2=[],zd2=[],Xlabel='x',Ylabel='y',Zlabel='z'):
    xd=np.array(xd)
    yd=np.array(yd)
    zd=np.array(zd)
    xd2=np.array(xd2)
    yd2=np.array(yd2)
    zd2=np.array(zd2)
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
#    ax1.set_zlim3d(0.5,0.6)设置z轴的显示范围
#    ax1.set_ylim3d(10,20)
    ax1.scatter3D(xd, yd, zd, cmap='Blues')  # 绘制散点图
    ax1.scatter3D(xd2, yd2, zd2, cmap='Reds')  # 绘制散点图
    ax1.set_xlabel(Xlabel)
    ax1.set_ylabel(Ylabel)
    ax1.set_zlabel(Zlabel)
    plt.show()

def progressBar(time,times,prompt="已完成："):
    now=round((time + 1) * 100 / times,2)
    print('\r' + prompt + str(now), end='%', flush=True)
    # 计算x,y坐标对应的高度值
def f(x, y):
    return (1 - x / 2 + x ** 3 + y ** 5) * np.exp(-x ** 2 - y ** 2)
if __name__=='__main__':





    # 生成x,y的数据
    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
    X, Y = np.meshgrid(x, y)
    print(f(X, Y).shape)
    # 填充等高线
    plt.contourf(X, Y, f(X, Y))
    # 显示图表
    plt.show()