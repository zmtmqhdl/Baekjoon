n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
print(data[(n - 1) // 2]) # 출력
                          # data라는 list에서 index의 값이 len(data) // 2인 것이 정답
                          # 여러 개의 값이 도출된 경우 가장 작은 값을 출력하므로 len(data)가 짝수인 경우는 n - 1로 해결