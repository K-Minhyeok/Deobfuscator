from collections import Counter
import math


def score_entropy(passwd):
    char_freq = Counter(passwd)
    entropy =0
    passwd_len = len(passwd)
    
    for f in char_freq.values():
        prob = f/passwd_len
        result = abs(math.log2(prob)*prob)
        entropy+=result
    print(entropy)

    if entropy < 4.0:
        print("ent 4.0")
        return 15
    elif entropy < 6.0:
        print("ent 6.0")
        return 10
    elif entropy < 11.9:
        print("ent 11.9")
        return 5
    else:
        return 0


print(score_entropy("zbgvlwmnqc"))