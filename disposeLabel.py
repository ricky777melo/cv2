import os
import matplotlib.pyplot as plt
from PIL import Image
import pylab
import json
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        return files
import json
import util.file as RF
import util.IO as RI

def generateCategoryFile():
    test_images=json.load(open("train.json",'r'))
    category_mapping=[]
    for image_name in test_images:
        for object_id in test_images[image_name]['objects']:
            category = test_images[image_name]['objects'][object_id]['category']
            if category not in category_mapping:
                category_mapping.append(category)
    category_num=len(category_mapping)
    print("category num:",category_num)
    RF.write('category.txt',category_mapping,dim=1,gap='\t')
    print(category_mapping)
def checkCategory():
    test_images=json.load(open("val.json",'r'))
    category_mapping=getCategoryMapping()
    for image_name in test_images:
        for object_id in test_images[image_name]['objects']:
            category = test_images[image_name]['objects'][object_id]['category']
            if category not in category_mapping:
                print(category,'error')
def getCategoryMapping():
    categorys=RF.read('category.txt',dim=1,gap='\t')
    category_mapping={}
    for i in range(categorys.__len__()):
        category_mapping[categorys[i]]=i
    return category_mapping
def getCategoryList():
    categorys = RF.read('category.txt', dim=1, gap='\t')
    return categorys
def generateLabel(set='train'):
    test_images=json.load(open(set+".json",'r'))
    category_mapping=getCategoryMapping()
    index=0
    for image_name in test_images:
        answer=[]
        for object_id in test_images[image_name]['objects']:
            tmp_answer=[str(category_mapping[test_images[image_name]['objects'][object_id]['category']])]
            tmp_line=test_images[image_name]['objects'][object_id]['bbox']
            tmp_answer.append('%.6f' % ((tmp_line[0]+tmp_line[2])/2/test_images[image_name]['width']))
            tmp_answer.append('%.6f' % ((tmp_line[1]+tmp_line[3])/2/test_images[image_name]['height']))
            tmp_answer.append('%.6f' % ((tmp_line[2]-tmp_line[0])/test_images[image_name]['width']))
            tmp_answer.append('%.6f' % ((tmp_line[3]-tmp_line[1])/test_images[image_name]['height']))
            answer.append(tmp_answer)
        RF.write('labels/'+set+'/'+image_name[:-3]+'txt',answer,dim=2,gap=' ')
        RF.write(set+'2017.txt','./images/'+set+'2017/'+image_name+'\n',dim=0,append=True)
        RI.progressBar(index,test_images.__len__())
        index+=1
def getCategories():
    test_images=json.load(open("val.json",'r'))
    category_mapping=[]
    for image_name in test_images:
        for object_id in test_images[image_name]['objects']:
            category = test_images[image_name]['objects'][object_id]['category']
            if category not in category_mapping:
                category_mapping.append(category)
    category_num=len(category_mapping)
    print(category_mapping)
    print("category num:",category_num)
    RF.write('category.txt',category_mapping,dim=1,gap='\t')
    print(category_mapping)
if __name__ == '__main__':
    file_list=file_name('test/exp5/labels')
    category_mapping=getCategoryList()
    answer=[]
    print(category_mapping)
    for file in file_list:
        imgfile=file[:-3]+'jpg'
        result=RF.read('test/exp5/labels/'+file,dim=2,gap=' ',ifFloat=True)
        result.pop(-1)
        tmp_line={}
        tmp_img=Image.open("my_coco/images/test2017/"+imgfile)
        tmp_line[imgfile]={}
        tmp_line[imgfile]["height"]=tmp_img.size[0]
        tmp_line[imgfile]["width"]=tmp_img.size[1]
        tmp_line[imgfile]["depth"]=3
        tmp_line[imgfile]["objects"]={}
        for i in range(result.__len__()):
            tmp_line[imgfile]["objects"][str(int(result[i][0]))]={}
            tmp_line[imgfile]["objects"][str(int(result[i][0]))]['category']=category_mapping[int(result[i][0])]
            result[i][1]*=tmp_img.size[0]
            result[i][2]*=tmp_img.size[1]
            result[i][3]*=tmp_img.size[0]
            result[i][4]*=tmp_img.size[1]
            trans_ans=[]
            trans_ans.append(int(result[i][1]-result[i][3]/2))
            trans_ans.append(int(result[i][2]+result[i][4]/2))
            trans_ans.append(int(result[i][1]+result[i][3]/2))
            trans_ans.append(int(result[i][2]-result[i][4]/2))
            tmp_line[imgfile]["objects"][str(int(result[i][0]))]['bbox'] = trans_ans
        RF.write('hehe.json',json.dumps(tmp_line)+',',dim=0,append=True)


        print(file)
        # print(item)
        # img = plt.imread("my_coco/images/test2017/"+str(item['image_id'])+'.jpg')  # 在这里读取图片
        # print(img.shape)
        # plt.imshow(img)  # 显示读取的图片
        # pylab.show()

    #     for object_id in test_images[image_name]['objects']:
    #         category = test_images[image_name]['objects'][object_id]['category']
    #         if category not in category_mapping:
    #             category_mapping.append(category)
    # category_num=len(category_mapping)
    # print(category_mapping)
    # print("category num:",category_num)
    # RF.write('category.txt',category_mapping,dim=1,gap='\t')
    # print(category_mapping)


