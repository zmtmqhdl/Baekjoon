data = [] # data라는 list생성
a = list(map(int, input().split())) # 대입된 값을 원소로 갖는 a라는 list생성
data.append(sum(a)) # append를 사용하여 sum(a)의 값을 data라는 list의 원소로 대입
b = list(map(int, input().split())) # 대입된 값을 원소로 갖는 b라는 list생성
data.append(sum(b)) # append를 사용하여 sum(b)의 값을 data라는 list의 원소로 대입
c = list(map(int, input().split())) # 대입된 값을 원소로 갖는 c라는 list생성
data.append(sum(c)) # append를 사용하여 sum(c)의 값을 data라는 list의 원소로 대입
d = list(map(int, input().split())) # 대입된 값을 원소로 갖는 d라는 list생성
data.append(sum(d)) # append를 사용하여 sum(d)의 값을 data라는 list의 원소로 대입
e = list(map(int, input().split())) # 대입된 값을 원소로 갖는 e라는 list생성
data.append(sum(e)) # append를 사용하여 sum(e)의 값을 data라는 list의 원소로 대입
print(data.index(max(data)) + 1, max(data)) # index를 사용하여 우승자의 번호를 출력하고 max를 사용하여 점수의 총합을 출력