def reverse(x, y) : # 함수 생성 -> 3 * 3의 크기로 원소를 뒤집는 기능
    for i in range(x, x + 3) : # 반복문 for -> x부터 x + 2까지 차례대로 i에 대입하며 반복
        for j in range(y, y + 3) : # 반복문 for -> y부터 y + 2까지 차례대로 j에 대입하며 반복
            a[i][j] = 1 - a[i][j] # 1 - 1 = 0, 1 - 0 = 1
def check() : # 함수 생성 -> a와 b를 비교하는 기능
    for i in range(n) : # 반복문 for -> 0부터 n - 1까지 차례대로 i에 대입하며 반복
        for j in range(m) : # 반복문 for -> 0부터 m - 1까지 차례대로 j에 대입하며 반복
            if a[i][j] != b[i][j] : # 조건문 if -> 3 * 3의 크기 형태로 a와 b를 비교
                return False # False 반환
    return True # True 반환
n, m = map(int, input().split()) # 값 대입
a = [list(map(int, input())) for _ in range(n)] # 2중 배열 형태로 대입된 값을 원소로 갖는 a라는 list생성
b = [list(map(int, input())) for _ in range(n)] # 2중 배열 형태로 대입된 값을 원소로 갖는 b라는 list생성
count = 0 # 행렬 a를 행렬 b로 바꾸는데 필요한 연산의 횟수를 저장할 count변수 초기화
for i in range(n - 2) : # 반복문 for -> 0부터 n - 1까지 차레대로 i에 대입하며 반복
    for j in range(m - 2) : # 반복문 for -> 0부터 m - 1까지 차례대로 j에 대입하며 반복 
        if a[i][j] != b[i][j]: # 조건문 if -> a와 b가 다를 경우
            reverse(i, j) # 함수 실행
            count += 1 # count = count + 1
if check() == True : # 조건문 if -> 행렬 a와 행렬 b가 일치할 경우
    print(count) # 출력
else: # 행렬 a를 행렬b로 바꿀 수 없는 경우
    print(-1) # 출력