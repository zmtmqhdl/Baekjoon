n = int(input()) # �� ����
score = list(map(int, input().split())) # score��� list�� �� ����
result = 0 # result �ʱ�ȭ
for i in range(n) : # �ݺ��� for
    result += score[i] / max(score) * 100 # result�� ���� �� �ջ�
print(result / n) # ��� ���