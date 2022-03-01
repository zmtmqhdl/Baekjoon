data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
ascending = [1, 2, 3, 4, 5, 6, 7, 8] # 1부터 8까지 오름차순으로 된 원소를 갖는 ascending라는 list생성
descending = [8, 7, 6, 5, 4, 3, 2, 1] # 8부터 1까지 내림차순으로 된 원소를 갖는 descending라는 list생성
if data == ascending : # 조건문 if, elif -> data라는 list의 원소가 ascending라는 list의 원소와 같은 경우
    print('ascending') # 출력
elif data == descending : # data라는 list의 원소가 descending라는 list의 원소와 같은 경우
    print('descending') # 출력
elif data != ascending and data != descending : # data라는 list의 원소가  ascending라는 list의 원소, descending라는 list의 원소 중 어느 것과도 같지 않을 경우
    print('mixed') # 출력