from deob_utils.checker import *
from deob_utils.getter import *
from scorer.score import *

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

        score = get_total_score(test_passwd,target_word) 
        if score >100 : 
            is_found = True  
        result= {
                "password" : test_passwd,
                "score" : score,
                "key" : i,
                "is_found" : is_found,
                "decoder" : "ROT"
                }
        total.append(result)        

    return total