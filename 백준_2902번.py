data = list(map(str, input().split('-'))) # 입력된 갑을 -라는 문자를 기준으로 나눠 원소로 가지는 data라는 list생성
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    print(i[0], end = '') # end를 사용하여 개행없이 출력