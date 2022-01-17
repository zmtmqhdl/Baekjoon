data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳을 data라는 list에 대입
n = str(input()) # 값 대입
for i in data : # 반복문 for -> i에 data라는 list의 원소값을 차례대로 대입
    n = n.replace(i, '*') # replace를 사용하여 i의 값을 *로 변경
print(len(n)) # 변경된 *과 변경되지 않은 알파벳 소문자들의 갯수를 len을 사용하여 출력