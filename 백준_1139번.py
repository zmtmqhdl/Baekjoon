n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(n)] # 2�� ����Ʈ �������� data��� list����
                                                                              # map�� lambda�� ����Ͽ� input()�� ���� ���ԵǴ� ���� x�� �ְ� ord(x) - 65�� ���d�Ͽ� data��� list�� ���ҷ� ����
                                                                              # rstrip�� ����Ͽ� ���� ���
alpha = [0] * 26 # ������ ������ ������ 0�� 26�� ������ alpha��� list����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� �����ϸ� �ݺ�
    j = 0 # �ڸ����� �����ϱ� ���� j���� �ʱ�ȭ
    for w in data[i][: : -1] : # �ݺ��� for -> data��� list�� ���� ������ ���Һ��� �������� w�� �����ϸ� �ݺ�
        alpha[w] += (10 ** j) # alpha[w] = alpha[w] + (10 ** j) -> j�� ������Ű�� �ڸ����� ������Ŵ
        j += 1 # j = j + 1
alpha.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� alpha��� list�� ������������ ����
sum = 0 # �հ踦 ������ sum���� �ʱ�ȭ
num = 9 # ���� ū �ڸ����� ���ڿ� ���� ���� ������ num���� ����
for i in range(26) : # �ݺ��� for -> 0���� 25���� i�� ���ʴ�� �����ϸ� �ݺ�
    if alpha[i] == 0 : # ���ǹ� if
        break # ����
    sum += (alpha[i] * num) # sum = sum + (alpha[i] * num) -> ���� ū �ڸ����� ���ڿ� 9���� 1���� ���ʴ�� ���ҽ�Ű�� ����
    num -= 1 # num = num - 1
print(sum) # ���