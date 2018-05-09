#!/usr/bin/python
# coding=utf-8
__author__ = 'guoshengkang'
import sys,os,re,string,time,json,gzip,random
import time
from jieba_cut import *

fout_path=os.path.join(os.path.split(os.path.realpath(__file__))[0], "book2filename.txt")
fout=open(fout_path,'w')
OT_path=os.path.join(os.path.split(os.path.realpath(__file__))[0], "OT-list.txt")
fout_OT=open(OT_path,'w')
NT_path=os.path.join(os.path.split(os.path.realpath(__file__))[0], "NT-list.txt")
fout_NT=open(NT_path,'w')

bible_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'bible-book-names.txt')
fin=open(bible_path,"r",encoding='UTF-8')
lines=fin.readline()
prefix=''
OT_num=0
NT_num=0
for line in fin:
  line=line.strip()
  if line==u'旧约':
    prefix='OT-';continue
  if line==u'新约':
    prefix='NT-';continue
  Ch_name,Ch_abb,Eng_name,Eng_abb=line.split(',')
  if prefix=='OT-':
    fout_OT.write(Eng_abb+'\n')
    OT_num+=1
    complete_prefix=prefix+"%02d"%(OT_num)+'_'
  else:
    fout_NT.write(Eng_abb+'\n')
    NT_num+=1
    complete_prefix=prefix+"%02d"%(NT_num)+'_'
  file_name=complete_prefix+Eng_name
  new_line=Eng_abb+','+file_name
  fout.write(new_line+'\n')
fin.close()
fout.close()
fout_OT.close()
fout_NT.close()
