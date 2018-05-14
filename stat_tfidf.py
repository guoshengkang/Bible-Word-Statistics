#!/usr/bin/python
# coding=utf-8
__author__ = 'guoshengkang'
import sys,os,re,string,time,json,gzip,random
import datetime,time,re
import math
from jieba_cut import *

starttime = datetime.datetime.now()    
#######################################################
def read_tf_file(filename,threshold):
  '''
  读取字频统计文件,计算该book中买个keyword的tf
  '''
  tmp_keywords=[]
  tmp_tf=dict()
  keyword_num=0
  output_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'output_file_tf')
  file_path=os.path.join(output_path, filename+'.txt')
  fin=open(file_path,"r",encoding='UTF-8')
  lines=fin.readlines()
  fin.close()
  for line in lines:
    line=line.strip()
    rank,keyword,tf_num=line.split(',')
    if int(tf_num)>=threshold:
      keyword_num+=int(tf_num)
      tmp_keywords.append(keyword)
      tmp_tf[keyword]=int(tf_num)
    else:
      break
  for keyword in tmp_tf:
    tmp_tf[keyword]=tmp_tf[keyword]/float(keyword_num)
  return tmp_keywords,tmp_tf

book2filename_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'book2filename.txt')
filenames=[] #所有的book列表
with open(book2filename_path, "r",encoding='UTF-8') as fin:
  for line in fin.readlines():
    line=line.strip()
    book,file_name=line.split(',')
    filenames.append(file_name)

book_tf=dict() #{book1:{k1:0.5,k2:0.4,...},book2:{},...}
book_keywords=dict() #{book1:[k1,k2,...],book2:[k1,k3,k4,...],...}
for filename in filenames:
  keywords,tf=read_tf_file(filename,2)
  book_keywords[filename]=keywords
  book_tf[filename]=tf
book_num=len(book_keywords)
print("there are %d books in Bible!!!"%book_num)

dictionary=[]
for book in book_keywords:
  dictionary.extend(book_keywords[book])
dictionary=set(dictionary)
print("there are %d keywords in dictionary!!!"%len(dictionary))

#计算每个keyword的idf
keyword_idf=dict()
for keyword in dictionary:
  accur_num=0 #keyword在book中出现的次数
  for book in book_keywords:
    if keyword in book_keywords[book]:
      accur_num+=1
  keyword_idf[keyword]=math.log(float(book_num)/(accur_num+1))

#计算每卷书中keyword的tf_idf
for filename in filenames:
  output_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'output_file_tfidf')
  file_path=os.path.join(output_path, filename+'.txt')
  fout=open(file_path,'w',encoding='UTF-8')
  keyword_tfidf=dict()
  for keyword in book_tf[filename]:
    keyword_tfidf[keyword]=book_tf[filename][keyword]*keyword_idf[keyword]
  sorted_dict=sorted(keyword_tfidf.items(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
  for index,(keyword,tfidf) in enumerate(sorted_dict):
    tmp_line='%d,%s,%.6f'%(index+1,keyword,tfidf)
    fout.write(tmp_line+'\n')
  fout.close() #关闭文件
#####################################################
endtime = datetime.datetime.now()
print((endtime - starttime),"time used!!!") #0:00:00.280797