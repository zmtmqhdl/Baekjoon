n, m = map(int, input().split()) # 값 대입
card = list(map(int, input().split())) # 대입된 값을 원소로 갖는 card라는 list생성
for _ in range(m) : # 반복문 for -> m만큼 반복
    card.sort() # sort를 사용하여 card라는 list의 원소를 오름차순으로 정렬
    x = card[0] # card라는 list에서 1번째로 작은 원소를 x로 지정
    y = card[1] # card라는 list에서 2번째로 작은 원소를 y로 지정
    del card[0], card[0] # card라는 list에서 1번째로 작은 원소를 삭제
                         # card[0]을 2번 사용한 이유는 del card[0]이 1번 실행되면 0번째 index의 값이 삭제되고 바로 index값이 정렬되기 때문에 card[0]을 1번 더 실행
    card.append(x + y) # append를 사용하여 x + y의 값을 card라는 list의 원소로 추가
    card.append(x + y) # append를 사용하여 x + y의 값을 card라는 list의 원소로 추가
print(sum(card)) # sum을 사용하여 card라는 list의 원소의 합 출력