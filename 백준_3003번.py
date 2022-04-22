set = [1, 1, 2, 2, 2, 8] # 올바른 세트
data = list(map(int, input().split())) # 발견한 피스
for i in range(6) : # 반복문 for -> 0부터 5까지 i에 차례대로 대입하며 반복
    print(set[i] - data[i], end = ' ') # end를 사용하여 개행 없이 출력