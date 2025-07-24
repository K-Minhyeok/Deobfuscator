from zxcvbn import zxcvbn

ASKII_LEN = 128
passwd = "1q2w3e4r"
target_word = "ST"

for i in range (ASKII_LEN):
    test_passwd = list(passwd)

    for j in range(len(passwd)):
        test_passwd[j] = chr((ord(test_passwd[j])+i)%128)
    test_passwd = ''.join(test_passwd)

    if target_word.find(test_passwd) >0:
        print(f"//////////// there are '{target_word}' in [ {test_passwd} ] ////////////")
        continue

    result = zxcvbn(test_passwd)
    print(f" === {test_passwd} : {result['score']} ===")
