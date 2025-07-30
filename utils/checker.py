import re

def has_target_word(target_word,test_word):
    if len(target_word) == 0 or test_word is None:
        return False
    
    if test_word.lower().find(target_word.lower()) != -1 :
        print(f"//////////// there are '{target_word}' in [ {test_word} ] ////////////")
        return True
    else :
        return False
    

def is_hex(s):
    return re.fullmatch(r'[0-9a-fA-F]+', s) is not None



def check_out_of_range(test_word):
    for c in test_word:
        if ord(c)<32 or 126<ord(c):
            return True
    return False
