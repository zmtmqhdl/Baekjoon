a = int(input()) # 값 대입
b = int(input()) # 값 대입
c = int(input()) # 값 대입
result = list(str(a * b * c)) # a * b * c를 str형으로 변환하여 list에 한 글자씩 나눠서 대입
for i in range(10): # 반복문 for
    print(result.count(str(i))) # count를 사용해 문자 i를 result라는 list에서 찾아서 갯수 출력