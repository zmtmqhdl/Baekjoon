n, k = map(int, input().split()) # �� ����
coin = [] # coin�̶�� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ� 
    coin.append(int(input())) # append�� ����Ͽ� ���Ե� ���� coin�̶�� list�� ����
count = 0 # ������ ������ Ȯ���� count���� �ʱ�ȭ
coin.sort(reverse = True) # sort(reverse = True)�� ����� coin�̶�� list�� ������������ ����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    count += k // coin[i] # count = count + (k // coin[i]) -> k�� coin[i]�� ���� ���� ����
    k = k % coin[i] # k�� coin[i]�� ������ ���� �������� k�� ����
print(count) # ���