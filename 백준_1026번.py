n = int(input()) # �׽�Ʈ Ƚ�� ����
a = list(map(int, input().split())) # �� ����
b = list(map(int, input().split())) # �� ����
a.sort() # sort�� ����Ͽ� a��� list�� ������������ ����
b.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� b��� list�� ������������ ����
sum = 0 # �հ踦 ������ sum���� �ʱ�ȭ
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    sum += (a[i] * b[i]) # sum = sum + (a[i] *  b[i]
print(sum) # ���