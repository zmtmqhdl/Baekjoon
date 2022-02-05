n = int(input()) # 테스트 횟수 대입
a = list(map(int, input().split())) # 값 대입
b = list(map(int, input().split())) # 값 대입
a.sort() # sort를 사용하여 a라는 list를 오름차순으로 정렬
b.sort(reverse = True) # sort(reverse = True)를 사용하여 b라는 list를 내림차순으로 정렬
sum = 0 # 합계를 저장할 sum변수 초기화
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    sum += (a[i] * b[i]) # sum = sum + (a[i] *  b[i]
print(sum) # 출력