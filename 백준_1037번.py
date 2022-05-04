n = int(input()) # 값 대입 
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
print(max(data) * min(data)) # 출력