n = int(input()) # 테스트 횟수 대입
data = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(n)] # 2중 리스트 형식으로 data라는 list생성
                                                                              # map과 lambda를 사용하여 input()을 통해 대입되는 값을 x에 넣고 ord(x) - 65롤 진햏하여 data라는 list의 원소로 대입
                                                                              # rstrip을 사용하여 개행 사용
alpha = [0] * 26 # 문자의 정보를 저장할 0을 26개 가지는 alpha라는 list생성
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 대입하며 반복
    j = 0 # 자릿수를 저장하기 위한 j변수 초기화
    for w in data[i][: : -1] : # 반복문 for -> data라는 list를 가장 마지막 원소부터 역순으로 w에 대입하며 반복
        alpha[w] += (10 ** j) # alpha[w] = alpha[w] + (10 ** j) -> j를 증가시키며 자릿수를 증가시킴
        j += 1 # j = j + 1
alpha.sort(reverse = True) # sort(reverse = True)를 사용하여 alpha라는 list를 내림차순으로 정렬
sum = 0 # 합계를 저장할 sum변수 초기화
num = 9 # 가장 큰 자릿수의 문자에 곱할 수를 저장할 num변수 생성
for i in range(26) : # 반복문 for -> 0부터 25까지 i에 차례대로 대입하며 반복
    if alpha[i] == 0 : # 조건문 if
        break # 중지
    sum += (alpha[i] * num) # sum = sum + (alpha[i] * num) -> 가장 큰 자릿수의 문자에 9부터 1까지 차례대로 감소시키며 대입
    num -= 1 # num = num - 1
print(sum) # 출력