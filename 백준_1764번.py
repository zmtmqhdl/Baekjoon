n, m = map(int,input().split()) # 값 대입
arr1 = set() # arr1라는 집합 생성
arr2 = set() # arr2라는 집합 생성
for _ in range(n) : # 반복문 for -> n만큼 반복 
    arr1.add(input()) # add를 사용하여 arr1라는 집합에 대입된 값을 원소로 대입
for _ in range(m) : # 반복문 for -> m만큼 반복
    arr2.add(input()) # add를 사용하여 arr2라는 집합에 대입된 값을 원소로 대입
arr = sorted(list(arr1 & arr2)) # arr1, arr2라는 집합의 원소 중에서 겹치는 원소를 오름차순으로 정렬하고 그 원소들을 arr라는 집합을 만들어 원소로 대입
print(len(arr)) # len을 사용하여 arr라는 집합의 원소 개수 출력
for i in arr : # 반복문 for -> arr라는 집합의 원소를 i에 차례대로 대입하며 반복
    print(i) # 출력