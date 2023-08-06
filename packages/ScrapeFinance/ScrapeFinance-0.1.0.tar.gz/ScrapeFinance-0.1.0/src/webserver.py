import json

import pymongo
from bson import json_util
from flask import Flask, render_template, jsonify

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.news1
collection = db.qqfinance2

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return '<h2>Welcome to Account Pool System</h2>'


@app.route('/qq')
def newsqq():
    print('查询新闻数据')
    result = collection.find()
    # for row in result:
    #     print(row['id'], row['content']['title'])
    return render_template('news.html', newsqqs=result)


@app.route('/api/news')
def newsqqapi():
    result = collection.find()
    data = []
    for item in result:
        data.append(item)
    # return jsonify(result)
    return json.dumps(data, default=json_util.default)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



