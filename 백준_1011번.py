t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    x, y = map(int, input().split()) # 값 대입
    distance = y - x # 거리
    count = 0 # 공간이동 장치 작돋 횟수
    a = 0.5 # 거리가 2번에 걸쳐 1씩 증가함
    k = 0 
    while distance > k : # 반복문 while
        a += 0.5 # a = a + 0.5
        k += int(a) # k = k + int(a)
        count += 1 # count = count + 1
    print(count) # 출력
# 거리 : 0      식 : 0
# 거리 : 1      식 : 1
# 거리 : 2      식 : 1 - 1
# 거리 : 3      식 : 1 - 1 - 1
# 거리 : 4      식 : 1 - 2 - 1
# 거리 : 5      식 : 1 - 2 - 1 - 1
# 거리 : 6      식 : 1 - 2 - 2 - 1
# 거리 : 7      식 : 1 - 2 - 2 - 1 - 1
# 거리 : 8      식 : 1 - 2 - 2 - 2 - 1
# 거리 : 9      식 : 1 - 2 - 3 - 2 - 1
# 거리 : 10     식 : 1 - 2 - 3 - 2 - 1 - 1
# 거리 : 11     식 : 1 - 2 - 3 - 2 - 2 - 1
# 거리 : 12     식 : 1 - 2 - 3 - 3 - 2 - 1
# 거리 : 13     식 : 1 - 2 - 3 - 3 - 2 - 1 - 1
# 거리 : 14     식 : 1 - 2 - 3 - 3 - 2 - 2 - 1
# 거리 : 15     식 : 1 - 2 - 3 - 3 - 3 - 2 - 1
# 거리 : 16     식 : 1 - 2 - 3 - 4 - 3 - 2 - 1
# 거리 : 17     식 : 1 - 2 - 3 - 4 - 3 - 2 - 1 - 1
# 거리 : 18     식 : 1 - 2 - 3 - 4 - 3 - 2 - 2 - 1
# 거리 : 19     식 : 1 - 2 - 3 - 4 - 3 - 3 - 2 - 1
# 거리 : 20     식 : 1 - 2 - 3 - 4 - 4 - 3 - 2 - 1