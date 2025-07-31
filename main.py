from decoder.base_64 import *
from decoder.rot import *
from decoder.xor import *
from utils.checker import *
from utils.getter import *

import time

passwd = "1q2w3e4r"
input_is_hex = False
target_word = "G;"
 
#--------------------------------------

if input_is_hex:
    passwd = convert_to_bytes(passwd)
    print(passwd)

result = deobf_with_ROT(passwd,target_word)
# for i in rot_result:
#     print(i)

# print(decode_with_Base64(passwd))

# result = deobf_with_XOR_one_key(passwd , target_word)

# result= deobf_with_XOR_two_bytes_keys(passwd,target_word)
for i in result:
    # if i['is_found']:
        print(i)

# start = time.time()
# end = time.time()
# print(f"Time spent of MAP: {end-start:.2f} sec")

