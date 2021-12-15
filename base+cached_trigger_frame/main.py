from cache_trigger_frame import *
from PIL import Image
import time
start_time = time.time()
path='./dataset/shop/rgb_'
f=Image.open('./dataset/shop/rgb_1.png')
Width,height=f.size
size=Width*height
trigger_frame_index=cachetriggerframe(path,35,size/2)
total_memory = 0
for i in trigger_frame_index:
    single_memory=os.path.getsize(path+str(i)+'.png')
    total_memory = total_memory + single_memory
print(total_memory)
print("--- %s seconds ---" % (time.time() - start_time))

#12195106
#--- 13.91174054145813 seconds ---