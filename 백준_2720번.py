n = int(input()) # 테스트 횟수 대입
for _ in range(n) : # 반복문 for -> n만큼 반복
    money = int(input()) # 값 대입
    a = money // 25 # 쿼터의 개수를 구함
    money -=  25 * (money // 25) # money = money - 25 * (money // 25)
    b = money // 10 # 다임의 개수를 구함
    money -= 10 * (money // 10) # money = money - 10 * (monny // 25)
    c = money // 5 # 니켈의 개수를 구함
    money -= 5 * (money // 5) # money = money - 5 * (money // 5)
    print(a, b, c, money) # 출력