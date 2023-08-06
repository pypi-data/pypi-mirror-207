import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.news1
collection = db.qqfinance2

#因为我们没有mongodb的桌面终端，所以自己写一个查询mongodb库的方法，来确认一下是否写入数据成功
print('查询多条数据')
# result = collection.find({'name':'小明'})
result = collection.find()

# print(result)
for row in result:
    # print(row['id'],row['title'],row['publish_time'],row['link_info'].get('share_url'))
    print(row['id'],row['content']['title'])
