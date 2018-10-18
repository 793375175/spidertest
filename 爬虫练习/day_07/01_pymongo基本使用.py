from pymongo import MongoClient


class PymongoTest(object):

    def __init__(self):
        # 链接数据
        self.client = MongoClient('127.0.0.1', 27017)
        # 获取要操作的集合
        self.col = self.client['py']['stu']

    def inser_one(self):

        self.col.insert_one({"name":"隔壁老王", "age":38, "gender":"男"})

    def inser_many(self):
        # 列表，字典
        datas = [{"name":"小三_{}".format(i), "age":18+i, "gender":"男"} for i in range(10)]
        self.col.insert_many(datas)

    def find_one(self):
        dic = self.col.find_one({"age":18})
        print(dic)
        print(type(dic))

    def find_many(self):
        cursor = self.col.find()
        for data in cursor:
            print(data)

    def update_one(self):
        self.col.update_one({"age":20},{"$set":{"age":18}})

    def update_many(self):
        self.col.update_many({"gender":"男"},{"$set":{"gender": "妖"}})

    def delete_one(self):
        self.col.delete_one({"gender":"妖"})

    def delete_many(self):
        self.col.delete_many({"gender":"妖"})

if __name__ == '__main__':
    pt = PymongoTest()

    # pt.inser_one()
    # pt.update_one()
    # pt.inser_many()
    # pt.find_one()
    # pt.update_many()
    # pt.delete_one()
    pt.delete_many()
    pt.find_many()