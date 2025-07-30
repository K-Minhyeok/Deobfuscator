from utils.checker import *
from utils.getter import *

ASCII_LEN = 127-33

def deobf_with_ROT(passwd,target_word):
    
    result = []

    for i in range (ASCII_LEN):
        test_passwd = list(passwd)
        
        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j]))+i))
            # test_passwd[j] = chr(((ord(test_passwd[j]) - 33 + i) % 94) + 33)

        if check_out_of_range(test_passwd):
            continue

        test_passwd = ''.join(test_passwd)

        if has_target_word(target_word,test_passwd):
            break


        sample_pw , score = get_result_of(test_passwd,"ROT")   
        tmp = [sample_pw,score,[i,j]]
        result.append(tmp)

    return result