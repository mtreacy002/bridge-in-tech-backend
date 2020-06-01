from flask import jsonify
import requests
# from requests.exceptions import HTTPError
from flask import json

from werkzeug.exceptions import HTTPException
import logging

# set base url

# for ms-api local server
BASE_MS_API_URL = "http://127.0.0.1:4000"

# for ms-api heroku server
# BASE_MS_API_URL = "https://bridge-in-tech-ms-test.herokuapp.com"

# @application.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response

# create instance
def post_request(request_url, data):
    response = None,
    try:
    
        response_raw = requests.post(
            request_url,
            json = data,
            headers = {"Accept": "application/json"}
        )
        response_raw.status_code = 201
        response_raw.encoding = "utf-8"
        response = response_raw.json()
        
    except HTTPException as e:
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"

    print(f"{response}")
    return response



