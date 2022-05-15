s = input() # 값 대입
data = set() # data라는 set생성
for i in range(len(s)) : # 반복문 for -> 0부터 len(s) - 1까지 i에 차례대로 대입하며 반복
    for j in range(i, len(s)) : # 반복문 for -> i부터 len(s) - 1까지 j에 차례대로 대입하며 반복
        data.add(s[i:j+1]) # add를 사용하여 s[i:j+1]을 data라는 set의 원소로 추가
                           # 중복은 추가되지 않음
print(len(data)) # 출력