a, b, c = map(int, input().split()) # 값 대입
if a == b == c : # 조건문 if, elif, else -> 같은 눈이 3개일 경우
    print(10000 + a * 1000)
elif a == b : # 같은 눈이 2개일 경우
    print(1000 + a * 100)
elif a == c : # 같은 눈이 2개일 경우
    print(1000 + a * 100)
elif b == c : # 같은 눈이 2개일 경우
    print(1000 + b * 100)
else : # 모두 다른 눈이 나온 경우
    print(100 * max(a, b, c))