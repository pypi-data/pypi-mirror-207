#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
import re
import random
import string
from typing import Optional

db = SQLAlchemy()

class User(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    token_usage = db.Column(db.Integer, default=0)
    token_limit = db.Column(db.Integer)
    api_key = db.Column(db.String(200))

    @staticmethod
    def generate_api_key() -> str:
        """Generates a customized API key for the user"""
        chars = string.ascii_letters + string.digits
        random_key = ''.join(random.choice(chars) for _ in range(48))
        return f'bk-{random_key}'

    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """Validates the format of an API key"""
        pattern = r'^bk-[A-Za-z0-9]{48}$'
        return bool(re.match(pattern, api_key))

    def set_api_key(self, api_key: Optional[str]) -> None:
        """Sets the API key for the user"""
        if api_key:
            if not User.validate_api_key(api_key):
                raise ValueError("Invalid API key format")
            self.api_key = api_key
        else:
            self.api_key = User.generate_api_key()


def initialize_database(app) -> None:
    """Initializes the database"""
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

def add_new_user(name: str, limit: int) -> User:
    """Adds a new user to the database"""
    api_key = User.generate_api_key()
    new_user = User(name=name, token_limit=limit, api_key=api_key)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_all_users() -> list[User]:
    """Returns all users in the database"""
    return User.query.all()

def get_user_by_id(user_id: int) -> User:
    """Returns a user object by ID"""
    return User.query.get(user_id)

def get_user_by_api_key(api_key: str) -> User:
    """Returns a user object by API key"""
    return User.query.filter_by(api_key=api_key).first()

def get_user_and_key(headers: dict) -> tuple:
    """
    Determines the API key and user corresponding to the request headers.

    :param headers: the request headers
    :return: a tuple containing the user and API key
    """
    api_key = headers['Authorization'].lstrip('Bearer ')

    # If the key begins with sk-, use OpenAI key
    if api_key[:3] == 'sk-':
        return None, api_key

    # Otherwise, use an OpenApy API key based on the user's credentials
    user = get_user_by_api_key(api_key)

    # If the user is not valid, return None for user and API Key
    if not user:
        return None, None

    # Otherwise, return the API Key and User object
    api_key = OPENAI_API_KEY
    headers['Authorization'] = f'Bearer {api_key}'

    return user, api_key


def update_user_token_usage(user: User, tokens_used: int) -> None:
    """Updates a user's token usage"""
    user.token_usage += tokens_used
    db.session.commit()
