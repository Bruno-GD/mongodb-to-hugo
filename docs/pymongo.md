# [PyMongo](https://docs.mongodb.com/drivers/python/)

## [PyMongo setup](https://pymongo.readthedocs.io/en/stable/installation.html)
```cli
python -m pip install pymongo
```

## [Connection to MongoAtlas](https://pymongo.readthedocs.io/en/stable/tutorial.html#making-a-connection-with-mongoclient)
```py
from pymongo import MongoClient # import MongoClient
client = MongoClient('mongodb://localhost:27017/')  # start instance of client
```
## [Getting a database](https://pymongo.readthedocs.io/en/stable/tutorial.html#getting-a-database)
```py
db = client.test_database       # select the databse and get an instance of it
db = client['test-database']    # same as above
```
## [Getting a collection](https://pymongo.readthedocs.io/en/stable/tutorial.html#getting-a-collection)
```py
collection = db.test_collection     # select the collection from database
                                    # and get an instance of it

collection = db['test-collection']  # same as above
```
## [Insert new document](https://pymongo.readthedocs.io/en/stable/tutorial.html#inserting-a-document)
```py
posts = db.posts                # get collection instance
post = posts.insert_one(post)   # insert_one method and return {data} from insert
post_id = post.inserted_id      # get the 'inserted_id' from last insert
```
## [Get single document](https://pymongo.readthedocs.io/en/stable/tutorial.html#getting-a-single-document-with-find-one)
```py
>>> posts.find_one()                # using previous collection instance
{ u'_id': ObjectId('...'),
 u'author': u'Mike',
 u'date': datetime.datetime(...),
 u'tags': [u'mongodb', u'python', u'pymongo'],
 u'text': u'My first blog post!'}
```
## [Get document by _id](https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-by-objectid)
```py
>>> post_id
ObjectId(...)
>>> posts.find_one({"_id": post_id}) # using previous collection instance
```
```py
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
```
## [Get more than one document](https://pymongo.readthedocs.io/en/stable/tutorial.html#querying-for-more-than-one-document)
```py
for post in posts.find():
    ...
```
## [Count documents](https://pymongo.readthedocs.io/en/stable/tutorial.html#counting)
```py
posts.count_documents({})
posts.count_documents({"author": "Mike"})
```
