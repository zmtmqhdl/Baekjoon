n = int(input()) # 값 대입
data = list(map(int, input().split())) # list형식으로 공백을 두고 값 입력
print(min(data), max(data)) # min, max를 이용하여 data라는 list에서 최솟값과 최댓값을 출력