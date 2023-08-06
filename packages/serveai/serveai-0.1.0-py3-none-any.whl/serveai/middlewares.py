#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import time
from typing import Any, Dict, Union

from flask import make_response

from config import PERIOD, RATE_LIMIT, WHITELISTED_IPS

# Global rate limit dict that stores the requests count and last request time for each IP address
rate_limit: Dict[str, Dict[str, Union[int, float]]] = {}


def cors_middleware(response: Any) -> Any:
    """
    Middleware function that adds CORS headers to the Flask response.

    Args:
        response (Flask Response): Response object to modify with CORS headers

    Returns:
        Any: Flask Response object with CORS headers
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


def rate_limit_middleware(func: Any) -> Any:
    """
    Middleware function that enforces a rate limit on all requests.

    Args:
        func (function): Flask route function to wrap with rate limiting middleware

    Returns:
        Any: Wrapper function that enforces rate limit for the input Flask route function
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function that applies rate limit middleware to Flask route functions.

        Args:
            *args (Any): positional arguments
            **kwargs (Any): keyword arguments

        Returns:
            Any: Flask response with rate limit headers or Flask route function
        """
        global rate_limit

        # Get the client IP address
        ip: str = args[0].headers.get("CF-Connecting-IP") \
            or args[0].headers.get("X-Forwarded-For") \
            or args[0].remote_addr

        # If IP is white-listed, skip rate limit enforcement
        if ip in WHITELISTED_IPS:
            return func(*args, **kwargs)

        # Get current UTC timestamp
        current_time: float = time()

        # Get rate limit tracker data for current IP
        ip_data: Dict[str, Union[int, float]] = rate_limit.get(ip, {})

        # If IP not in rate limit tracker, initialize with this request as the first
        if not ip_data:
            rate_limit[ip] = {"requests": 1, "last_request_time": current_time}
        else:
            # Calculate the time interval since the last request
            time_since_last_request = (current_time -
                                       ip_data["last_request_time"]) * 1000

            # If time since last request exceeds rate limit period in milliseconds, reset requests counter for the IP
            if time_since_last_request > PERIOD:
                rate_limit[ip] = {
                    "requests": 1,
                    "last_request_time": current_time
                }
            else:
                # Otherwise, increment the requests counter
                updated_count: int = ip_data["requests"] + 1
                # If the requests count exceeds the rate limit, return error
                if updated_count > RATE_LIMIT:
                    return make_response(
                        {
                            "status": False,
                            "error":
                            "Too many requests, please try again later"
                        },
                        429,
                    )
                # Otherwise, update the requests count and last request time for the IP
                rate_limit[ip] = {
                    "requests": updated_count,
                    "last_request_time": ip_data["last_request_time"]
                }

        # Call the Flask route function since the request didn't exceed the rate limit
        return func(*args, **kwargs)

    return wrapper
