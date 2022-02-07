n = 1000 - int(input()) # 값 대입 -> 지불할 돈이 1000엔 지폐이므로 1000 - int(input())
count = 0 # 동전의 개수를 저장할 count변수 초기화
coin = [500, 100, 50, 10, 5, 1] # 동전의 정보를 원소로 가진 coin이라는 list생성
for i in coin : # 반복문 for -> coin의 원소를 i에 차례대로 대입하며 반복
    count += n // i # count = count + (n // i)
    n %= i # n = n % i
print(count) # 출력