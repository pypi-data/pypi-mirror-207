#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

DEBUG = os.getenv("DEBUG", True)
SERVER_PORT = int(os.getenv("SERVER_PORT", 5000))
RATE_LIMIT = int(os.getenv("RATE_LIMIT", 60))
PERIOD = int(os.getenv("PERIOD", 60 * 1000))  # milliseconds
WHITELISTED_IPS = os.getenv("WHITELISTED_IPS", "").split(",")
OPENAI_KEYS = os.getenv("OPENAI_API_KEY", "").split(",")
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/users.db'
# OPENAI_KEYS = os.getenv("OPENAI_API_KEY", "").split(",")
