import os


def read(thePath,dim=2,gap=",",ifFloat=False,ifInt=False,encoding='utf-8'):
    '''

    :param thePath of the csvFile
    :return:
    '''
    if dim==2:
        with open(thePath, 'r', encoding=encoding) as f:
            data = f.read().split('\n')
        length=data.__len__()
        for i in range(length):
            data[i]=data[i].split(gap)
            if ifInt:
                for j in range(data[i].__len__()):
                    try:
                        data[i][j]=int(data[i][j])
                    except:
                        data[i][j]=i
            if ifFloat:
                for j in range(data[i].__len__()):
                    try:
                        data[i][j]=float(data[i][j])
                    except:
                        data[i][j]=i
    if dim==1:
        with open(thePath, 'r', encoding=encoding) as f:
            data = f.read().split(gap)
            if ifInt:
                data = [int(x) for x in data]
            if ifFloat:
                data=[float(x) for x in data]
    if dim==0:
        with open(thePath, 'r', encoding=encoding) as f:
            data = f.read()
            if ifInt:
                data = int(data)
            if ifFloat:
                data=float(data)


    return data

def write(thePath,data,dim=2,gap=',',encodeing='utf-8',append=False):
    '''

    :param thePath:
    :param data:二维数组
    :return:
    '''
    instruction='w'
    if append:
        instruction='a'
    if dim==2:
        with open(thePath,instruction, encoding=encodeing) as f:
            length=data.__len__()
            for i in range(length):
                line=[str(x) for x in data[i]]
                f.writelines(gap.join(line))
                if i!=length-1:
                    f.writelines("\n")
    if dim==1:
        with open(thePath, instruction, encoding=encodeing) as f:
            data=[str(x) for x in data]
            f.writelines(gap.join(data))
    if dim==0:
        with open(thePath, instruction, encoding=encodeing) as f:
            data=str(data)
            f.writelines(data)
    return True
def getRoot(root):
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find(root) + len(root)]
    return root_path
def sep():
    return os.sep
def filePath(pathList):
    answer=""
    for i in range(pathList.__len__()):
        answer+=pathList[i]
        if(i!=pathList.__len__()-1):
            answer+=sep()
    return answer




