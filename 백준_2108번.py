import sys # 라이브러리 호출
from collections import Counter # 라이브러리 호출 -> from을 사용하여 collections.Counter를 Counter로 사용할 수 있게 함
n = int(sys.stdin.readline()) # 값 대입 -> sys.stdin.readline() = input()
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(sys.stdin.readline())) # append를 사용하여 data라는 list에 대입된 값을 원소로 추가
data.sort() # sort를 사용해 data라는 list를 오름차순으로 정렬
count = Counter(data).most_common(2) # most_common을 사용해 data라는 list에 가장 많이 있는 원소 2개 선택
                                     # Counter의 자료형은 Dictionary
                                     # Counter({'A' : 5, 'B' : 4, 'C' : 3})
print(round(sum(data) / len(data))) # 산술평균 출력
print(data[len(data) // 2]) # 중앙값 출력
if len(data) > 1 : # 가정문 if, else -> n이 1개만 입력될 수도 있기 때문
    if count[0][1] == count[1][1] : # 가정문 if, else -> 최빈값이 2개 이상인 경우
        print(count[1][0]) # 최빈값 중 2번째로 작은 값 출력
    else :
        print(count[0][0]) # 최빈값 출력
else : # n이 1이라면 
    print(count[0][0]) # 출력
print(max(data) - min(data)) # 범위 출력