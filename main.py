from pymongo import MongoClient

url = 'mongodb://qwe:qwe123@ds149593.mlab.com:49593/heroku_c31w8929?retryWrites=false'
client = MongoClient(url)

db = client['heroku_c31w8929']
collection = db['test']

# collection.insert_one({'a':'b'})
rows = collection.find({})
result = []
# collection.delete_many({'a':'b'})
for row in rows:
   if 'age' in row:
       if row['age'] > 21:
          result.append(row['age'])

max_age = max(result)

rows = collection.find()
max_age_result=[]
for row in rows:
   if 'age' in row:
       if row['age'] == max_age:
          max_age_result.append(row)
print (len(max_age_result))