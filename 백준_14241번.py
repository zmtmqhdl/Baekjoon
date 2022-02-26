n = int(input()) # 값 대입
score = 0 # 점수를 저장할 score변ㅅ 초기화
slime = list(map(int, input().split())) # 대입된 값을 원소로 갖는 slime이라는 list생성
slime.sort(reverse = True) # sort(reverse = True)를 사용하여 slime이라는 list의 원소를 내림차순으로 정렬
while len(slime) != 1 : # 반복문 while -> len을 사용하여 구한 slime이라는 list의 원소의 갯수가 1개가 아닐 경우 반복
    slime.insert(0, slime[0] + slime[1]) # insert를 사용하여 0번째 index에 slime[0] + slime[1]의 값을 대입 
    score += (slime[1] * slime[2]) # score = score + (slime[1] + slime[2])
    del slime[1] # del을 사용하여 slime이라는 list에서 1번째 index값을 삭제
    del slime[1] # del을 사용하여 slime이라는 list에서 1번째 index값을 삭제
print(score) # 출력