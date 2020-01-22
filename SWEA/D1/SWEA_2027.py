# Problem [2027] : 주어진 텍스트를 그대로 출력하세요.
#  <출력>
#  #++++
#  +#+++
#  ++#++
#  +++#+
#  ++++#

string = '++++'
string_list = list(string)
for i in range(len(string)) :
    string_list.insert(i,'#')
    print(''.join(map(str,string_list)))
    string_list = list(string)


