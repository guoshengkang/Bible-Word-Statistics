#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-08 16:37:24
# @Author  : ${guoshengkang} (${kangguosheng1@huokeyi.com})

import sys,os,re,string,time,json,gzip,random
import datetime,time,re
from jieba_cut import *
from numpy import *
import numpy as np
import matplotlib.pylab as plt

starttime = datetime.datetime.now()    
#######################################################
def proportion(x,p):
  ordered=sorted(x,reverse = True) # 降序
  total=sum(x)
  cumadd=0
  for e in ordered:
    cumadd=cumadd+e
    if cumadd/total>=p: #占比
      return e

bible_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-book-names.txt')
fin=open(bible_path,"r",encoding='UTF-8')
lines=fin.readline()
prefix=''
OT_num=0
NT_num=0
Eng_abb2Eng_name=dict()
Eng_abb2Ch_name=dict()
for line in fin:
  line=line.strip()
  if line==u'旧约':
    prefix='OT-';continue
  if line==u'新约':
    prefix='NT-';continue
  Ch_name,Ch_abb,Eng_name,Eng_abb=line.split(',')
  Eng_abb2Eng_name[Eng_abb]=Eng_name
  Eng_abb2Ch_name[Eng_abb]=Ch_name

#旧约书名
old_testament_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'OT-list.txt')
old_testament=[]
with open(old_testament_path, "r",encoding='UTF-8') as fin:
  for line in fin.readlines():
    line=line.strip()
    old_testament.append(line)

#新约书名
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

flag=None
word_count=dict()
books_order=[]
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
    # print('processing book:',Eng_abb,(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
  new_line=re.sub('[，。！、？；“”]', "",scripture)
  word_num=len(new_line)
  word_count[Eng_abb]=word_count.get(Eng_abb,0)+word_num
  if Eng_abb not in books_order:
  	books_order.append(Eng_abb)

books   =[Eng_abb2Eng_name[book] for book in books_order]
word_num=[word_count[book] for book in books_order]
word_num=array(word_num)/sum(word_num)

sorted_dict=sorted(word_count.items(), key=lambda d:d[1], reverse = True ) #d[0]为key,d[1]为value,返回一个元组列表
order_books   =[Eng_abb2Eng_name[e[0]] for e in sorted_dict]
order_word_num=[e[1] for e in sorted_dict]
order_word_num=array(order_word_num)/sum(order_word_num)

old_books   =[Eng_abb2Eng_name[e[0]] for e in sorted_dict if e[0] in old_testament]
old_word_num=[e[1] for e in sorted_dict if e[0] in old_testament]
old_word_num=array(old_word_num)/sum(old_word_num)

new_books   =[Eng_abb2Eng_name[e[0]] for e in sorted_dict if e[0] in new_testament]
new_word_num=[e[1] for e in sorted_dict if e[0] in new_testament]
new_word_num=array(new_word_num)/sum(new_word_num)

fig = plt.figure(1)  
ax  = fig.add_subplot(111)  
all_x = range(len(word_num))
all_y = word_num*100
ax=plt.bar(all_x, all_y,tick_label=books)  
plt.xticks(all_x,rotation=80,fontsize=8)
plt.ylabel("%")
plt.title("Holy-Bible")
p80=np.percentile(all_y,80)#80%分位数
pm=np.median(all_y)
mean=np.mean(all_y)
p20=np.percentile(all_y,20)#20%分位数
plt.plot(all_x,len(word_num)*[p80],'^',color='lime',label='80%_quantile') 
plt.plot(all_x,len(word_num)*[pm],'D',color='lime',label='median') 
plt.plot(all_x,len(word_num)*[mean],'o',color='navy',label='mean') 
plt.plot(all_x,len(word_num)*[p20],'v',color='lime',label='20%_quantile')
prop80=proportion(all_y,0.8) 
plt.plot(all_x,len(word_num)*[prop80],'*',color='red',label='80%_proportion') 
for xx,yy in zip(all_x,all_y):
  plt.text(xx-0.6,yy+0.1,'%.1f'%yy) 
# 光滑曲线
plt.plot(all_x, all_y,'o-',color='coral',label='proportion')
plt.legend()
plt.show() 

