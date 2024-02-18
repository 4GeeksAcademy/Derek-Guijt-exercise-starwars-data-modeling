import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def serialize(self):
        return{
            "email": self.email,
            "user_name": self.user_name
        }
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=False)
    rotational_period = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    

    def serialize(self):
        return {
            "diameter": self.diameter,
            "rotational_period": self.rotational_period,
            "climate": self.climate,
            "population": self.population,
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    

    def serialize(self):
        return {
            "model": self.model,
            "crew": self.crew,
            "passengers": self.passengers,
            "cost_in_credits": self.cost_in_credits,
        }
    
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    

    def serialize(self):
        return {
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height,
            "name": self.name,
        }
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)

    user=relationship(User)
    characters=relationship(Characters)
    vehicles=relationship(Vehicles)
    planets=relationship(Planets)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
