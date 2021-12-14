from genericpath import getsize
from PIL import Image
import numpy as np
import os
from Compress_fuc import *
# input:threshold1 and threshold2 
# function:compute the trigger frame 
# output:return the index of picture needed to be sent
def cachetriggerframe(path,threshold1,threshold2):
    trigger_frame_index=[]
    for i in range(498):
        a=i+1
        b=a+1
        path1=os.path.join(path + str(a) + '.png' )
        path2=os.path.join(path + str(b) + '.png' )
        img1=Image.open(path1,'r').convert('L')
        img2=Image.open(path2,'r').convert('L')

        mats1 = np.array(img1)
        mats2 = np.array(img2)
        differ=mats2-mats1    
        mask=differ>35
        sum=np.sum(mask!=0)
        # Image.fromarray(differ).show() #查看帧差图像
        if sum > threshold2:
            trigger_frame_index.append(b)
            # img2.show()
    return trigger_frame_index


# print("The index of frames needed to be trigger:",trigger_frame_index)
# for i in trigger_frame:
    # info=[]
    # info=Compress_Alth(path,i)
    # print(info)