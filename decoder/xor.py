from deob_utils.getter import *
from multiprocessing import Pool
from functools import partial
from scorer.score import *


   
def deobf_with_XOR_one_key(passwd , target_word):
    is_found = False
    total = []
    for i in range(256):
        test_passwd = list(passwd)

        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j])^ i)))

        if check_out_of_range(test_passwd):
            continue

        test_passwd = ''.join(test_passwd)
        
        score = get_total_score(test_passwd,target_word)   
        if score >100 : 
            is_found = True

        result= {
        "password" : test_passwd,
        "score" : score,
        "key_pair" : [i,j],
        "is_found" : is_found,
        "decoder" : "XOR_One_Key"
        }
        total.append(result)

    return total



def deobf_with_XOR_two_bytes_keys(passwd,target_word):

    keys = [[i, j] for i in range(256) for j in range(256)]
    cpu_num = get_cpu_num()
    result = []

    func = partial(calculate_XOR_two_bytes, passwd=passwd,target_word =target_word)

    with Pool(cpu_num) as pool:
        for i in pool.map(func,keys):

            if i is not None:
                result.append(i)
    return result              

def calculate_XOR_two_bytes(key_pair,passwd,target_word):
    i,j = key_pair
    is_founded = False
    test_passwd = list(passwd) 

    for c in range(len(test_passwd)):
        key = i if c%2==0 else j
        test_passwd[c] = chr(((ord(test_passwd[c])^ key)))

    if check_out_of_range(test_passwd):
        return None

    test_passwd = ''.join(test_passwd)

    score = get_total_score(test_passwd,target_word)   
    if score >100 : 
        is_found = True

    result= {
        "password" : test_passwd,
        "score" : score,
        "key_pair" :key_pair,
        "is_found" : is_found,
        "decoder" : "XOR_Two_Keys"
        }
    
    
    return  result