import base64

decode_me = ""
num = 4

for i in range(1, num):
    decode_me = base64.b64decode(decode_me)
    print(decode_me)