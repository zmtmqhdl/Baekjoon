s = int(input()) # 값 대입
n = 1 # 1부터 더해가며 최댓값을 찾을 것이므로 1부터 값을 저장할 n변수 생성
while n * (n + 1) / 2 <= s : # 반복문 while -> 
                             # n * (n + 1) / 2는 1부터 n까지의 합 공식
    n += 1 # n = n + 1
print(n - 1) # n이 s보다 커지게 되므로 n - 1출력