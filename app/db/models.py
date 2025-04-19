from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from config import getConfig

Base = declarative_base()
SessionLocal = None

class Users(Base):
    __tablename__ = 'users' 
    id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    
class UserRoles(Base):
    __tablename__ = 'user_roles' 
    user_id = Column(String, primary_key=True)
    role_id = Column(String, primary_key=True)
    
class Roles(Base):
    __tablename__ = 'roles' 
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    
class UserChannels(Base):
    __tablename__ = 'user_channels' 
    user_id = Column(String, primary_key=True)
    channel_id = Column(String, primary_key=True)

class Channels(Base):
    __tablename__ = 'channels' 
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

class Message(Base):
    __tablename__ = 'messages' 
    id = Column(String, primary_key=True)
    content = Column(String, nullable=False) 
    user_id = Column(String, nullable=False) 
    channel_id = Column(String, nullable=False)
    created_at = Column(String, nullable=False)  
    
class MessageReactions(Base):
    __tablename__ = 'message_reactions' 
    message_id = Column(String, primary_key=True)
    reaction_id = Column(String, primary_key=True)
    
class Reactions(Base):
  __tablename__ = 'reactions'
  id = Column(String, primary_key=True)
  emoji = Column(String, nullable=False)

def init_db():
    try:    
        DATABASE_URL = getConfig().DB_CONNECTION.get_secret_value()
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(bind=engine)
        
        global SessionLocal
        SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
    except Exception as e:
        print(f"Error initializing database: {e}")
        exit(1)
    
def get_session():
    global SessionLocal
    return SessionLocal