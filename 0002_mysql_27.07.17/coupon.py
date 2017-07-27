# -*- coding: utf-8 -*-
"""
Spyder Editor

第 0001 题：作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random

def Generate_Coupon(n):
    """
    生成200个10位激活码
    前9位为随机的数字或字母
    第10位为前面9位的ASCII码对10的膜
    数字0~9的ASCII码范围为48~57
    字母A~Z的ASCII码范围为65~90
    字母a~z的ASCII码范围为97~122
    """
    codes = []
    for j in range(n):
        code = []
        tail=0
        for i in range(9):
            j=random.randint(0,2)
            if j==0:
                a,b=48,57
            elif j==1:
                a,b=65,90
            elif j==2:
                a,b=97,122
            #chr(a) 将ASCII码/整数a转为一个字符
            code.append(chr(random.randint(a,b)))
            #ord(a) 将a转换为其ASCII码/整数
            tail += ord(code[i])
            #str(a) 将整数a转换为字符串
            #此处因为tail的范围为0到9,而0的ASCII码为48
            #亦可:tail = chr(tail%10 + 48)
        tail = str(tail%10)
        code.append(tail)
        #调用join方法连接一个列表里的所有元素
        #用""里的内容来连接，如果""里为空，就连成一个字符串
        code_ = "".join(code)
        codes.append(code_)
    f = open('codes.txt','w')
    j=0
    for i in range(len(codes)):
        j += 1
        f.write(codes[i]+"\t")
        if j%10==0:
            f.write("\n")
    f.close()
    return codes

def Check_Coupon(codes):
    """
    由code原理来检验code是否合格
    即最后一位数字（非ASCII码）等于前9位ASCII码和对10的膜
    """
    for i in range(len(codes)):
        code = codes[i]
        tail = 0
        for j in range(len(code)-1):
            tail += ord(code[j])
        tail = tail%10
        if int(code[len(code)-1]) == tail:
            print('Permission through')
        else:
            print('Permission denied')

if __name__ == "__main__":
    result = Generate_Coupon(200)
    Check_Coupon(result)
    for i in range(len(result)):
        print(result[i])
    