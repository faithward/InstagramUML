import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    child = relationship("posts") 
    userPosts = Column(ARRAY(Integer, ForeignKey('posts.id')))
    child = relationship("bookmarks")
    markedPosts = Column(ARRAY(Integer, ForeignKey('bookmarks.id')))
    child = relationship("comments")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user = relationship("users")
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    child = relationship("bookmarks")
    child = relationship("likes")
    postLikes = Column(Integer, ForeignKey('likes.id'), nullable=False)
    child = relationship("medias")
    child = relationship("comments")
    postComments = Column(ARRAY(String, ForeignKey('comments.id')))

    def to_dict(self):
        return {}

class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    post = relationship("posts")
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("users")

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post = relationship("posts")
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("users")

class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    kind = Column(String(25), nullable=False)
    url = Column(String(150), nullable=False)
    post = relationship("posts")
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    post = relationship("posts")
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    user = relationship("users")
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e