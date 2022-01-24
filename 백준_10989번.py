import sys # sys라이브러리 호출
n = int(sys.stdin.readline()) # 테스트 횟수 대입
                              # sys.stdin.readline() = input()
data = [0] * 10001 # 0으로 가득찬 data라는 list생성
                   # 10001개인 이유 -> 주어진 수가 자연수이므로 1 ~ 10000까지의 범위를 갖는다.
for _ in range(n) : # 반복문 for -> n만큼 반복
    new_data = int(sys.stdin.readline()) # 값 대입
    data[new_data] += 1 # data[new_data] = data[new_data] + 1
                        # 대입된 값을 index로 생각하며 해당 index의 값을 1만큼 증가시킨다.
for i in range(10001) : # 반복문 for
    if data[i] != 0 : # 조건문 if -> data[i]가 0이 아니라면
        for j in range(data[i]) : # 반복문 for -> index의 값만큼 반복
            print(i) # index출력