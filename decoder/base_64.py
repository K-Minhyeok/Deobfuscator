import base64

def decode_with_Base64(passwd):
    try:
        print("Decode with base64")
        return base64.b64decode(passwd).decode('UTF-8')
    except Exception:
        print("It's not Base64 Encoded")
        return None 