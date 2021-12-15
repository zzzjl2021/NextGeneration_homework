from PIL import Image
import os
import time
from client import *
start_time=time.time()
path='./dataset/shop/rgb_'
total_memory = 0
for i in range(1499):
    a = i + 1
    path1=os.path.join(path+str(a)+'.png')
    img_size=os.path.getsize(path1)
    sock_client_image(path1)
    total_memory = total_memory + img_size
print(total_memory)
print("--- %s seconds ---" % (time.time() - start_time))

# 500张
#291372032
# --- 0.023934125900268555 seconds ---
# 291372032
# --- 28.138097047805786 seconds ---

# 1500张
# 896018820
# --- 0.06983733177185059 seconds ---
# 896018820
# --- 78.0328860282898 seconds ---