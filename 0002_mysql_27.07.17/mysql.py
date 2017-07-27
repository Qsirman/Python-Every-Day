# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:04:18 2017

@author: claus
"""
import pymysql
import coupon

if __name__ == "__main__":
    coupon_code = coupon.Generate_Coupon(200)
    coupon_code = tuple(coupon_code)
    db = pymysql.connect("localhost","root","sml197421","coupon")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS COUPON")
    db.commit()
    cursor.execute("SELECT VERSION()")
    vid = cursor.fetchone()
    print("Database version : '%s'" % vid)
    sql = """CREATE TABLE COUPON(
    ID INT NOT NULL,
    CODE CHAR(10) NOT NULL)"""
    try:
        cursor.execute(sql)
    except:
        db.rollback()
    coupon_data=[]
    for i in range(len(coupon_code)):
        coupon_data.append([i+1,coupon_code[i]])
    cursor.executemany("INSERT INTO COUPON(ID,CODE) VALUES(%s,%s)",coupon_data)
    try:
        db.commit()
    except:
        db.rollback()
    db.close()