# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:01:07 2017

@author: claus
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

原理：除了_`'外的其他符号，空格以及换行符都看成是有一个新字符的标志
Bug：但没有解决如果最后一个字符忘记加标点符号的情况
"""
signs = []
def signs_append(a,b):
    for i in range(a,b):
        signs.append(i)

def words_count(f):
    signs_append(32,39)
    signs_append(40,48)
    signs_append(58,65)
    signs_append(91,95)
    signs_append(123,127)
    a=f.read()
    count=0
    for i in range(len(a)):
        if (i!=len(a)-1):
            if(ord(a[i]) in signs and ord(a[i+1]) != '\n') or (ord(a[i]) not in signs and a[i+1] == '\n') :
                print(a[i])
                count += 1
        else:
            print(i)
            if (ord(a[i]) in signs) or (a[i]=='\n'):
                print(a[i])
                count +=1
    return count

if __name__=="__main__":
    f = open('test.txt','r')
    print(words_count(f))
    f.close()