from PIL import Image
import os
import time
start_time=time.time()
path='./dataset/shop/rgb_'
total_memory = 0
for i in range(499):
    a = i + 1
    path1=os.path.join(path+str(a)+'.png')
    img_size=os.path.getsize(path1)
    total_memory = total_memory + img_size
print(total_memory)
print("--- %s seconds ---" % (time.time() - start_time))
#291372032
# --- 0.023934125900268555 seconds ---