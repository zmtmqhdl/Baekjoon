n = int(input()) # 반복 횟수 대입
for _ in range(n) : # 반복문 for
    data = input() # 값 대입
    for i in range(len(data) - 1) : # 반복문 for -> i번째 문자와 i + 1번째 문자를 비교할 것이므로 마지막 문자는 횟수에 들어갈 필요가 없기에 반복 횟수는 data의 길이 - 1
        if data[i] != data[i + 1] : # 조건문 if -> 만약 i번째 문자와 i + 1번째 문자가 같지 않다면
            new_data = data[i + 1:] # new_data라는 변수에 data의 i + 1번째부터 마지막 문자까지 대입
            if new_data.count(data[i]) > 0 : # 조건문 if - > 만약 new_data에 data[i]가 존재한다면
                n -= 1 # n = n - 1
                break # 중지
print(n) # 출력