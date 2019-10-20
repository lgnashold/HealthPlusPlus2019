import os
import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)  


def init_db():
    db.drop_all()
    db.create_all()
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
# engine = db.create_engine('sqlite:///sqllite_test.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.