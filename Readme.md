# Readme

#### 1. 说明：

只聚类的话，时间会消耗太大，也没有必要
所以就分为3种情况：
	**base**,
	**base+cached_trigger_frame**,
	**base+cached_trigger_frame+cluster_compress**
这个视频是来自服装商店的监控，镜头不晃，更方便物体移动侦测，也符合所提算法的适用场景。
输入一共500张图片，选择出的触发帧能够很好的捕捉目标的移动状况。可以查看**base+cached_trigger_frame+cluster_compress**文件夹下的触发帧选择



####  2.实验结果 

|                     *500*张                     |     bytes      |          deal_time           |        transfer_time        |         total_time         |
| :---------------------------------------------: | :------------: | :--------------------------: | :-------------------------: | :------------------------: |
|                    **base**                     | 291372032bytes | 0.023934125900268555 seconds | 28.114162921905518 seconds  | 28.138097047805786 seconds |
|         **base+cached_trigger_frame**:          | 11603894bytes  |  8.418972253799438 seconds   | 1.0066678524017334 seconds  | 9.425640106201172 seconds  |
| **base+cached_trigger_frame+cluster_compress**: |  1550034bytes  |  16.530482292175293 seconds  | 0.12128210067749023 seconds | 16.651764392852783 seconds |

|                    *1500*张                     |     bytes      |          deal_time          |        transfer_time        |         total_time         |
| :---------------------------------------------: | :------------: | :-------------------------: | :-------------------------: | :------------------------: |
|                    **base**                     | 896018820bytes | 0.06983733177185059 seconds | 28.114162921905518 seconds  | 78.0328860282898  seconds  |
|         **base+cached_trigger_frame**:          | 38535362bytes  |  29.09647560119629 seconds  | 1.0066678524017334 seconds  | 32.34994077682495 seconds  |
| **base+cached_trigger_frame+cluster_compress**: |  5188045bytes  |  52.57721996307373 seconds  | 0.12128210067749023 seconds | 51.702720403671265 seconds |



