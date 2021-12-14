ps:只聚类的话，时间会消耗太大，也没有必要
所以就分为3种情况：
	base,
	base+cached_trigger_frame,
	base+cached_trigger_frame+cluster_compress
这个视频是来自服装商店的监控，镜头不晃，更方便物体移动侦测，也符合所提算法的适用场景。
输入一共500张图片，选择出的触发帧能够很好的捕捉目标的移动状况，可以看result文件夹中的数据。

目前是计算每种情况的总传输字节大小，和程序运行时间：
base:
	#291372032
	# --- 0.023934125900268555 seconds ---
base+cached_trigger_frame:
	#12195106
	#--- 13.91174054145813 seconds ---
base+cached_trigger_frame+cluster_compress:
	#1613537
	# --- 23.467470169067383 seconds ---
可以看出压缩确实很大，运行时间倒不是问题，因为我们更在意传输时间。
至于传输时间，我还在写代码...