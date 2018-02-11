★★★圣经和合本词语统计项目★★★
工作内容如下:
1.统计<<圣经和合本>>中整本圣经、旧约、新约以及各书卷中词语出现的次数
结果见output_file_tf文件夹

2.统计<<圣经和合本>>中相对整本圣经而言词语在各书卷中的重要性
结果见output_file_tfidf文件夹

文件说明:
◎圣经中文和合本.txt
bible-hhb.txt -- 处理不可见字符后的和合本中文圣经
bible-hhb-split.txt -- 和合本中文圣经及结巴分词结果
注: UTF-8格式编码中行首可能会有一个不可见字符,可以转化为UTF-8无BOM格式编码再进行处理

◎圣经中各书卷的中英文名称及缩写
bible-book-names.txt

◎output_file_tf和output_file_tfidf文件夹中的文件名称和书卷名臣英文缩写的对应关系
book2filename.txt

◎书卷列表
OT-list.txt -- 旧约书卷列表
NT-list.txt -- 新约书卷列表

◎自定义的词典:user.dict
圣经人地名之人名(1153个),参照http://www.godcom.net/rdm/r/
圣经人地名之地名(1829个),参照http://www.godcom.net/rdm/di/

◎圣经中人物名字意义,参照http://www.godcom.net/zhuti/81.htm
