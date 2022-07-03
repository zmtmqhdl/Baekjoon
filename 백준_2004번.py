n, m = map(int, input().split()) # 값 대입
def two_count(i) : # 함수 생성 -> 2의 개수를 세는 함수 
    two = 0 # 2의 개수를 저장할 two변수 초기화
    while i != 0 : # 반복문 while -> i가 0이 아닐 경우 반복 
        i //= 2 # i = i // 2
        two += i # two = two + i
    return two # two의 값을 반환
def five_count(i) : # 함수 생성 -> 5의 개수를 세는 함수
    five = 0 # 5의 개수를 저장할 five변수 초기화
    while i != 0: # 반복문 while -> i가 0이 아닐 경우 반복
        i //= 5 # i = i // 5
        five += i # five = five + i
    return five # five의 값을 반환
print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m))) # min을 사용하여 2와 5의 개수 중 적은 것을 출력