n, m = map(int, input().split()) # 값 대입
j = int(input()) # 값 대입
move = 0 # 움직인 횟수를 저장할 move변수 초기화
start = 1 # 바구니 왼쪽 끝의 위치를 저장할 start변수에 1저장
end = m # 바구니 오른쪽 끝의 위치를 저장할 end변수에 m저장
for _ in range(j) : # 반복문 for -> j만큼 반복
    apple = int(input()) # 값 대입
    if apple < start : # 조건문 if, elif -> 사과가 바구니보다 왼쪽에 떨어지는 경우
        move += (start - apple) # move = move + (start - apple)
        start = apple # 바구니 왼쪽 끝의 위치 변경
        end = apple + m - 1 # 바구니 오른쪽 끝의 위치 변경
    elif apple > end : # 사과가 바구니보다 오른쪽에 떨어지는 경우
        move += (apple - end) # move = move + (apple - end)
        end = apple # 바구니 왼쪽 끝의 위치 변경
        start = end - m + 1 # 바구니 오른쪽 끝의 위치 변경
print(move) # 출력