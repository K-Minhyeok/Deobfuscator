def score_bigram(passwd):
    score =0
    COMMON_BIGRAMS = [
    'th', 'of', 'io', 'he', 'ed', 'le', 'in', 'is', 've', 'er', 'it', 'co', 'an', 'al', 'me', 're',
    'ar', 'de', 'on', 'st', 'hi', 'at', 'to', 'ri', 'en', 'nt', 'ro', 'nd', 'ng', 'ic', 'ti', 'se',
    'ne', 'es', 'ha', 'ea', 'or', 'as', 'ra', 'te', 'ou', 'ce'
    ]

    for i in range (len(passwd)-1):
        if passwd[i:i+2] in COMMON_BIGRAMS:
            print(passwd[i:i+3])
            score +=1
    
    if score>15:
        return 15
    else :
        return score
    
def score_trigram(passwd):
    score =0
    COMMON_TRIGRAMS = [
    'the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 
    'nce', 'edt', 'tis', 'oft', 'sth', 'men']

    for i in range (len(passwd)-2):
        if passwd[i:i+3].lower() in COMMON_TRIGRAMS:
            print(passwd[i:i+3])
            score +=1
    
    if score>15:
        return 15
    else :
        return score

print(score_trigram("that is the menu"))