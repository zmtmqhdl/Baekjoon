n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
kg = 1 # 무게의 최솟값을 저장할 kg변수 생성 -> 추 무게를 더해가며 i의 앞에 있는 추 무게의 합보다 i의 무게가 크면 그 사이의 값들은 표현할 수가 없음
for i in data : # 반복문 for -> data라는 원소를 i에 차례대로 대입하며 반복
    if kg < i : # 조건문 if -> 
        break # 중지
    kg += i # kg = kg + i
print(kg) # 출력