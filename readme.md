训练word2vec字向量所用。
语料可以从[wiki_zh](https://pan.baidu.com/s/1uPMlIY3vhusdnhAge318TA)下载

使用工具为gensim。

经验:

对于较大量文本一定要使用gensim的语料加载工具。
即使是一个1MB文件也会产生巨大的语料文件。
当然，如果有TB级内存也可以直接使用gensim运行。
否则，可以享受一下蓝屏的快感。