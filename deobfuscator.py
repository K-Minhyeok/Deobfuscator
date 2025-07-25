from zxcvbn import zxcvbn
import base64

ASCII_LEN = 127-33
passwd = "1q2w3e4r"
target_word = "cEGF"

def has_target_word(test_word):
    if len(target_word) == 0 or test_word is None:
        return False
    
    if test_word.lower().find(target_word.lower()) != -1 :
        print(f"//////////// there are '{target_word}' in [ {test_word} ] ////////////")
        return True
    else :
        return False
    
def get_result_of(test_password,where):
        result = zxcvbn(test_password)
        print(f"{where} : {test_password} / {result['score']} ")
        return result['password'], result['score']


def deobf_with_ROT():
    for i in range (ASCII_LEN):
        test_passwd = list(passwd)
        
        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j]) - 33 + i) % 94) + 33)

        test_passwd = ''.join(test_passwd)
        if has_target_word(test_passwd):
            break

        get_result_of(test_passwd,"ROT")

def decode_with_Base64():
    try:
        print("Decode with base64")
        return base64.b64decode(passwd).decode('UTF-8')
    except Exception:
        print("It's not Base64 Encoded")
        return None 

def deobf_with_XOR_noKeyed():
    for i in range(256):
        test_passwd = list(passwd)
        for j in range(len(test_passwd)):
            test_passwd[j] = chr( ((ord(test_passwd[j]) - 33) ^ i) % 94 + 33 )
        
        test_passwd = ''.join(test_passwd)
        if has_target_word(test_passwd):
            break

        get_result_of(test_passwd,"XOR KEY_x")


deobf_with_ROT()
print(decode_with_Base64())
deobf_with_XOR_noKeyed()