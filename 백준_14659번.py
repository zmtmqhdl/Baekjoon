n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
max_num = 0 # 가장 높은 봉우리의 정보를 저장할 max_num변수 초기화
count = 0 # 용이 공격할 수 있는 봉우리의 갯수를 저장할 count변수 초기화
max_count = 0 # 가장 많이 공격할 수 있는 봉우리의 갯수를 저장할 max_count변수 초기화
for i in data : # data라는 list의 원소를 차례대로 i에 대입하며 반복
    if i > max_num : # 조건문 if, else -> i번째 봉우리가 max_num봉우리보다 낮은 경우
        max_num = i # max_num을 i로 변경 -> 가장 높은 봉우리 변경
        count = 0 # count변수 초기화
    else : # i번째 봉우리가 max_num봉우리보다 높은 경우
        count += 1 # count = count + 1
    max_count = max(count, max_count) # max를 사용하여 count, max_count 중 높은 값을 max_count에 저장
print(max_count) # 출력