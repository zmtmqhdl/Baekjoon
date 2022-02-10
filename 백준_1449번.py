n, l = map(int, input().split()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
start = data[0] # 테이프를 처음으로 사용하는 지점
endata = data[0] + l # 테이프를 처음으로 사용하는 지점 +  테이프 길이 = 테이프가 끝나는 지점
count = 1 # 테이프의 갯수를 저장할 count변수 생성
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복 
    if start <= data[i] < endata : # 조건문 if, else -> 물이 새는 곳의 위치가 테이프가 끝나는 지점의 위치보다 작은 경우
        continue # i로 진행되고 있는 for문을 넘어감
    else : # 물이 새는 곳의 위치가 테이프가 끝나는 지점의 위치보다 큰 경우
        start = data[i] # 테이프가 시작되는 위치를 data[i]로 변경
        endata = data[i] + l  # 테이프가 끝나는 지점의 위치를 data[i] + l로 변경
        count += 1 # count = count + 1
print(count) # 출력