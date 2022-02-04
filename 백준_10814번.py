n = int(input()) # 테스트 횟수 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    x, y = map(str, input().split()) # 값 대입
    data.append((int(x), y)) # append를 사용하여 data에 x, y를 원소로 대입
data.sort(key = lambda x : x[0]) # lamdba를 사용하여 나이 오름차순으로 정렬
                                 # lambda 매개변수 : 표현식 -> 함수를 한 줄로 표현한 것
                                 # lambda x : (x[0], x[1])을 하게 되면 나이 오름차순, 이름 오름차순으로 정렬 가능
for i in data : # 반복문 for -> i에 daat의 원소를 차례대로 대입
    print(i[0], i[1]) # i의 0번째 index값과 1번째 index값을 분리하여 공백을 두고 출력