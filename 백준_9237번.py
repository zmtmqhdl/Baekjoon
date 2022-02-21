n = int(input()) # 값 대입
tree = list(map(int, input().split())) # 대입된 값을 원소로 갖는 tree라는 list생성
tree.sort(reverse = True) # sort(reverse = True)를 사용하여 tree라는 list의 원소를 내림차순으로 정렬
for i in range(len(tree)) : # 반복문 for -> 0부터 len(tree) - 1까지 i에 차례대로 대입하며 반복
    tree[i] = tree[i] + i + 1 # 나무가 다 자라는데 걸리는 시간 연산
print(max(tree) + 1) # 이장님은 다음날 오기 때문에 max(tree) + 1을 연산하여 출력