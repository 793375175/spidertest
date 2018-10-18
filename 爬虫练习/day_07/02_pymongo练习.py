from pymongo import MongoClient

"""
使用python向集合t3中插入1000条文档,文档包含_id和name
id的值为0,1,2,3,...999
name的值为py0,py2,....
查询显示出_id为100整数的倍数的文档, 如100,200,30
"""

from datetime import datetime

class MongoTest(object):

    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.col = self.client['py']['t6']

    def insert_data(self):
        datas = [{"_id":i, "name":"py{}".format(i)} for i in range(1000)]
        # 如果参数是一个字典就插入一条数据, 如果参数是一个列表, 插入多条数据
        self.col.insert(datas)

    def show_data(self):
        """查询显示出_id为100整数的倍数的文档, 如100,200,30"""
        # 自定查询条件
        cursor = self.col.find({"$where": "function(){ return this._id % 100 == 0 && this._id != 0; }"})
        for data in cursor:
            print(data)

    def show_data2(self):
        """先查询所有数据, 然后在使用python来过滤"""
        cursor = self.col.find()
        for data in cursor:
            if data['_id'] % 100 == 0 and data['_id'] != 0:
                print(data)


if __name__ == '__main__':
    mt = MongoTest()
    # mt.insert_data()
    start = datetime.now()
    # mt.show_data() # 0.069896
    mt.show_data2() # :0.005891
    end = datetime.now()
    print("花费时间:{}".format((end-start).total_seconds()))