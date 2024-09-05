import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify

SECRET_KEY = 'super_secret_secrets'

def encode_token(user_id): #original
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id #subject, aka, who is the token for
    }

    token = jwt.encode(payload, SECRET_KEY,  algorithm='HS256')
    return token

def token_required(f): #f = the function our wrapper wraps around
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around a function we need to make sure its parameters make it through the wrapper
        token = None
        if 'Authorization' in request.headers: 
            try:
                token = request.headers['Authorization'].split()[1] 
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')# decoding the token with the same way we encoded it
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Tokehas expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"}), 401
            return f(*args, **kwargs) #Calling our wrapped function
        else:
            return jsonify({"message": "Authentication token missing"}), 401
    return wrapper 

def user_validation(f): #validates and returns the user_id associated with the token
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers["Authorization"].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Tokehas expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"}), 401    
            return f(token_id=payload['sub'], *args, **kwargs)
        else:
            return jsonify({"message": "Authentication token missing"}), 401
        
    return wrapper


def encode_role_token(user_id, role_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id, #subject, aka, who is the token for
        'admin': role_id
    }

    token = jwt.encode(payload, SECRET_KEY,  algorithm='HS256')
    return token


def admin_required(f): #f = the function our wrapper wraps around
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around a function we need to make sure its parameters make it through the wrapper
        token = None
        if 'Authorization' in request.headers: 
            try:
                token = request.headers['Authorization'].split()[1] 
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')# decoding the token with the same way we encoded it
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token is expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"}), 401
            if payload['admin']:
                return f(*args, **kwargs) #Calling our wrapped function
            else:
                return jsonify({"message": "Need Admin permissions"}), 401
        else:
            return jsonify({"message": "Authentication token missing"}), 401
    return wrapper 