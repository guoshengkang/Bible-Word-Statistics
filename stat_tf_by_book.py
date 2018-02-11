#!/usr/bin/python
# coding=utf-8
__author__ = 'guoshengkang'
import sys,os,re,string,time,json,gzip,random
import datetime,time,re
from jieba_cut import *
reload(sys)
sys.setdefaultencoding('utf8')
starttime = datetime.datetime.now()    
#######################################################
book2filename_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'book2filename.txt')
book2filename=dict()
with open(book2filename_path, "r") as fin:
  for line in fin.readlines():
    line=unicode(line.strip(), "utf-8")
    book,file_name=line.split(unicode(',','utf-8'))
    book2filename[book]=file_name
bible_split_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-hhb-split.txt')
fout_bible=open(bible_split_path,'w') #打开文件
bible_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-hhb.txt')
fin=open(bible_path)
lines=fin.readlines()
fin.close()
row_num=len(lines) #文件的行数
print "There are %d lines in the input file!!!"%row_num
flag=None
output_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'output_file_tf')
file_path=None
for row,line in enumerate(lines): #row：0,1,2,3,...
  line=unicode(line.strip(),'utf-8')
  keyword_list=re.split(r"\s+", line,3) #Gen 创 1:1 起初神创造天地。
  if len(keyword_list)==4:
    Eng_abb=keyword_list[0];scripture=keyword_list[3]
  else:
    print "length of line:(%s) is not 4 !!!"%line
    continue
  if Eng_abb!=flag: #进入新的书卷
    print 'processing book:',Eng_abb,(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    flag=Eng_abb
    if file_path: #将字典写入文件
      sorted_dict=sorted(keyword2num.iteritems(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
      fout_stat=open(file_path,'w') #打开文件
      for keyword,number in sorted_dict:
        tmp_line=','.join([keyword,str(number)])
        fout_stat.write(tmp_line.encode('utf-8')+'\n')
      fout_stat.close() #关闭文件
    keyword2num=dict() #字典初始化为{}
    file_path = os.path.join(output_path, book2filename[flag]+'.txt')
    print file_path
  split_words=seg_sentence(scripture)
  split_line=line+'-->'+split_words
  fout_bible.write(split_line.encode('utf-8')+'\n')
  keywords=split_words.split(unicode('|','utf-8'))
  for keyword in keywords:
    keyword2num[keyword]=keyword2num.get(keyword,0)+1

if file_path: #将最后一个字典写入文件
  sorted_dict=sorted(keyword2num.iteritems(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
  fout_stat=open(file_path,'w') #打开文件
  for keyword,number in sorted_dict:
    tmp_line=','.join([keyword,str(number)])
    fout_stat.write(tmp_line.encode('utf-8')+'\n')
  fout_stat.close() #关闭文件

fout_bible.close()
#####################################################
endtime = datetime.datetime.now()
print (endtime - starttime),"time used!!!" #0:00:00.280797