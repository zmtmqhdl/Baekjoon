n, m = map(int, input().split()) # 값 대입
sum = 0 # 결과를 저장할 sum변수 초기화
data = [] # data라는 list생성
for _ in range(m) : # 반복문 for -> m만큼 반복
    x, y = list(map(int, input().split())) # x, y
    data.append([x, y]) # append를 사용하여 [x, y]를 data라는 list에 원소로 추가
                        # 2중 배열 형태로 저장됨
six_data = sorted(data, key = lambda x : x[0]) # sorted(data, key = lambda x : x[0])를 사용하여 data라는 list의 원소를 x값을 기준으로 오름차순으로 정렬하여 six_data라는 list에 저장
                                               # 패키지 가격이 저렴한 순으로 정렬
one_data = sorted(data, key = lambda x : x[1]) # sorted(data, key = lambda x : x[1])를 사용하여 data라는 list의 원소를 y값을 기준으로 오름차순으로 정렬하여 six_data라는 list에 저장
                                               # 낱개 가격이 저렴한 순으로 정렬
if six_data[0][0] <= one_data[0][1] * 6 : # 조건문 if, else -> 패키지의 가격이 낱개의 가격보다 같거나 작을 경우
    sum = six_data[0][0] * (n // 6) + one_data[0][1] * (n % 6) # n을 6으로 나눈 몫 * 패키지 가격 + n을 6으로 나눴을 때의 나머지 * 낱개 가격
    if six_data[0][0] < one_data[0][1] * (n % 6) : # 조건문 if -> 구매해야하는 갯수를 초과하더라도 패키지로 구매하는 것이 저렴한 경우
        sum = six_data[0][0] * (n // 6 + 1) # (n을 6으로 나눈 몫 + 1) * 패키지 가격
else: # 패키지의 가격이 낱개로 구매하는 것보다 비싼 경우
    sum = one_data[0][1] * n # 낱개 가격 * n
print(sum) # 출력