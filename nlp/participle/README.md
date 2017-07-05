
## jieba 中文处理

**1.基本分词函数与用法**
jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)

jieba.cut 方法接受三个输入参数:
* 需要分词的字符串
* cut_all 参数用来控制是否采用全模式
* HMM 参数用来控制是否使用 HMM 模型

jieba.cut_for_search 方法接受两个参数:
* 需要分词的字符串
* 是否使用 HMM 模型。

该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细.
