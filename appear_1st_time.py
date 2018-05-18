#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-14 10:31:25
# @Author  : ${guoshengkang} (${kangguosheng1@huokeyi.com})

import os
import re
from numpy import *
from jieba_cut import *

output_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'output_file_tf')
file_path0 = os.path.join(output_path, 'holy_bible.txt')
fin=open(file_path0,'r',encoding='UTF-8') #打开文件
keywords=[] #关键词
stats=[]	#出现次数
for line in fin:
	line=line.strip()
	rank,keyword,stat=line.split(',')
	keywords.append(keyword)
	stats.append(int(stat))

# 找到占篇幅前80%的关键词
arr=array(stats)
arr=arr/sum(arr)
arr=arr.cumsum() #累加
for index,x in enumerate(arr):
	if x >=0.8:
		num=index
		break
keywords_p80=keywords[:num+1] #需要统计第一次出现的关键词

appeared_dict=dict()
bible_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-hhb.txt')
fin=open(bible_path,'r',encoding='UTF-8')
for row,line in enumerate(fin): #row：0,1,2,3,...
	line=line.strip()
	Eng_abb,Ch_abb,chapter,scripture=re.split(r"\s+", line,3) #Gen 创 1:1 起初神创造天地。
	book_chapter=Ch_abb+chapter
	split_words=seg_sentence(scripture)
	keywords_split=split_words.split('|')
	for keyword in keywords_split:
		if (keyword in keywords_p80) and (keyword not in appeared_dict):
			appeared_dict[keyword]=book_chapter

# 将结果写入文件
fout_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'appear_1st_time.csv')
fout=open(fout_path,'w',encoding='UTF-8') #打开文件
for index,keyword in enumerate(keywords_p80):
	output_line='%d,%s,%d,%s'%(index+1,keyword,stats[index],appeared_dict[keyword])
	fout.write(output_line+'\n')
fout.close()