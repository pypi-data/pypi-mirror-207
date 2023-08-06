#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from flask import Blueprint, Response, request

from database import get_user_and_key
from functions import calculate_tokens, get_openai_key

OPENAI_API_URL = 'https://api.openai.com'
OPENAI_API_KEY = get_openai_key()

routes_blueprint = Blueprint("routes", __name__)


@routes_blueprint.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@routes_blueprint.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path: str) -> Response:
    """
    Proxies requests to the OpenAI API, adding user identification.

    :param path: the API path, for example 'v1/engines/davinci/search'
    :return: the OpenAI response with user-specific data
    """
    url = f"{OPENAI_API_URL}/{path}"
    headers = {key: value for (key, value) in request.headers if key != 'Host'}

    # Determine the user appropriate for the API call and what API key to use
    user, api_key = get_user_and_key(headers)
    if not user or not api_key:
        return Response(status=401)

    # Calculate the number of tokens used and update the user token usage
    if user:
        token_used = calculate_tokens(request)
        update_user_token_usage(user, tokens_used)

    response = requests.request(url=url,
                                headers=headers,
                                data=request.get_data(),
                                method=request.method,
                                params=request.args,
                                stream=True)

    # For Debug use
    # response.headers['Authorization'] = f'Bearer {api_key}'

    def generate():
        for chunk in response.iter_content(chunk_size=8192):
            yield chunk

    return Response(generate(),
                    headers=dict(response.headers),
                    status=response.status_code,
                    content_type=response.headers['Content-Type'])


@routes_blueprint.route('/v1/chat/completions', methods=['POST'])
def chat_completions() -> Response:
    """
    Proxies chat completions requests to the OpenAI API, adding user identification and calculating tokens used.

    :return: the OpenAI response with user-specific data
    """
    path = f"{OPENAI_API_URL}/v1/chat/completions"
    url = f"{OPENAI_API_URL}/{path}"
    headers = {key: value for (key, value) in request.headers if key != 'Host'}
    headers['Content-Type'] = 'application/json'

    # Determine the user appropriate for the API call and what API key to use
    user, api_key = get_user_and_key(headers)

    # If the API key is unrecognized, return a 401 Unauthorized error
    if not user or not api_key:
        return Response(status=401)

    # Calculate the number of tokens used and update the user token usage
    if user:
        tokens_used = calculate_tokens(request)
        update_user_token_usage(user, tokens_used)

    # TODO: handle non-stream
    response = requests.post(url=url,
                             headers=headers,
                             json=request.json,
                             stream=True)

    def generate():
        for chunk in response.iter_content(chunk_size=8192):
            yield chunk

    return Response(generate(),
                    headers=dict(response.headers),
                    status=response.status_code,
                    content_type=response.headers['Content-Type'])


@routes_blueprint.after_request
def after(response):
    # print(response.status)
    print(response.headers)
    # print(response.get_data())
    return response
