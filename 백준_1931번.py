n = int(input()) # 테스트 횟수 대입
time = [] # time이라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    x, y = map(int, input().split()) # 값 대입
    time.append((x, y)) # append를 사용하여 (x, y)를 time이라는 list의 원소로 추가
time.sort() # time이라는 list를 오름차순으로 정렬 -> x의 오름차순
time.sort(key = lambda x : x[1]) # time이라는 list를 오름차순으로 정렬 -> y의 오름차순
                                 # 회의가 일찍 끝날수록 고려할 수 있는 변수가 늘어남
end = 0 # 회의가 끝난 시간을 저정할 end변수 초기화
count = 0 # 회의의 최대 갯수를 저장할 count변수 초기화
for a, b in time : # 반복문 for -> a, b에 time이라는 list에 저장된 (x, y)형태의 원소를 차례대로 대입하며 반복
    if a >= end : # 조건문 if -> 회의 시작 시간이 최근에 회의가 끝난 시간보다 이후인 경우
        count += 1 # count = count + 1
        end = b # 회의가 끝난 시간을 b로 변경
print(count) # 출력