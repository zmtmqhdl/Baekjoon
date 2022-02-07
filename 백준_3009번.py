x_list = [] # x값들을 수집할 x_list라는 list생성
y_list = [] # y값들을 수집할 y_list라는 list생성
for _ in range(3) : # 반복문 for
    x, y = map(int, input().split()) # 값 대입
    x_list.append(x) # x_list라는 list에 x값을 원소로 추가
    y_list.append(y) # y_list라는 list에 y값을 원소로 추가
for i in range(3) : # 반복문 for
    if x_list.count(x_list[i]) == 1: # 조건문 if -> count를 사용하여 x_list가 가진 원소 중 개수가 1개인 것을 찾아냄
        result_x = x_list[i]
    if y_list.count(y_list[i]) == 1: # 조건문 if -> count를 사용하여 y_list가 가진 원소 중 개수가 1개인 것을 찾아냄
        result_y = y_list[i]
print(result_x, result_y) # 출력
