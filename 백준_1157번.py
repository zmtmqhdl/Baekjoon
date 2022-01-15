data = [i for i in str(input()).upper()] # 입력된 값을 대문자로 바꿔서 list에 값 대입
result = None
max = 0
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : # 조건문 for -> i에 A ~ Z까지 차례대로 문자가 들어감
    if i in data : # 조건문 if -> i에 data의 원소값이 차례대로 들어감
        temp = data.count(i) # count를 사용하여 data라는 list에서 해당 문자의 갯수를 계산
        if temp > max : # 조건문 if -> 현재 계산 중인 알파벳이 전에 계산된 알파벳의 갯수보다 많을 경우
            max = temp
            result = i
        elif temp == max : # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
            result = "?"
        else :
            continue # 반복문 안에 명시된 코드 건너뜀
print(result) # 출력