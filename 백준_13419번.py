for _ in range(int(input())) : # 반복문 for -> 대입된 값만큼 반복
    s = input() # 값 대입
    if len(s) % 2 == 1 : # 조건문 if -> s의 길이의 값이 홀수인 경우
        for i in range(0, len(s), 2) : # 반복문 for -> 0부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        for i in range(1, len(s), 2) : # 반복문 for -> 1부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        print() # 개행 출력
        for i in range(1, len(s), 2) : # 반복문 for -> 1부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        for i in range(0, len(s), 2) : # 반복문 for -> 0부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        print() # 개행 출력
    else : # s의 길이의 값이 짝수인 경우
        for i in range(0, len(s), 2) : # 반복문 for -> 0부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        print() # 개행 출력
        for i in range(1, len(s), 2) : # 반복문 for -> 1부터 len(s) - 1까지 2의 간격으로 i에 대입하며 반복
            print(s[i], end = '') # end를 사용하여 공백을 두고 출력
        print() # 개행 출력