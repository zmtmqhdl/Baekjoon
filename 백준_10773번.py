k = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(k) : # 반복문 for -> k만큼 반복
    a = int(input()) # 값 대입
    if a == 0 : # 조건문 if, else -> 재현이가 0을 외친 경우
        del data[-1] # del을 사용하여 data라는 list에서 가장 마지막 원소를 삭제
    else : # 재현이가 0을 외치지 않은 경우
        data.append(a) # append를 사용하여 data라는 list에 a를 원소로 대입
print(sum(data)) # sum을 사용하여 data라는 list의 원소의 합을 출력