s = str(input()) # 값 대입
data = [-1] * 26 # -1원소를 26개 가진 data라는 list 생성
for i in range(len(s)) : # 반복문 for -> s의 길이만큼 반복
    for j in range(26) : # 반복문 for
        if s[i] == chr(97 + j) and data[j] == -1: # 조건문 if -> s를 한 문자씩 알파벳 소문자와 차례대로 비교하여 값이 같으면서 데이터 중복 입력 방지를 위해 data[j]의 값이 -1일 때
                                                  # chr은 아스키 코드를 문자로 바꿈
                data[j] = i # 값 설정
for i in data : # 반복문 for -> data라는 list의 원소를 i에 차례대로 대입
    print(i, end = ' ') # end = ' '를 사용하여 print후 개행이 아닌 띄어쓰기를 하도록 하여 출력