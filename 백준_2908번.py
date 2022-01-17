a, b = map(int, input().split()) # 값 대입
a = str(a) # a값을 str형으로 변환
b = str(b) # b값을 str형으로 변환
if a[2] > b[2] : # 조건문 if, elif, else -> a의 마지막 문자와 b의 마지막 문자 비교
    print(a[2], a[1] ,a[0], sep = '') # a의 값을 마지막 문자부터 차례대로 출력하고 sep = ''를 사용해 공백을 없앰
elif a[2] < b[2] :
    print(b[2], b[1], b[0], sep = '')
else :
    if a[1] > b[1] : # a의 2번째 문자와 b의 2번째 문자 비교
        print(a[2], a[1], a[0], sep = '')
    elif a[1] < b[1] :
        print(b[2], b[1], b[0], sep = '')
    else :
        if a[0] > b[0] : # a의 1번째 문자와 b의 1번째 문자 비교
            print(a[2], a[1], a[0], sep = '')
        else :
            print(b[2], b[1], b[0], sep = '')