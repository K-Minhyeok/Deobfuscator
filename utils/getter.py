from multiprocessing import cpu_count
from zxcvbn import zxcvbn
from utils.checker import *

def get_cpu_num():
    return cpu_count()-1


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
    

def get_result_of(test_password,where):
        result = zxcvbn(test_password)
        # print(f"{where} : {test_password} / {result['score']} ")
        return result['password'], result['score']