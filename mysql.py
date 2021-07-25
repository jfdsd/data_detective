# -*- coding: utf-8 -*-
import pymysql

class MySQL(object):

    #连接数据库
    def connection_sql(self):
        self.db=pymysql.connect(host="localhost",user="root",password="12345678f",db="jd_peripheral",port=3306,charset='utf8')
        return self.db

    #关闭数据库
    def close_sql(self):
        self.db.close()

    #排行数据插入方法，该方法可以根据更换表名插入排行数据
    def insert_ranking(self,cur,value,table):
        sql_insert="insert into {table} (id,name,jd_price,jd_id,good) "\
                   "values(%s,%s,%s,%s,%s) on duplicate "\
                   "key update name=values(name),jd_price=values(jd_price),"\
                   "jd_id=values(jd_id),good=values(good)".format(table=table)

        try:
            cur.executemany(sql_insert,value)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    #关注数据插入方法，该方法可以根据更换表名插入排行数据
    def insert_attention(self,cur,value,table):
        sql_insert="insert into {table} (name,jd_price,jd_id,good,middle_time,poor_time) " \
        "values(%s,%s,%s,%s,%s,%s)".format(table=table)

        try:
            cur.executemany(sql_insert,value)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    #查询排行数据表前10名的商品名称、价格、好评率
    def query_top10_info(self,cur):
        query_sql="select name,jd_price,good from jd_ranking where id<=10"
        cur.execute(query_sql)
        results=cur.fetchall()
        return results

    #根据id查询排行数据表数据内容
    def query_id_info(self,cur,id):
        query_sql="select name,jd_price,jd_id,good from jd_ranking where id={id}".format(id=id)
        cur.execute(query_sql)
        results=cur.fetchone()
        return results

    #查询关注商品的数据库表中是否有相同的商品名称
    def query_is_name(self,cur,name):
        query_sql="select count(*) from attention where name='{name}'".format(name=name)
        cur.execute(query_sql)
        results=cur.fetchall()
        return results[0][0]

    #查询商品排行信息
    def query_rankings(self,cur,table):
        query_sql="select id,name,jd_price,jd_id,good from {table}".format(table=table)
        cur.execute(query_sql)
        results=cur.fetchall()
        row=len(results)
        column=len(results[0])
        return row,column,results

    #查询排行榜所有商品名称
    def query_rankings_name(self,cur,table):
        name_all_list=[]
        query_sql="select name from {table}".format(table=table)
        cur.execute(query_sql)
        results=cur.fetchall()
        for r in results:
            name_all_list.append(r[0].replace(' ',''))
        return name_all_list

    #查询已经关注的商品信息
    def query_evaluate_info(self,cur,table):
        query_sql="select id,name,jd_price,jd_id,good,middle_time,poor_time from {table}".format(table=table)
        cur.execute(query_sql)
        results=cur.fetchall()
        if len(results)!=0:
            row=len(results)
            column=len(results[0])
            return row,column,results
        else:
            return 0,0,0

    #更新关注商品信息
    def update_attention(self,cur,table,column,id):
        sql_update="update {table} set {column} where id='{id}'".format(table=table,column=column,id=id)
        try:
            cur.execute(sql_update)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    #删除关注商品信息
    def delete_attention(self,cur,name):
        delete_sql="delete from attention where name='{name}'".format(name=name)
        try:
            cur.execute(delete_sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)



