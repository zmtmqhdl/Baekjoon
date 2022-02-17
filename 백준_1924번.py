x, y = map(int, input().split()) # 값 대입
a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # 요일의 정보를 담은 a라는 list생성
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월별 날짜의 정보를 담은 b라는 list생성
day = 0 # 날짜의 정보를 저장할 day변수 초기화
for i in range(0, x - 1) : # 반복문 for -> 0부터 x - 2까지 i에 차례대로 대입하며 반복
    day += b[i] # day = day + b[i]
day = (day + y) % 7 # day를 7로 나눠서 나머지를 연산
print(a[day]) # 출력