from pymongo import MongoClient
client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# insert
# db.users.insert_one({'name':'bab', 'age':27})
# db.users.insert_one({'name':'john', 'age':20})
# db.users.insert_one({'name':'anny', 'age':21})

# select
# all_users = list(db.users.find({}, {'_id':False}))
# for user in all_users:
#     print(user)

# select one
# user = db.users.find_one({'name':'bab'}, {'_id':False})
# print(user)

# update one
# db.users.update_one({'name':'bab'}, {'$set':{'age':19}})

# delete one
db.users.delete_one({'name':'bab'})


