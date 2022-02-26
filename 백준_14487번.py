n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
del data[-1] # del을 사용하여 data라는 list에서 가장 큰 값을 가진 원소 삭제
print(sum(data)) # sum을 사용하여 data라는 list의 원소의 합을 출력