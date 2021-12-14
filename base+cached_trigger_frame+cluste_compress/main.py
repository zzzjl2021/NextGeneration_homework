from cache_trigger_frame import *
from Compress_fuc import *
from PIL import Image
path='./shop/rgb_'
f=Image.open('./shop/rgb_1.png')
Width,height=f.size
size=Width*height
trigger_frame_index=cachetriggerframe(path,35,size/2)
total_memory = 0
for i in trigger_frame_index:
    info=[]
    info=Compress_Alth(path,i)
    total_memory = total_memory + info[1]
print(total_memory)