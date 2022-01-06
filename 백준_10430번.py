A, B, C = map(int, input().split()) # map(적용시킬 함수, 적용할 값)
print((A + B) % C) #덧셈은 + 사용, 나눗셈의 나머지는 % 사용, 곱셈은 * 사용
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)