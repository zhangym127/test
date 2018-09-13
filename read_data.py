# coding= utf-8
import os
import cv2
import numpy as np

from trainTest.read_img import endwith

#输入一个文件路径，对其下的每个文件夹下的图片读取，并对每个文件夹给一个不同的Label
#返回一个img的list,返回一个对应label的list,返回一下有几个文件夹（有几种label)

def read_file(path):
    img_list = []
    label_list = []
    dir_counter = 0
    print("read_file:")

    #对路径下的所有子文件夹中的所有bmp文件进行读取并存入到一个list中
    for child_dir in os.listdir(path):
        child_path = os.path.join(path, child_dir)

        for dir_image in os.listdir(child_path):
            if endwith(dir_image,'png'):#图片格式jpg   bmp
                img = cv2.imread(os.path.join(child_path, dir_image),cv2.COLOR_BGR2GRAY)
                img.resize(241, 132)
                print("img:",img.shape)
                #img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                img_list.append(img)
                label_list.append(dir_counter)

        dir_counter += 1

    # 返回的img_list转成了 np.array的格式
    img_list = np.array(img_list)
    print("img_list:", img_list.shape)
    return img_list,label_list,dir_counter

#读取训练数据集的文件夹，把他们的名字返回给一个list
def read_name_list(path):
    name_list = []
    for child_dir in os.listdir(path):
        name_list.append(child_dir)
    return name_list



if __name__ == '__main__':
    img_list,label_lsit,counter = read_file('./train')

    print (counter)#文件夹个数
    print(label_lsit)#文件夹
    print(img_list)#照片

