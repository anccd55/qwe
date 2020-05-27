from pymongo import MongoClient

url = 'mongodb://qwe:qwe123@ds149593.mlab.com:49593/heroku_c31w8929?retryWrites=false'
client = MongoClient(url)

db = client['heroku_c31w8929']
collection = db['test']

collection.insert_one({'a':'b'})

rows = collection.find({})
for row in rows:
  print(row)