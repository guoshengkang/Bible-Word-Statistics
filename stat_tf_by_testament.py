#!/usr/bin/python
# coding=utf-8
__author__ = 'guoshengkang'
import sys,os,re,string,time,json,gzip,random
import datetime,time,re
from jieba_cut import *

starttime = datetime.datetime.now()    
#######################################################
old_testament_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'OT-list.txt')
old_testament=[]
with open(old_testament_path, "r",encoding='UTF-8') as fin:
  for line in fin.readlines():
    line=line.strip()
    old_testament.append(line)
new_testament_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'NT-list.txt')
new_testament=[]
with open(new_testament_path, "r",encoding='UTF-8') as fin:
  for line in fin.readlines():
    line=line.strip()
    new_testament.append(line)

bible_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-hhb.txt')
fin=open(bible_path,'r',encoding='UTF-8')
lines=fin.readlines()
fin.close()
row_num=len(lines) #文件的行数
print("There are %d lines in the input file!!!"%row_num)

output_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'output_file_tf')
file_path0 = os.path.join(output_path, 'holy_bible.txt')
file_path1 = os.path.join(output_path, 'old_testament.txt')
file_path2 = os.path.join(output_path, 'new_testament.txt')
fout0=open(file_path0,'w',encoding='UTF-8') #打开文件
fout1=open(file_path1,'w',encoding='UTF-8') #打开文件
fout2=open(file_path2,'w',encoding='UTF-8') #打开文件
keyword2num0=dict() #字典初始化为{}
keyword2num1=dict() #字典初始化为{}
keyword2num2=dict() #字典初始化为{}

flag=None
for row,line in enumerate(lines): #row：0,1,2,3,...
  line=line.strip()
  keyword_list=re.split(r"\s+", line,3) #Gen 创 1:1 起初神创造天地。
  if len(keyword_list)==4:
    Eng_abb=keyword_list[0];scripture=keyword_list[3]
  else:
    print("length of line:(%s) is not 4 !!!"%line)
    continue
  if Eng_abb!=flag: #进入新的书卷
    flag=Eng_abb
    print('processing book:',Eng_abb,(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
  split_words=seg_sentence(scripture)
  keywords=split_words.split('|')
  for keyword in keywords:
    keyword2num0[keyword]=keyword2num0.get(keyword,0)+1
  if Eng_abb in old_testament:
    for keyword in keywords:
      keyword2num1[keyword]=keyword2num1.get(keyword,0)+1
  if Eng_abb in new_testament:
    for keyword in keywords:
      keyword2num2[keyword]=keyword2num2.get(keyword,0)+1

#将3个字典分别排序,并写入文件
sorted_dict=sorted(keyword2num0.items(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
for index,(keyword,number) in enumerate(sorted_dict):
  tmp_line='%d,%s,%d'%(index+1,keyword,number)
  fout0.write(tmp_line+'\n')
fout0.close() #关闭文件

sorted_dict=sorted(keyword2num1.items(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
for index,(keyword,number) in enumerate(sorted_dict):
  tmp_line='%d,%s,%d'%(index+1,keyword,number)
  fout1.write(tmp_line+'\n')
fout1.close() #关闭文件

sorted_dict=sorted(keyword2num2.items(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
for index,(keyword,number) in enumerate(sorted_dict):
  tmp_line='%d,%s,%d'%(index+1,keyword,number)
  fout2.write(tmp_line+'\n')
fout2.close() #关闭文件
#####################################################
endtime = datetime.datetime.now()
print((endtime - starttime),"time used!!!") #0:00:00.280797