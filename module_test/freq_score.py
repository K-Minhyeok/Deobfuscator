def score_freq_character(passwd):
    ENGLISH_FREQ = {'a': 8,'b': 2,'c': 5,'d': 3,'e': 11,'f': 2,
                    'g': 2,'h': 3,'i': 8,'j': 0,'k': 1,'l': 5,
                    'm': 3,'n': 7,'o': 7,'p': 3,'q': 0,'r': 8,
                    's': 6,'t': 7,'u': 4,'v': 1,'w': 1,'x': 0,'y': 2,'z': 0}
    score = 0
    for i in passwd:
        if i in ENGLISH_FREQ:
            score += ENGLISH_FREQ[i]
    
    result = score*2/len(passwd)

    return round(result)


print(score_freq_character("theeis is test123"))