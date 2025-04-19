import pymongo
from config import getConfig

client = pymongo.MongoClient(getConfig().MONGO_URI.get_secret_value())
db = None

class VoiceLog:
    def __init__(self, user_id, channel_id, timestamp, action):
        self.user_id = user_id
        self.channel_id = channel_id
        self.timestamp = timestamp
        self.action = action

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "channel_id": self.channel_id,
            "timestamp": self.timestamp,
            "action": self.action
        }

class Reactions:
    def __init__(self, message_id, emoji, user, timestamp):
        self.message_id = message_id
        self.emoji = emoji
        self.user = user
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "emoji": self.emoji,
            "user": self.user,
            "timestamp": self.timestamp
        }

class Messages:
    def __init__(self, id, content, author, channel, timestamp):
        self.message_id = id
        self.content = content
        self.user_id = author
        self.channel_id = channel
        self.created_at = timestamp

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "content": self.content,
            "user_id": self.user_id,
            "channel_id": self.channel_id,
            "created_at": self.created_at,
        }

def init_db():
    global db
    database = getConfig().MONGO_DB_NAME.get_secret_value()
    if database in client.list_database_names():
        db = client[database]
        
    else:
        print("ERROR: Database does not exist.")
        exit(1)
        
def get_messages_collection():
    global db
    if db is None:
        init_db()
        
    if "messages" in db.list_collection_names():
        collection = db["messages"]
    else:
        print("Collection 'messages' does not exist. Creating a new collection.")
        collection = db.create_collection("messages")
        collection.create_index("message_id", unique=True)
        
    return collection
    
def get_reactions_collection():
    global db
    if db is None:
        init_db()
        
    if "reactions" in db.list_collection_names():
        collection = db["reactions"]
    else:
        print("Collection 'reactions' does not exist. Creating a new collection.")
        db.create_collection("reactions")
        collection = db["reactions"]
        collection.create_index([("message_id", 1), ("emoji", 1), ("user", 1)], unique=True)
        
    return collection
    
def get_voice_logs_collection():
    global db
    if db is None:
        init_db()
        
    if "voicelogs" in db.list_collection_names():
        collection = db["voicelogs"]
    else:
        print("Collection 'voicelogs' does not exist. Creating a new collection.")
        db.create_collection("voicelogs")
        collection = db["voicelogs"]
        collection.create_index([("user_id", 1), ("channel_id", 1)], unique=True)
    
    return collection
    
def new_voice_log(voice_log):
    try:
        collection = get_voice_logs_collection()
        collection.insert_one(voice_log.to_dict())
    except Exception as e:
        pass
    
def new_reaction(reaction):
    try:
        collection = get_reactions_collection()
        collection.insert_one(reaction.to_dict())
    except Exception as e:
        pass

def new_message(message):
    try:
        collection = get_messages_collection()
        collection.insert_one(message.to_dict())
    except Exception as e:
        pass