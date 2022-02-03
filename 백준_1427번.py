n = int(input()) # 값 대입
data = [i for i in str(n)] # data라는 list에 n을 str형으로 변환시켜 대입
data.sort(reverse = True) # sort를 사용해 data라는 list 내림차순 정렬\
                          # reverse = True일 경우는 내림차순
for i in data : # 반복문 for -> i에 data라는 list의 원소를 차례대로 대입
    print(i, end = '') # end = ''를 사용해 개행을 하지 않고 출력