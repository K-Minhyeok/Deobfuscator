from utils.getter import *
from multiprocessing import Pool
from functools import partial


def deobf_with_XOR_two_bytes_keys(passwd,target_word):

    keys = [[i, j] for i in range(256) for j in range(256)]
    cpu_num = get_cpu_num()
    result = []

    #이거 설명글 쓰기
    func = partial(calculate_XOR_two_bytes, passwd=passwd,target_word =target_word )

    with Pool(cpu_num) as pool:
        for i in pool.map(func,keys):

            if i is not None:
                result.append(i)
    return result              

def calculate_XOR_two_bytes(key_pair,passwd,target_word):
    i,j = key_pair
    test_passwd = list(passwd) 

    for c in range(len(test_passwd)):
        key = i if c%2==0 else j
        test_passwd[c] = chr(((ord(test_passwd[c])^ key)))

    if check_out_of_range(test_passwd):
        return

    test_passwd = ''.join(test_passwd)

    if has_target_word(target_word,test_passwd):
        print("hit with key:", i, j)

    sample_pw , score = get_result_of(test_passwd,"XOR 2Bytes_Key")   
    result= [sample_pw,score,key_pair]    

    return  result