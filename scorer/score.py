from nltk.corpus import words
from utils.checker import *
from utils.getter import *



def score_freq_character(passwd):
    ENGLISH_FREQ = {'a': 8,'b': 2,'c': 5,'d': 3,'e': 11,'f': 2,
                    'g': 2,'h': 3,'i': 8,'j': 0,'k': 1,'l': 5,
                    'm': 3,'n': 7,'o': 7,'p': 3,'q': 0,'r': 8,
                    's': 6,'t': 7,'u': 4,'v': 1,'w': 1,'x': 0,'y': 2,'z': 0}
    score = 0
    for i in passwd:
        if i in ENGLISH_FREQ:
            score += ENGLISH_FREQ[i]
    
    result = round(score*2/len(passwd))

    if result > 15:
        return 15
    else : 
        return result


def score_bigram(passwd):
    score =0
    COMMON_BIGRAMS = {
    'th', 'of', 'io', 'he', 'ed', 'le', 'in', 'is', 've', 'er', 'it', 'co', 'an', 'al', 'me', 're',
    'ar', 'de', 'on', 'st', 'hi', 'at', 'to', 'ri', 'en', 'nt', 'ro', 'nd', 'ng', 'ic', 'ti', 'se',
    'ne', 'es', 'ha', 'ea', 'or', 'as', 'ra', 'te', 'ou', 'ce'
    }

    for i in range (len(passwd)):
        if passwd[i:i+2] in COMMON_BIGRAMS:
            score +=1
    
    return score

def score_trigram(passwd):
    score =0
    COMMON_TRIGRAMS = [
    'the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 
    'nce', 'edt', 'tis', 'oft', 'sth', 'men']

    for i in range (len(passwd)-2):
        if passwd[i:i+3] in COMMON_TRIGRAMS:
            print(passwd[i:i+3])
            score +=1
    
    if score>15:
        return 15
    else :
        return score

def score_pattern(passwd):
    return

def score_entropy(passwd):
    return



def get_total_score(passwd,target_word):
    total = 0
    
    # target_word 존재 유무
    if has_target_word(target_word,passwd) :
        total +=100

    #문자 패턴 (20점 만점)
    total+= score_pattern(passwd)

    #자주 등장하는 알파벳 (15점 만점) 
    #Done
    total+= score_freq_character(passwd)
    
    #자주 등장하는 bigram (15점 만점)
    #Done

    total+= score_bigram(passwd)

    #자주 등장하는 trigram (15점 만점)
    #Done
    total+= score_trigram(passwd)


    #entropy (10점 만점)
    total+= score_entropy(passwd)


    #강력한 비밀번호인지 (10점 만점)
    result =get_result_of(passwd)
    score = result['score']
    total += score

    return total
