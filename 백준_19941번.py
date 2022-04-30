n, k = map(int, input().split()) # 값 대입
data = list(str(input())) # 대입된 값을 원소로 갖는 data라는 list생성
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    if data[i] == 'P' : # 조건문 if -> data[i]가 사람인 경우
        for j in range(max(0, i - k), min(i + k + 1, n)) : # 반복문 for -> max(0, i - k)부터 min(i + k + 1, n) - 1까지 j에 차례대로 대입하며 반복
            if data[j] == 'H' : # 조건문 if -> data[j]가 햄버거인 경우
                data[j] = 0 # data[j]의 값을 0으로 변경
                break # 중지
print(data.count(0)) # count를 사용하여 data라는 list에서 0의 개수를 출력