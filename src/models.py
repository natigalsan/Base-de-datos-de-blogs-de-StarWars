import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, primary_key=True)



class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_pj = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))

    rel_user = relationship(User)

    def to_dict(self):
        return {}


class Fav_Pj (Base):
    __tablename__ = 'fav_Pj'
    id = Column(Integer, primary_key=True)
    name_Fav_pj = Column(String(250))

    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    rel_personajes = relationship(Personajes)


class Naves (Base):
    __tablename__ = 'naves'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_nave = Column(String(250))
    manufacturer = Column(String(250))
    vehicle_class = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    rel_user = relationship(User)

class Fav_naves (Base):
    __tablename__ = 'fav_naves'
    id = Column(Integer, primary_key=True)
    name_Fav_naves = Column(String(250))

    naves_id = Column(Integer, ForeignKey('naves.id'))
    rel_naves = relationship(Naves)

class Planetas (Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_pl = Column(String(250))
    climate = Column(String(250))
    diameter = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    rel_user = relationship(User)

class Fav_planetas (Base):
    __tablename__ = 'fav_pl'
    id = Column(Integer, primary_key=True)
    name_Fav_pl = Column(String(250))

    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    rel_planetas = relationship(Planetas)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

#     person_id = Column(Integer, ForeignKey('person.id'))


