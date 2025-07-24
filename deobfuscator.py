from zxcvbn import zxcvbn

ASCII_LEN = 127-33
passwd = "1q2w3e4r"
target_word = "%j&"

def has_target_word(test_word):
    if test_word.lower().find(target_word.lower()) != -1 :
        print(f"//////////// there are '{target_word}' in [ {test_word} ] ////////////")
        return True
    else :
        return False
    

def get_from_ROT():

    for i in range (ASCII_LEN):
        test_passwd = list(passwd)

        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j]) - 33 + i) % 94) + 33)

        test_passwd = ''.join(test_passwd)

        if has_target_word(test_passwd):
            break

        result = zxcvbn(test_passwd)
        print(f" ::: {test_passwd} : {result['score']} ::: {len(test_passwd)}")




get_from_ROT()