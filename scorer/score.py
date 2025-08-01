from nltk.corpus import words
from deob_utils.checker import *
from deob_utils.getter import *
from collections import Counter
from zxcvbn import zxcvbn
import math

def score_freq_character(passwd):
    ENGLISH_FREQ = {'a': 8,'b': 2,'c': 5,'d': 3,'e': 11,'f': 2,
                    'g': 2,'h': 3,'i': 8,'j': 0,'k': 1,'l': 5,
                    'm': 3,'n': 7,'o': 7,'p': 3,'q': 0,'r': 8,
                    's': 6,'t': 7,'u': 4,'v': 1,'w': 1,'x': 0,'y': 2,'z': 0}
    score = 0
    low_passwd = passwd.lower()
    for i in low_passwd:
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
    return 0

def score_entropy(passwd):
    char_freq = Counter(passwd)
    entropy =0
    passwd_len = len(passwd)
    
    for f in char_freq.values():
        prob = f/passwd_len
        result = abs(math.log2(prob)*prob)
        entropy+=result

    if entropy < 4.0:
        return 15
    elif entropy < 6.0:
        return 10
    elif entropy < 11.9:
        return 5
    else:
        return 0

def score_strong_password(test_password):
        result = zxcvbn(test_password)
        return 10 - result['score']    


def get_total_score(passwd,target_word):

    print(passwd, end='===')
    if passwd == "":
        return 0
    
    total = 0

    if target_word != "" :
        if has_target_word(target_word,passwd) :
            total +=100

    #20
    total+= score_freq_character(passwd)
    print(score_freq_character(passwd),end=' ')
    
    #15
    total+= score_bigram(passwd)
    print(score_bigram(passwd),end=' ')

    #15
    total+= score_trigram(passwd)
    print(score_trigram(passwd),end=' ')


    #entropy (15점 만점)
    total+= score_entropy(passwd)
    print(score_entropy(passwd),end=' ')


    #문자 패턴 (20점 만점)
    total+= score_pattern(passwd)
    print(score_pattern(passwd),end=' ')

    #강력한 비밀번호인지 (10점 만점  (10-강력함 점수))
    total += score_strong_password(passwd)

    print(score_strong_password(passwd),end=' ')

    print(total)
    return total