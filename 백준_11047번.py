n, k = map(int, input().split()) # 값 대입
coin = [] # coin이라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복 
    coin.append(int(input())) # append를 사용하여 대입된 값을 coin이라는 list에 저장
count = 0 # 동전의 갯수를 확인할 count변수 초기화
coin.sort(reverse = True) # sort(reverse = True)를 사용해 coin이라는 list를 내림차순으로 정렬
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    count += k // coin[i] # count = count + (k // coin[i]) -> k를 coin[i]로 나눈 몫을 더함
    k = k % coin[i] # k를 coin[i]로 나눴을 때의 나머지를 k로 지정
print(count) # 출력