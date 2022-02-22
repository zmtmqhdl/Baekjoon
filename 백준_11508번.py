n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # append를 사용하여 대입된 값을 data라는 list의 원소로 추가
data.sort(reverse = True) # sort(reverse = True)를 사용하여 data라는 list의 원소를 내림차순으로 정렬
total = sum(data) # sum을 사용하여 data라는 list의 원소의 합을 total변수에 저장
for i in range(0, len(data)) : # 반복문 for -> 0부터 len(data) - 1까지 i에 차례대로 대입하며 반복
    if i % 3 == 2 : # 조건문 if -> 3개씩 묶음으로 하여 가장 저렴한 것을 빼주기 위해서 묶음을 짓는 과정
        total -= data[i] # total = total - data[i] -> 묶음 중에서 가장 저렴한 값을 빼는 연산
print(total) # 출력