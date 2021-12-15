import time
from cache_trigger_frame import *
from Compress_fuc import *
from PIL import Image
from client import *
start_time = time.time()
path='./dataset/shop/rgb_'
f=Image.open('./dataset/shop/rgb_1.png')
Width,height=f.size
size=Width*height
trigger_frame_index=cachetriggerframe(path,35,size/2)
total_memory = 0
for i in trigger_frame_index:
    # print(i)
    info=[]
    info=Compress_Alth(path,i)
    total_memory = total_memory + info[1]
    path2=os.path.join('./base+cached_trigger_frame+cluster_compress/image_ys','rgb_'+ str(i) +'re.png')
    sock_client_image(path2)
print(total_memory)
print("--- %s seconds ---" % (time.time() - start_time))

# 500张
# 1550034
# --- 16.530482292175293 seconds ---
# 1530811
# --- 16.651764392852783 seconds ---

# 1500张
# 5188045
# --- 52.57721996307373 seconds ---
# 5168620
# --- 51.702720403671265 seconds ---
