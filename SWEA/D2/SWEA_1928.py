# Proble [1928] : Base64 Decoder
# 8 bit 문자 = > 6 bit 문자
# Decoding

base64_dict_binary = dict()
base64_dict_digit = dict()

for a in range(1,27) :
    if chr(a+64) not in base64_dict_digit :
        base64_dict_digit[chr(a+64)] = a-1
for b in range(1,27) :
    if chr(b+96) not in base64_dict_digit :
        base64_dict_digit[chr(b+96)] = b+25
for c in range(0,10) :
    if chr(c+48) not in base64_dict_digit :
        base64_dict_digit[chr(c+48)] = c+52
base64_dict_digit['+'] = 62
base64_dict_digit['/'] = 63


for i in range(1,27) :
    if chr(i+64) not in base64_dict_binary :
        base64_dict_binary[chr(i+64)] = str(bin(i-1))[2:]
for k in range(1,27) :
    if chr(k+96) not in base64_dict_binary :
        base64_dict_binary[chr(k+96)] = str(bin(k+25))[2:]
for j in range(0,10) :
    if chr(j+48) not in base64_dict_binary :
        base64_dict_binary[chr(j+48)] = str(bin(j+52))[2:]
base64_dict_binary['+'] = str(bin(62))[2:]
base64_dict_binary['/'] = str(bin(63))[2:]

result = ''
my_string = input()
for string in my_string :
    if string in base64_dict_binary.keys() :
        result += base64_dict_binary[string]

result_list =list()
for i in range(1,(len(result))//6+1) :
    result_list.append(result[6*(i-1):6*i])

for i,(key,value) in enumerate(base64_dict_digit.items()):
    if value == int('0b'+str(result_list[0]),2) :
        print(key)

