x, y, w, h = map(int, input().split()) # 값 대입
print(min(x, y, w - x, h - y)) # min을 활용해 최솟값 출력