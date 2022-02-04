n = int(input()) # 값 대입
data = [] # data라는 list생성
          # 별 모양을 저장할 list
for _ in range(n) : # 반복문 for -> n만큼 반복 :
    data.append(["*" for _ in range(n)]) # append를 사용하여 *를 n만큼 data라는 list에 대입
                                         # n * n 형태로 *을 가진 2차원 배열
divide = n # divide변수 n으로 초기화 
count = 0 # n이 3의 몇 거듭제곱인지 파악하기 위한 count변수 생성
while divide != 1 : # 반복문 while -> n이 3의 몇 거듭제곱인지 연산
    divide /= 3 # divde = divide / 3
    count += 1 # count = count + 1
for n in range(count) : # 반복문 for -> 0부터 count - 1까지 n에 차례대로 대입하며 반복
    blank = [i for i in range(n) if (i // (3 ** n)) % 3 == 1] # blank라는 list생성 -> 공백인 좌표를 구하는 과정
    for i in blank : # 반복문 for -> blank라는 list의 원소를 차례대로 i에 대입하며 반복
        for j in blank : # 반복문 for -> blank라는 list의 원소를 차례대로 j에 대입하며 반복
            data[i][j] = " " # data[i][j]의 원소를 공백으로 바꿈
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    print("".join(i)) # join을 사용하여 i를 합쳐서 하나의 문자열로 바꿔서 출력
                      # '구분자'.join(list) -> 구분자에 _을 넣으면 list의 원소를 출력하되 문자 사이에 _을 추가하여 출력