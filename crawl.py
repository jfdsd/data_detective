# -*- coding: utf-8 -*-
import requests     #网络请求模块
from urllib.request import urlretrieve      #直接远程下载图片
import shutil       #文件夹控制

import json
import re
import os

rankings_list=[]        #排行数据列表

class Crawl(object):

    #获取排行
    def get_rankings_json(self,url):
        self.jd_id_list=[]                  #京东ID列表
        self.name_list=[]                   #商品名称列表
        self.good_list=[]                   #好评率列表
        response=requests.get(url)          #发送网络请求，获取服务器响应
        json_str=str(response.json())       #将请求结果的json信息转化为字符串
        dict_json=eval(json_str)            #将json字符串信息转换为字典,方便信息提取
        jd_id_str=''

        #每次获取数据前，先将保存图片的文件夹清空，清空后再创建目录
        if os.path.exists('img_download'):  #判断img目录是否存在
            shutil.rmtree('img_download')   #删除img目录
            os.makedirs('img_download')     #创建img目录
        for index,i in enumerate(dict_json['products']):
            id=i['wareId']
            J_id='J_'+i['wareId']
            self.jd_id_list.append(id)
            name=i['wareName']
            self.name_list.append(name)
            good=i['goodRate']
            self.good_list.append(str(good)+'%')
            jd_id_str=jd_id_str+J_id+','
            if index<=10:
                imgPath='http://img11.360buyimg.com/n1/s320x320_'+i['imgPath']
                #下载图片到本地
                urlretrieve(imgPath,'img_download/'+str(index)+'.jpg')
        return jd_id_str

    #获取商品价格
    def get_price(self,id):
        rankings_list.clear()
        price_url='http://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
        response=requests.get(price_url.format(id_str=id))
        price=response.json()
        for index,item in enumerate(price):
            name=self.name_list[index]
            jd_price=item['p']
            jd_id=self.jd_id_list[index]
            good=self.good_list[index]
            rankings_list.append((index+1,name,jd_price,jd_id,good))
        return rankings_list


    #获取评价内容，score参数差评为1，中评为2，好评为3，0为全部
    def get_evaluation(self,score,id):
        #创建头部信息
        headers={'User-Agent':'OW64;rv:59.0)Gecko/20100101 Firefox/59.0'}
        params={
            'callback':'fetchJSON_comment98vv10635',
            'productId':id,
            'score':score,
            'sortType':6,
            'pageSize':10,
            'isShadowSku':0,
            'page':0,
        }
        url='https://club.jd.com/comment/skuProductPageComments.action'
        evaluation_response=requests.get(url,params=params,headers=headers)
        if evaluation_response.status_code==200:
            evaluation_response=evaluation_response.text
            try:
                t=re.search(r'({.*})',evaluation_response).group(0)

            except Exception as e:
                print("评价json数据匹配异常！")
            j=json.loads(t)
            commentSummary=j['comments']
            for comment in commentSummary:
                c_content=comment['content']
                c_time=comment['creationTime']
                c_name=comment['nickname']
                c_score=comment['score']
            if len(commentSummary)==0:
                return '无'
            else:
                return commentSummary[0]['creationTime']