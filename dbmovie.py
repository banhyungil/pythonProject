from pymongo import MongoClient
client = MongoClient('mongodb+srv://banhyungil:qudduqdl1!@cluster0.umvvk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


# movies = list(db.movies.find({}, {'_id':False}))
# for movie in movies:
#     print(movie)

g_movie = db.movies.find_one({'title':'가버나움'}, {'_id':False})
star = g_movie['star']

movies = list(db.movies.find({'star':star}, {'_id':False}))

for m in movies:
    print(m['title'])

doc = {'title':'가버나움'}
result = db.movies.update_one(doc, {'$set':{'star':'0'}})
print(db.movies.find_one(doc))

