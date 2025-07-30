
from decoder.base_64 import *
from decoder.rot import *
from utils.checker import *
from utils.getter import *
from utils.operator import *


import time


passwd = "1q2w3e4r"
input_is_hex = False
target_word = "G;"
    
def deobf_with_XOR_one_key():

    for i in range(256):
        test_passwd = list(passwd)

        for j in range(len(test_passwd)):
            test_passwd[j] = chr(((ord(test_passwd[j])^ i)))

        if check_out_of_range(test_passwd):
            continue

        test_passwd = ''.join(test_passwd)

        if has_target_word(target_word, test_passwd):
            break


if input_is_hex:
    passwd = convert_to_bytes(passwd)
    print(passwd)

# rot_result = deobf_with_ROT(passwd,target_word)
# for i in rot_result:
#     print(i)

# print(decode_with_Base64(passwd))

deobf_with_XOR_one_key()

result = deobf_with_XOR_two_bytes_keys(passwd,target_word)
for i in range(len(result)):
    print(result[i])

# start = time.time()
# end = time.time()
# print(f"Time spent of MAP: {end-start:.2f} sec")

