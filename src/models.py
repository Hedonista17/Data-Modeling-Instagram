import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__='followers'

    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer)
    following_id = Column(Integer)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    password= Column(String(50), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname= Column(String(30), nullable=False)
    register_date=Column(String(250), nullable=False)
    email=Column(String(250), nullable=False,unique=True)
    followers_id = Column(Integer, ForeignKey('Followers.followers_id'))
    followers = relationship(Followers)
    following_id = Column(Integer, ForeignKey('Followers.following_id'))
    following = relationship(Followers)


class Publicaciones(Base):
    __tablename__ = 'publicacion'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)
    likes= Column(Integer)
    post=  Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    publicaciones = relationship(User)

class Compartir(Base):
    __tablename__ = 'compartir'
    
    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    media =  Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('publicacion.id'))
    compartir = relationship(Publicaciones)

class Favoritos(Base):
    __tablename__='favorito'

    id = Column(Integer, primary_key=True)
    post_id =  Column(Integer, ForeignKey('publicacion.id'))
    favoritos = relationship(Publicaciones)


   
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
