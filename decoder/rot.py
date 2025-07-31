from utils.checker import *
from utils.getter import *

ASCII_LEN = 127-33

def deobf_with_ROT(passwd,target_word):
    total = []

    for i in range (ASCII_LEN):
        test_passwd = list(passwd)
        is_found = False

        for j in range(len(test_passwd)):
            # test_passwd[j] = chr(((ord(test_passwd[j]))+i))
            test_passwd[j] = chr(((ord(test_passwd[j]) - 33 + i) % 94) + 33)

        if check_out_of_range(test_passwd):
            continue

        test_passwd = ''.join(test_passwd)

        if has_target_word(target_word,test_passwd):
            is_found = True


        score = get_result_of(test_passwd,"ROT")   
        result= {
                "password" : test_passwd,
                "score" : score,
                "key" : i,
                "is_found" : is_found
                }
        total.append(result)        

    return total