import base64

def generate_base64(key):
    key = str(key)
    return str(base64.urlsafe_b64encode(key.encode("utf-8")))