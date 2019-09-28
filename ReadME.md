## 主要功能介绍及分析
### 功能介绍
1. 统计各书卷中出现词语的词频
2. 统计各书卷中出现词语的TF-IDF值
3. 统计占篇幅前80%的词语在圣经中首次出现的书卷名称
4. 统计各书卷的篇幅占比分布

### 功能分析
1. 由书卷中出现词语的词频，大致可看出该词语的重要性
2. 由书卷中出现词语的TF-IDF值，大致可看出该词语在该卷数的独特重要性
3. 由书卷的篇幅占比分布，可以大致看出该卷书在整本圣经中的重要性

## 具体代码功能介绍
1. [**book2filename.py**](book2filename.py)
  * **Function**: 抽取各书卷英文名称缩写
  * **Input**: 
    * [bible-book-names.txt](bible-book-names.txt)文件，包含中英文书卷名称及缩写
  * **Output**:
    * [OT-list.txt](OT-list.txt): 旧约英文书卷名缩写列表
    * [NT-list.txt](NT-list.txt): 新约英文书卷名缩写列表
    * [book2filename.txt](book2filename.txt): 新旧约英文书卷名缩写与文件命名的对应列表
2. [**stat_tf_by_book.py**](stat_tf_by_book.py)
  * **Function**: 统计各书卷中出现词语的词频
  * **Input**: 
    * [book2filename.txt](book2filename.txt): 新旧约英文书卷名缩写与文件命名的对应列表
    * [bible-hhb.txt](bible-hhb.txt): 和合本圣经
  * **Output**:
    * [bible-hhb-split.txt](bible-hhb-split.txt): 和合本圣经及分词结果
    * [output_file_tf](output_file_tf): 各书卷的词频统计结果
3. [**stat_tf_by_testament.py**](stat_tf_by_testament.py)
  * **Function**: 统计整本圣经、旧约圣经及新约圣经的词频
  * **Input**: 
    * [OT-list.txt](OT-list.txt): 旧约英文书卷名缩写列表
    * [NT-list.txt](NT-list.txt): 新约英文书卷名缩写列表
    * [bible-hhb.txt](bible-hhb.txt): 和合本圣经
  * **Output**:
    * [output_file_tf/holy_bible.txt](output_file_tf/holy_bible.txt): 整本圣经的词频统计
    * [output_file_tf/old_testament.txt](output_file_tf/old_testament.txt): 旧约圣经的词频统计
    * [output_file_tf/new_testament.txt](output_file_tf/new_testament.txt): 新约圣经的词频统计
4. [**stat_tfidf.py**](stat_tfidf.py)
  * **Function**: 统计各书卷中出现词语的TF-IDF值
  * **Input**: 
    * [output_file_tf](output_file_tf): 各书卷的词频统计结果
    * [book2filename.txt](book2filename.txt): 新旧约英文书卷名缩写与文件命名的对应列表
  * **Output**:
    * [output_file_tfidf](output_file_tfidf): 各书卷的反词频统计结果
5. [**appear_1st_time.py**](appear_1st_time.py)
  * **Function**: 统计占篇幅前80%的词语在圣经中首次出现的书卷名称
  * **Input**: 
    * [output_file_tf](output_file_tf): 各书卷的词频统计结果
    * [book2filename.txt](book2filename.txt): 新旧约英文书卷名缩写与文件命名的对应列表
  * **Output**:
    * [appear_1st_time.csv](appear_1st_time.csv): 占篇幅前80%的词语在圣经中首次出现的书卷名称
6. [**stat_word_by_book.py**](stat_word_by_book.py)
  * **Function**: 统计各书卷的篇幅占比分布
  * **Input**: 
    * [bible-book-names.txt](bible-book-names.txt)文件，包含中英文书卷名称及缩写
    * [OT-list.txt](OT-list.txt): 旧约英文书卷名缩写列表
    * [NT-list.txt](NT-list.txt): 新约英文书卷名缩写列表
    * [bible-hhb.txt](bible-hhb.txt): 和合本圣经
  * **Output**:
    * [圣经_书卷篇幅占比图.png](圣经_书卷篇幅占比图.png)
    * [圣经_书卷篇幅占比排序图.png](圣经_书卷篇幅占比排序图.png)
    * [proportion_rank.csv](proportion_rank.csv): 书卷篇幅占排序列表
    * [旧约_书卷篇幅占排序比图.png](旧约_书卷篇幅占排序比图.png)
    * [新约_书卷篇幅占排序比图.png](新约_书卷篇幅占排序比图.png)

书卷篇幅占排序列表，详见文件[proportion_rank.csv](proportion_rank.csv)

| 序号 | 书卷 | 字数 | 占比 |
| :----: | :----: | :----: | :----: |
| 1	| 诗篇 |	55535 |	5.96% |
| 2	| 耶利米书 | 51181 | 5.49% |
| 3	| 创世记 | 45191 | 4.85% |
| 4	| 以赛亚书 | 44306 | 4.76% |
| 5	| 以西结书 | 43385 | 4.66% |
| ...	| ... | ... | ... |

## 注意事项
1. UTF-8格式编码中行首可能会有一个不可见字符,可以转化为UTF-8无BOM格式编码再进行处理
2. 为使jieba分词能将圣经的人名、地名分出来，特别将它们定义为自定义的词典文件[user.dict](user.dict)
3. 由于圣经书卷不完全按时间顺序排列，因此词语在圣经中首次出现的书卷名称并不代表是最早出现的时间
4. 本项目的功能分析，仅供参考

## 参考资料
* 圣经人地名之人名(1153个): <http://www.godcom.net/rdm/r/>
* 圣经人地名之地名(1829个): <http://www.godcom.net/rdm/di/>
* 圣经中人物名字意义: <http://www.godcom.net/zhuti/81.htm>

## 书卷篇幅占比图
<div align=center><img width="1000" height="540" src="圣经_书卷篇幅占比图.png"/>
<div align=center><img width="1000" height="540" src="圣经_书卷篇幅占比排序图.png"/>
<div align=center><img width="1000" height="540" src="旧约_书卷篇幅占排序比图.png"/>
<div align=center><img width="1000" height="540" src="新约_书卷篇幅占排序比图.png"/>


-----
<p align="left"></p>
欢迎并感谢您提出宝贵的问题或建议: 点击[**【我要提问】**](https://github.com/guoshengkang/Bible-Word-Statistics/issues/new)