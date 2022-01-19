n = int(input()) # 값 대입
count = 1 # 벌집의 개수 -> 입력값이 항상 1 이상
result = 1 # 결과값 -> 입력값이 항상 1 이상
while n > count : # 반복문 while -> n이 count보다 클 동안 반복
    count += 6 * result # count = count + (6 * result)
    result += 1 # result = result + 1
print(result) # 출력