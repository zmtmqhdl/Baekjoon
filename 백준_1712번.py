a, b, c = map(int, input().split())
if b >= c :
    print(-1)
a, b, c = map(int, input().split()) # 값 대입
if b >= c : # 조건문 if, else -> b가 c보다 커서 손익분기점이 존재하지 않을 때
    print(-1) # 출력
else : 
    print(int(a / (c - b)) + 1) # 가변비용 - 수입 = 이익)
                                # 고정비용 / 이익 + 1 = 손익분기점