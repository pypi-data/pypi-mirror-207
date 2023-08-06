#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import OPENAI_KEYS

def get_openai_key():
    return random.choice(OPENAI_KEYS)

def calculate_tokens(text):
    return random.random()
