n = int(input()) # 테스트 횟수 대입
data = list(map(int, input().split())) # 대입된 값을 갖는 data라는 list생성
sort_data = sorted(list(set(data))) # data를 set형으로 바꾸어 중복된 값을 제거하고 오름차순으로 정렬된 sort_data라는 list생성
result = {sort_data[i] : i for i in range(len(sort_data))} # sort_data에서 i값을 가진 원소가 몇 번째 index에 위치하고 있는지 확인하기 위해 result라는 dictionary생성
                                                           # data의 값 : 정렬되었을 때의 index값
for i in data : # 반복문 for -> i에 data의 원소를 차례대로 대입
    print(result[i], end = ' ') # end를 사용하여 개행없이 공백을 두고 출력