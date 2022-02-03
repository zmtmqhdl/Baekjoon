n = int(input()) # 테스트 횟수 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    new_data = input() # 값 대입
    if new_data not in data : # 가정문 if -> data라는 list에 new_data의 값이 없다면
        data.append(new_data) # append를 사용하여 data라는 list에 new_data를 원소로 추가
data.sort() # data라는 list를 오름차순으로 정렬
data.sort(key = len) # data라는 list를 원소의 길이가 오름차순이 되도록 정렬
                     # key = len을 사용하면 원소의 길이가 짧은 것부터 정렬이 됨
print(data) # 출력