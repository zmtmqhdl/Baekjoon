n = int(input()) # 값 대입
i = int(input()) # 값 대입
data = list(map(int, str(i))) # list(map(int, str(i))) -> i의 값을 str형으로 바꾸어 한 문자씩 int형으로 다시 바꿔 list에 넣음
print(sum(data)) # data라는 list에 있는 원소들의 합을 출력