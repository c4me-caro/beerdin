import pymongo
from config import getConfig

client = pymongo.MongoClient(getConfig().MONGO_URI.get_secret_value())
db = None

class Reactions:
    def __init__(self, emoji, count, users):
        self.emoji = emoji
        self.count = count
        self.users = users

    def to_dict(self):
        return {
            "emoji": self.emoji,
            "count": self.count,
            "users": self.users
        }

class Messages:
    def __init__(self, id, content, author, channel, timestamp, reactions):
        self.message_id = id
        self.content = content
        self.user_id = author
        self.channel_id = channel
        self.created_at = timestamp
        self.reactions = reactions

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "content": self.content,
            "user_id": self.user_id,
            "channel_id": self.channel_id,
            "created_at": self.created_at,
            "reactions": [reaction.to_dict() for reaction in self.reactions],
        }

def init_db():
    global db
    database = getConfig().MONGO_DB_NAME.get_secret_value()
    if database in client.list_database_names():
        db = client[database]
        
    else:
        print(f"Database '{database}' does not exist. Creating a new database.")
        exit(1)
        
def get_messages_collection():
    global db
    if db is None:
        init_db()
        
    if "messages" in db.list_collection_names():
        return db["messages"]
    else:
        print("Collection 'messages' does not exist. Creating a new collection.")
        db.create_collection("messages")
        return db["messages"]

def new_message(message):
    collection = get_messages_collection()
    collection.insert_one(message.to_dict())