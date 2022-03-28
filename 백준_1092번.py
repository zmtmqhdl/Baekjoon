n = int(input()) # 값 대입
crane = list(map(int, input().split())) # 대입된 값을 원소로 갖는 crane이라는 list생성
m = int(input()) # 값 대입
box = list(map(int, input().split())) # 대입된 값을 원소로 갖는 box라는 list생성
crane.sort(reverse = True) # sort(reverse = True)를 사용하여 crane이라는 list의 원소를 내림차순으로 정렬
box.sort(reverse = True) # sort(reverse = True)를 사용하여 box라는 list의 원소를 내림차순으로 정렬
time = 0 # 결과값을 저장할 time변수 초기화
checked = [0] * m # 0을 m개 가진 checked라는 list생성
count = 0 # 옮긴 박스의 개수를 저장할 count변수 초기화
position = [0] * n # 0을 n개 가진 position라는 list생성 -> 옮겨야하는 상자의 index값
if max(box) > max(crane): # 조건문 if, else -> 가장 무거운 상자를 옮길 수 없는 경우
    print(-1) # 출력
else : # 크레인이 상자를 모두 옮길 수 있는 경우
    while count < len(box) : # 반복문 while -> 상자를 다 옮기지 않았을 경우 반복
        for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
            while position[i] < len(box) : # 반복문 while -> 옮겨야하는 상자가 남은 경우 반복
                if not checked[position[i]] and crane[i] >= box[position[i]] : # 조건문 if -> 상자를 옮기지 않았고 크레인이 상자를 옮길 수 있는 경우
                    checked[position[i]] = True # 상자를 옮겼으므로 checked값을 True로 변경
                    position[i] += 1 # position[i] = position[i] + 1
                    count += 1 # count = count + 1
                    break # 중지
                position[i] += 1 # position[i] = position[i] + 1
        time += 1 # time = time + 1
    print(time) # 출력