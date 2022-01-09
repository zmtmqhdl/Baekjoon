n, x = map(int, input().split()) # 값 입력
a = list(map(int, input().split())) # list형으로 값 입력
for i in a : # 반복문 -> i에 a의 값을 차례대로 대입
    if x > i :
        print(i, sep = ' ') # sep를 사용하여 출력 후 마지막에 공백