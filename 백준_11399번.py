n = int(input()) # �׽�Ʈ Ƚ�� ����
time_data = list(map(int, input().split())) # �Էµ� ������ ���ҷ� ���� time_data��� list����
time_data.sort() # sort�� ����Ͽ� time_data�� ������������ ����
sum = 0 # �ʿ��� �ð��� ���� �ּڰ��� ������ sum���� �ʱ�ȭ
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    for j in range(i + 1) : # �ݸ� for -> 0���� i���� j�� ���ʴ�� �����ϸ� �ݺ�
        sum += time_data[j] # sum = sum + time_data[j]
print(sum) # ���