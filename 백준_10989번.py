import sys # sys���̺귯�� ȣ��
n = int(sys.stdin.readline()) # �׽�Ʈ Ƚ�� ����
                              # sys.stdin.readline() = input()
data = [0] * 10001 # 0���� ������ data��� list����
                   # 10001���� ���� -> �־��� ���� �ڿ����̹Ƿ� 1 ~ 10000������ ������ ���´�.
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    new_data = int(sys.stdin.readline()) # �� ����
    data[new_data] += 1 # data[new_data] = data[new_data] + 1
                        # ���Ե� ���� index�� �����ϸ� �ش� index�� ���� 1��ŭ ������Ų��.
for i in range(10001) : # �ݺ��� for
    if data[i] != 0 : # ���ǹ� if -> data[i]�� 0�� �ƴ϶��
        for j in range(data[i]) : # �ݺ��� for -> index�� ����ŭ �ݺ�
            print(i) # index���