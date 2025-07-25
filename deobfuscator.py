from zxcvbn import zxcvbn
import base64
import re

ASCII_LEN = 127-33
passwd = "1q2w3e4r"
input_is_hex = False
target_word = "kgfi"

def is_hex(s):
    return re.fullmatch(r'[0-9a-fA-F]+', s) is not None

def convert_to_bytes(passwd):
    try:
        if len(passwd) %2 ==1:
            print("It's not Hex value. Len should be even")
            exit(1)            
        if is_hex(passwd):
            passwd = bytes.fromhex(passwd).decode('utf-8')
            return passwd
    except Exception as e:
        print(e)
        return None
    

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


def check_out_of_range(test_word):
    for c in test_word:
        if ord(c)<32 or 126<ord(c):
            return True
    return False

def deobf_with_ROT():
    
    for i in range (ASCII_LEN):
        test_passwd = list(passwd)
        
        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j]))+i))
            # test_passwd[j] = chr(((ord(test_passwd[j]) - 33 + i) % 94) + 33)

        if check_out_of_range(test_passwd):
            continue

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
    
def deobf_with_XOR_one_key():

    for i in range(256):
        test_passwd = list(passwd)

        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j])^ i)))

        if check_out_of_range(test_passwd):
            continue

        test_passwd = ''.join(test_passwd)

        if has_target_word(test_passwd):
            break
        get_result_of(test_passwd,"XOR KEY_x")


def deobf_with_XOR_two_bytes_keys():
    count =0
    for i in range(256):

        for j in range(256):
            test_passwd = list(passwd)  
            for c in range(len(test_passwd)):
                key = i if c%2==0 else j
                test_passwd[c] = chr(((ord(test_passwd[c])^ key)))

            if check_out_of_range(test_passwd):
                continue

            test_passwd = ''.join(test_passwd)

            if has_target_word(test_passwd):
                break

            print(count,end=' ')
            get_result_of(test_passwd,"XOR 2Bytes_Key")    
            count+=1 


if input_is_hex:
    passwd = convert_to_bytes(passwd)
    print(passwd)

# deobf_with_ROT()
# print(decode_with_Base64())
# deobf_with_XOR_one_key()
deobf_with_XOR_two_bytes_keys()
