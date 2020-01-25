# Problem [1983] : 조교의 성적 매기기
# A+,A0,A- ...  D+,D0 까지 총 10개이 있다.
# 학생의 수 N은 항상 10의 배수
# 찾고자 하는 학생 : K 1 <= K <= <10



test_cnt = int(input())
grade_list = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for test in range(1,test_cnt+1) :
    result = ''
    student_count, search_idx = map(int,input().split())
    student_list = dict()

    for i in range(student_count) :
        score1, score2, socore3 = map(int,input().split())
        student_list[i] = score1*(0.35) + score2*(0.45) + socore3*(0.20)

    sorted_list = sorted(student_list.values())
    grade = sorted_list.index(student_list[search_idx-1])
    result = grade_list[int((grade/student_count*10))]
    
    print('#{} {}'.format(test,result))
