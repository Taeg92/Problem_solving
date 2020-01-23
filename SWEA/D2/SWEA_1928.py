# Proble [1928] : Base64 Decoder
# 6 bit 문자 = > 8 bit 문자
# Decoding

def decode_String(string):
    result_string = ''
    for idx in range(len(string) // 4):
        base64_string = string[idx * 4:(idx + 1) * 4]
        decoding = 0
        temp_list = list()
        for index in range(4):
            value = get_decode_Value(base64_string[index])
            decoding = (decoding << 6) + value

        temp_list.append(chr(decoding >> 16))
        temp_list.append(chr((decoding >> 8) & 0xff))
        temp_list.append(chr(decoding & 0xff))
        temp_string = ''.join(map(str,temp_list))
        result_string = result_string + temp_string
    return result_string

def get_decode_Value(alpha):

    if ('A' <= alpha <= 'Z'):
        val = ord(alpha) - ord('A')
    elif ('a' <= alpha <= 'z'):
        val = ord(alpha) - ord('a') + 26
    elif ('0' <= alpha <= '9'):
        val = ord(alpha) - ord('0') + 52
    elif (alpha == '+'):
        val = 62
    elif (alpha == '/'):
        val = 63
    return val



test_cnt = int(input())
result_decode = ''
for test_count in range(1, test_cnt+1):
    encode_string = input()
    result_decode = decode_String(encode_string)
    print('#{} {}'.format(test_count,result_decode))
