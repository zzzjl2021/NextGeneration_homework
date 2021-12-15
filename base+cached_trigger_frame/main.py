from cache_trigger_frame import *
from PIL import Image
import time
from client import *
start_time = time.time()
path='./dataset/shop/rgb_'
f=Image.open('./dataset/shop/rgb_1.png')
Width,height=f.size
size=Width*height
trigger_frame_index=cachetriggerframe(path,35,size/2)
print(trigger_frame_index)
total_memory = 0
for i in trigger_frame_index:
    single_memory=os.path.getsize(path+str(i)+'.png')
    total_memory = total_memory + single_memory
    sock_client_image(path+str(i)+'.png')
print(total_memory)
print("--- %s seconds ---" % (time.time() - start_time))

# 500张图片
# 11603894
# --- 8.418972253799438 seconds ---处理
# 11603894
# --- 9.425640106201172 seconds ---处理+发送

# 1500张
# 38535362
# --- 29.09647560119629 seconds ---处理
# 38535362
# --- 32.34994077682495 seconds ---处理+发送