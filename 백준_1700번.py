import sys # 라이브러리 호출
n, k = map(int, sys.stdin.readline().split()) # 값 대입 -> sys.stdin.readline().split() = input().split()
plug = [0] * n # 0을 n개 가진 plug라는 list생성
               # 0은 아직 꽂지 않은 플러그
data = list(map(int, sys.stdin.readline().split())) # 대입된 값을 원소로 갖는 data라는 list생성
count = swap = num = max = 0 # 결과값을 저장할 count변수, 바꿀 값을 저장할 swap변수, data라는 list의 index값을 저장할 num변수, data라는 list의 index값을 저장할 max변수 초기화
for i in data : # 반복문 for -> data라는 list의 원소를 i에 차례대로 대입하며 반복
    if i in plug : # 조건문 if, elif, else -> i의 값이 plug라는 list에 존재할 경우
        pass # 실행할 코드가 없음
    elif 0 in plug : # plug라는 list에 0이 존재할 경우
        plug[plug.index(0)] = i # index를 사용하여 plug라는 list에 가장 처음으로 나오는 0을 i로 바꿈
    else : # 모든 플러그가 가득 찬 경우
        for j in plug : # 반복문 for -> plug라는 list의 원소를 j에 차례대로 대입하며 반복
            if j not in data[num:] : # 조건문 if, elif -> data[num:]라는 list에 j의 값이 존재하지 않을 경우
                                     # 해당 전기용품이 나중에 다시 사용되지 않을 경우
                swap = j # 뽑을 예정인 전기용품 swap변수에 저장
                break # 중지
            elif data[num:].index(j) > max : # data라는 list에서 더 나중에 사용되는 전기용품을 찾는 과정
                max = data[num:].index(j) # 더 나중에 사용되는 전기용품을 max변수에 저장
                swap = j # 뽑을 예정인 전기용품 sawp변수에 저장
        plug[plug.index(swap)] = i # index를 사용하여 plug라는 list에 swap번째에 있는 값을 i로 바꿈
        max = swap = 0 # max, swap 초기화
        count += 1 # count = count + 1
    num += 1 # num = num + 1
             # 사용된 전기용품을 제외하기 위함
print(count) # 출력