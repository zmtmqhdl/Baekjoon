import sys # 라이브러리 호출
n = int(sys.stdin.readline()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    command = sys.stdin.readline().split() # 값 대입
    if command[0] == 'push' : # 조건문 if, elif, else -> 명령어가 push인 경우
        data.append(command[1]) # append를 사용하여 command[1]을 data라는 list의 원소로 추가
    elif command[0] == 'pop' : # 명령어가 pop인 경우
        if len(data) == 0 : # 조건문 if, else -> 스택이 빈 경우
            print(-1) # 출력
        else : # 스택이 비어있지 않은 경우
            print(data.pop()) # pop을 이용하여 가장 위에 있는 정수를 빼고 출력
    elif command[0] == 'size' : # 명령어가 size인 경우
        print(len(data)) # len을 사용하여 data라는 list의 원소의 개수를 출력
    elif command[0] == 'empty' : # 명령어가 empty인 경우
        if len(data) == 0 : # 조건문 if, else -> 스택이 빈 경우
            print(1) # 출력
        else : # 스택이 비어있지 않은 경우
            print(0) # 출력
    else : # 명령어가 top인 경우
        if len(data) != 0 : # 조건문 if, else -> 스택이 비어있지 않은 경우
            print(data[-1]) # 출력
        else : # 스택이 빈 경우
            print(-1) # 출력