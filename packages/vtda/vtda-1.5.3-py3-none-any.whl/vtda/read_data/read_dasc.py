# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:35:25 2023

@author: DELL
"""
import pandas as pd 
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
import datetime
import struct
import os
import re
import math
from vtda.util.util import fix_num
#解决中文乱码问题
plt.rcParams["font.sans-serif"]='SimHei'
#解决负号无法正常显示问题
plt.rcParams["axes.unicode_minus"]= False


        
def read_dasc_data(dir_=os.getcwd(),tongdao='all',source='jiliuhuan'):
    pass
    os.chdir(dir_) 
    name_=os.listdir() #列出所有文件  
    name_=[s for s in name_ if s[0] in ['A','1','K','V']] #选出 只是数据的文件名
    name_1=[]
    ls=['index','.']
    for i in name_:
        pass
        if 'index' in i:
            pass
        else:
            name_1.append(i)
    for i in name_1:
        pass
        if '.' in i:
            name_1.remove(i)    
        else:
            pass
    name_2={}
    for i in name_1:
        pass
        try:
            name_2[str(int(i.split('_')[1]))]=i
        except:
            name_2[i.split('_')[0]]=i           
    res={}
    if tongdao=='all':
        name_=list(name_2.keys())
    else:
        name_=fix_num(tongdao)        
        
    for i in name_:
        pass
        if source=='jiliuhuan':
            res[i]=read_single_data(data_file=dir_+'/'+name_2[i])    
        else:
            res[i]=read_single_data_yaoce(data_file=dir_+'/'+name_2[i]) 
            

    res_duanhao=read_single_data_yaoce(dir_+'/1_01_index')
    zongduanshu=0
    res_duanhao_=[]
    for i in range(len(res_duanhao)):
        pass
        if (i % 2) == 1: #i为单数 但是在list中双数的位置
            zongduanshu+=res_duanhao[i] 
            res_duanhao_.append(res_duanhao[i])
    caiyangpinlv=len(res[list(res.keys())[0]])/zongduanshu
    
    res_duanhao__={}
    for i in range(len(res_duanhao_)):
        if i==0:
            res_duanhao__[i]=[0,res_duanhao_[i]*caiyangpinlv]
        else: 
            res_duanhao_[i]=round(res_duanhao_[i-1]+res_duanhao_[i],2)
            res_duanhao__[i]=[res_duanhao_[i-1]*caiyangpinlv,res_duanhao_[i]*caiyangpinlv]

    res_={}
    for i in  res_duanhao__:
        pass
        res_[str(i)]={}
        for j in res:
            pass
            res_[str(i)][j]=res[j][int(res_duanhao__[i][0]):int(res_duanhao__[i][1])]

    res_info={}
    for i in range(len(res_duanhao_)):
        pass
        res_info[str(i)]={'采集时间':datetime.datetime.fromtimestamp(res_duanhao[i*2]).strftime('%Y-%m-%d %H:%M:%S'),
                    '采样时长':res_duanhao_[i],
                     '采样频率':caiyangpinlv}        
    return res_,res_info

def read_single_data(data_file):
    pass

    data_file = open(data_file, 'rb')    
    data_temp = data_file.read()
    a=struct.pack('<f', 0.000000019)
    res=[]
    n=4
    int(len(data_temp)/n)
    for i in range(int(len(data_temp)/n)):
        s=data_temp[i*n:i*n+n]
        data_short, = struct.unpack('<f', s)
        res.append(data_short)
    return np.array(res).astype(float)

def read_single_data_yaoce(data_file):
    pass

    data_file = open(data_file, 'rb')    
    data_temp = data_file.read()
    res=[]
    n=8
    int(len(data_temp)/n)
    for i in range(int(len(data_temp)/n)):
        s=data_temp[i*n:i*n+n]
        data_short, = struct.unpack('<d', s)
        res.append(data_short)
    return np.array(res).astype(float)

#data=read_data(dir_=dir_,tongdao='1')        

def write_to_stp(data_file,res):
    pass
    f = open(data_file, 'w')
    f.write(res)
    f.close()    

def write_to_sts(data_file,res):
    pass

    for i in res:
        pass
        try:
            res1+=struct.pack('<f', i)
        except: 
            res1=struct.pack('<f', i)
    
    f = open(data_file, 'wb')
    f.write(res1)
    f.close()
    

def write_to_cgdlx(dir_,data_,info_,duiying,shiyanming='transform',shiyanhao=1):
    pass
    ii=0
    for i in data_:
        pass
        ii+=1
        write_to_sts(dir_+f'/{shiyanming}_{str(shiyanhao)}#{ii}.sts',data_[i])
        res=f'{ii},{duiying[i]},με,0.05,1,10,ICP,2023-04-05 00:00:44,2000,30596,1' 
        write_to_stp(dir_+f'/{shiyanming}_{str(shiyanhao)}#{ii}.tsp',res)

if __name__ == '__main__':

    #dir_=r'E:\城轨中心\1科研\2所基金\2021ZXJ003城市轨道交通遥测轮轨力采集系统研发\机辆所软件及数据\轮轨力数据\19号线集流环\集流环20230209\1_01_index'
    dir_=r'E:\城轨中心\1科研\2所基金\2021ZXJ003城市轨道交通遥测轮轨力采集系统研发\机辆所软件及数据\轮轨力数据\19号线集流环\集流环20230317'
    dir_=dir_.replace('\\', '/')
    data,info=read_dasc_data(dir_=dir_,tongdao='1-3')
    
