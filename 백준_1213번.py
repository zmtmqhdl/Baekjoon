n = list(map(str, input())) # �� ����
answer = '' # ���� �ʱ�ȭ
temp = '' # ���� �ʱ�ȭ
odd = 0 # Ȧ���� ������ ������ Ȯ���� odd���� �ʱ�ȭ
count = [0 for _ in range(26)] # 0�� 25���� ���ҷ� ���� count��� list����
for i in n : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    count[ord(i) - 65] += 1 # count[ord(i) - 65] = count[ord(i) - 65] + 1 
for i in range(26) : # �ݺ��� for -> 0���� 25���� i�� ���ʴ�� �����ϸ� �ݺ�
    if count[i] % 2 == 1: # ���ǹ� if -> ���ڰ� Ȧ���� ���
        odd += 1 # odd = odd + 1
        temp = chr(i + 65) # Ȧ���� ���ڸ� temp��� ������ ����
    answer += chr(i + 65) * (count[i] // 2) # ¦������ ���ڸ� ���ݸ� �Է�
reverse_answer = list(answer) # answer�� ���ҷ� ���� reverse_answer��� list����
reverse_answer.reverse() # reverse�� ����Ͽ� ���Ҹ� ������
if odd > 1 : # ���ǹ� if -> ������ Ȧ���� ���ڰ� 2�� �̻��� ���
    print("I'm Sorry Hansoo") # ���
else : # ������ Ȧ���� ���ڰ� 1���� ���
    print(answer + temp + ''.join(map(str, reverse_answer))) # ���