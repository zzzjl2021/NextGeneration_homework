import os
import cv2
import numpy as np
from PIL import Image
from scipy.cluster.vq import kmeans2
#输入：图像
#输出：size
def Compress_Alth(path,index):
    file_path=os.path.join(path+str(index)+'.png')
    img = cv2.imread(file_path)  # img.shape (720, 1280, 3)
    # cv2.imshow("Image", img)   
    # cv2.waitKey()
    img_reshape = img.reshape((-1,3))  # img_reshape.shape (921600, 3)
    #压缩 用3比特表示一种颜色
    n_cluster = 8  # 8=2^3
    centers, labels = kmeans2(img_reshape.astype(np.float), n_cluster, minit='points')
    compressed_img = np.asarray(labels)  #标签数组
    #解压
    recovered_img = []
    for i in compressed_img:
        recovered_img.append(centers[i])
    recovered_img = np.asarray(recovered_img,dtype='uint8').reshape(img.shape)
    # cv2.imshow('compressed_img',recovered_img)
    # cv2.waitKey()
    im = Image.fromarray(np.uint8(recovered_img[:,:,::-1]))
    path2=os.path.join('image_ys',os.path.basename(file_path).split('.')[0]+'re.png')
    im.save(path2)
    #图片大小
    img_size1=os.path.getsize(file_path)
    img_size2=os.path.getsize(path2)
    memory_saved=img_size1-img_size2
    compression_ratio=img_size1/img_size2
    return img_size1,img_size2,memory_saved,compression_ratio
# path = './shop/rgb_'
# trigger_frame_info=[]
# trigger_frame_info=Compress_Alth(path,10)
# print(trigger_frame_info)