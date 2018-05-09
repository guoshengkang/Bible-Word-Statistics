#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os,sys
import string
import jieba

# jieba.add_word('路得')
jieba.load_userdict("user.dict")
#替换结巴词库
# dcit_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'my_dict.txt')
# jieba.set_dictionary(dcit_path)

# 如果有一些词语需要合并可以添加个人词典
# jieba.load_userdict('userdict.txt')
# 创建停用词列表
def creadstoplist(stopwordspath):
    stwlist = [line.strip() for line in open(stopwordspath, 'r',encoding='UTF-8').readlines()]
    return stwlist

# 对句子进行分词
def seg_sentence(sentence): #输入unicode编码字符串
    sentence=sentence.upper() #将字母统一换成大写
    wordList = jieba.cut(sentence, cut_all=True) ## 全模式
    #停用词文件由用户自己建立,注意路径必须和源文件放在一起
    stopwords_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'stopwords.txt')
    stwlist = creadstoplist(stopwords_path) #这里加载停用词的路径
    stwlist.extend(list(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+" "+'\t')) #添加英文标点符号
    keyword_list=[]
    digit_reg=r'^(\d+\.?\d*(?:L|ML|CM|MM|M|G|KG|V)?)$' #数字正则
    digit_reg=re.compile(digit_reg)
    for word in wordList:
        if word not in stwlist: #判断是否是停用词
            if len(word) > 1:  #不去掉长度为1的词
                is_digit=re.search(digit_reg,word) #判断关键词是否为数字
                if is_digit is None:
                    keyword_list.append(word)
            elif word==u'神':
                keyword_list.append(word)
            else:
                pass
    return '|'.join(keyword_list)

