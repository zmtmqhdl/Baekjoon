n = int(input()) # 테스트 횟수 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    x, y = map(int, input().split()) # 값 대입
    data.append((y, x)) # append를 사용하여 data라는 list에 tuple형태로 x와 y값을 원소로 추가
                        # y값이 우선적으로 오름차순으로 정렬되어야 하므로 (y, x)
data.sort() # sort를 사용하여 data라는 list를 오름차순으로 정렬
for i in data : # 반복문 for -> data라는 list의 원소를 i에 차례대로 대입
    print(i[1], i[0]) # data에는 (y, x)값의 형태로 원소가 들어가 있으므로 y, x의 순서를 고려하여 tuple값을 추출하여 출력