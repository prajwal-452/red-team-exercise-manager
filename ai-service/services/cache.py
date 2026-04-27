import redis
import hashlib
import json

r = redis.Redis(host="localhost", port=6379, db=0)

def get_cache_key(text):
    return hashlib.sha256(text.encode()).hexdigest()

def get_cached(text):
    try:
        value = r.get(get_cache_key(text))
        if value:
            return json.loads(value)
    except:
        pass
    return None

def set_cache(text, data):
    try:
        r.setex(get_cache_key(text), 900, json.dumps(data))
    except:
        pass