fig = plt.figure(2)  
ax  = fig.add_subplot(111)  
order_all_x = range(len(order_word_num))
order_all_y = order_word_num*100
ax=plt.bar(range(len(order_word_num)), order_word_num*100,tick_label=order_books)  
plt.xticks(range(len(order_word_num)),rotation=80,fontsize=8)
plt.ylabel("%")
plt.title("Holy-Bible (ranked)")
p80=np.percentile(order_word_num*100,80)#80%分位数
pm=np.median(order_word_num*100)
mean=np.mean(order_word_num*100)
p20=np.percentile(order_word_num*100,20)#20%分位数
plt.plot(range(len(order_word_num)),len(order_word_num)*[p80],'^',color='lime',label='80%_quantile') 
plt.plot(range(len(order_word_num)),len(order_word_num)*[pm],'D',color='lime',label='median') 
plt.plot(range(len(order_word_num)),len(order_word_num)*[mean],'o',color='navy',label='mean') 
plt.plot(range(len(order_word_num)),len(order_word_num)*[p20],'v',color='lime',label='20%_quantile')
prop80=proportion(order_word_num*100,0.8) 
plt.plot(range(len(order_word_num)),len(order_word_num)*[prop80],'*',color='red',label='80%_proportion')
for xx,yy in zip(order_all_x,order_all_y):
  plt.text(xx-0.6,yy+0.1,'%.1f'%yy) 
# 光滑曲线
plt.plot(order_all_x, order_all_y,'o-',color='coral',label='proportion')
plt.legend()
plt.show() 

fig = plt.figure(3)  
ax  = fig.add_subplot(111)  
old_x = range(len(old_word_num))
old_y = old_word_num*100
ax=plt.bar(old_x, old_y,tick_label=old_books)  
plt.xticks(old_x,rotation=60)
plt.ylabel("%")
plt.title("Old_Testament")
p80=np.percentile(old_y,80)#80%分位数
pm=np.median(old_y)
mean=np.mean(old_y)
p20=np.percentile(old_y,20)#20%分位数
plt.plot(old_x,len(old_word_num)*[p80],'^',color='lime',label='80%_quantile') 
plt.plot(old_x,len(old_word_num)*[pm],'D',color='lime',label='median') 
plt.plot(old_x,len(old_word_num)*[mean],'o',color='navy',label='mean') 
plt.plot(old_x,len(old_word_num)*[p20],'v',color='lime',label='20%_quantile')
prop80=proportion(old_y,0.8) 
plt.plot(old_x,len(old_word_num)*[prop80],'*',color='red',label='80%_proportion')
for xx,yy in zip(old_x,old_y):
  plt.text(xx-0.3,yy+0.1,'%.1f'%yy) 
# 光滑曲线
plt.plot(old_x, old_y,'o-',color='coral',label='proportion')
plt.legend()
plt.show() 

fig = plt.figure(4)  
ax  = fig.add_subplot(111) 
new_x = range(len(new_word_num))
new_y = new_word_num*100
ax=plt.bar(new_x, new_y,tick_label=new_books)  
plt.xticks(range(len(new_word_num)),rotation=60)
plt.ylabel("%")
plt.title("New_Testament")
# 画出各分位数线
p80=np.percentile(new_y,80)#80%分位数
pm=np.median(new_y)
mean=np.mean(new_y)
plt.plot(new_x,len(new_word_num)*[p80],'^',color='lime',label='80%_quantile') 
plt.plot(new_x,len(new_word_num)*[pm],'D',color='lime',label='median') 
plt.plot(new_x,len(new_word_num)*[mean],'o',color='navy',label='mean') 
plt.plot(new_x,len(new_word_num)*[p20],'v',color='lime',label='20%_quantile')
prop80=proportion(new_word_num*100,0.8) 
plt.plot(new_x,len(new_word_num)*[prop80],'*',color='red',label='80%_proportion')
# 标记柱形的高度值
for xx,yy in zip(new_x,new_y):
  plt.text(xx-0.2,yy+0.1,'%.1f'%yy)
# 光滑曲线
plt.plot(new_x, new_y,'o-',color='coral',label='proportion')
plt.legend()
plt.show() 

file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'proportion.txt')
fout=open(file_path,'w',encoding='UTF-8') #打开文件
order_books   =[Eng_abb2Ch_name[e[0]] for e in sorted_dict]
order_word_num=[e[1] for e in sorted_dict]
order_word_num=array(order_word_num)/sum(order_word_num)*100
for index,book in enumerate(order_books):
	output_line='%s,%.2f%%'%(book,order_word_num[index])
	fout.write(output_line+'\n')
fout.close()
#####################################################
endtime = datetime.datetime.now()
print((endtime - starttime),"time used!!!") #0:00:00.280797